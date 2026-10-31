from decimal import Decimal
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from .forms import RegisterForm, CheckoutForm
from .models import Product, Order, OrderItem

def _cart_data(request):
    cart = request.session.get("cart", {})
    items, total = [], Decimal("0.00")
    for product_id, quantity in cart.items():
        product = Product.objects.filter(pk=product_id).first()
        if product and int(quantity) > 0:
            line_total = product.price * int(quantity)
            items.append({"product": product, "quantity": int(quantity), "line_total": line_total})
            total += line_total
    return items, total

def home(request):
    return render(request, "shop/home.html", {"products": Product.objects.all()})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "shop/product_detail.html", {"product": product})

def cart(request):
    items, total = _cart_data(request)
    return render(request, "shop/cart.html", {"items": items, "total": total})

def add_to_cart(request, pk):
    if request.method != "POST":
        return redirect("product_detail", pk=pk)
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get("cart", {})
    current = int(cart.get(str(pk), 0))
    if current < product.stock:
        cart[str(pk)] = current + 1
        request.session["cart"] = cart
        messages.success(request, "Product added to your cart.")
    else:
        messages.warning(request, "Available stock limit reached.")
    return redirect("cart")

def update_cart(request, pk):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=pk)
        try:
            quantity = int(request.POST.get("quantity", 1))
        except ValueError:
            quantity = 1
        cart = request.session.get("cart", {})
        if quantity <= 0:
            cart.pop(str(pk), None)
        elif quantity <= product.stock:
            cart[str(pk)] = quantity
        else:
            messages.warning(request, f"Only {product.stock} item(s) available.")
        request.session["cart"] = cart
    return redirect("cart")

def remove_from_cart(request, pk):
    if request.method == "POST":
        cart = request.session.get("cart", {})
        cart.pop(str(pk), None)
        request.session["cart"] = cart
    return redirect("cart")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Your account has been created.")
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "shop/register.html", {"form": form})

@login_required
def checkout(request):
    items, total = _cart_data(request)
    if not items:
        messages.info(request, "Your cart is empty.")
        return redirect("home")
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                # Re-check stock while creating the order.
                for item in items:
                    product = Product.objects.select_for_update().get(pk=item["product"].pk)
                    if product.stock < item["quantity"]:
                        messages.error(request, f"Not enough stock for {product.name}.")
                        return redirect("cart")
                order = Order.objects.create(
                    user=request.user, full_name=form.cleaned_data["full_name"],
                    phone=form.cleaned_data["phone"], address=form.cleaned_data["address"],
                    total=total,
                )
                for item in items:
                    product = Product.objects.select_for_update().get(pk=item["product"].pk)
                    OrderItem.objects.create(
                        order=order, product=product, product_name=product.name,
                        price=product.price, quantity=item["quantity"],
                    )
                    product.stock -= item["quantity"]
                    product.save(update_fields=["stock"])
            request.session["cart"] = {}
            messages.success(request, f"Order #{order.pk} placed successfully.")
            return redirect("order_history")
    else:
        form = CheckoutForm(initial={"full_name": request.user.get_full_name() or request.user.username})
    return render(request, "shop/checkout.html", {"form": form, "items": items, "total": total})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).prefetch_related("items")
    return render(request, "shop/orders.html", {"orders": orders})
