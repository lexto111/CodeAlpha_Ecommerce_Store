## Nova Store — Full Stack E-commerce Website 

Developed by: god ferry lexto

GitHub: https://github.com/lexto111

Project: CodeAlpha Internship — Task 1

Role: Python / Django Developer

## About the Project

I developed Nova Store as part of my CodeAlpha internship (Task 1 — Simple E-commerce Store).

This project is a full-stack e-commerce web application developed using Python, Django, HTML, CSS, JavaScript and SQLite.

The application allows users to browse products, view product details, create accounts, manage shopping carts, place orders and track their previous purchases.

Through this project, I gained practical experience in Django web development, database management, user authentication, backend development and frontend integration.

> Internship task: CodeAlpha — Task 1, Simple E-commerce Store

## Features

- Product catalogue with product images, descriptions, prices, and stock.
- Individual product detail pages.
- Add-to-cart, quantity update, and remove-from-cart actions.
- User registration, login, and logout using Django authentication.
- Login-protected checkout and order history.
- Order and order-item records stored in the database.
- Stock availability validation and stock reduction after successful order placement.
- Django admin interface for managing products and reviewing orders.
- Responsive layout for desktop and mobile screens.

## Tech stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Python, Django |
| Database | SQLite |
| Authentication | Django built-in authentication |
| Admin | Django Admin |

## Project structure

```text
django_ecommerce_store/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── store_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── shop/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
├── templates/
│   ├── base.html
│   └── shop/
└── static/
    ├── css/style.css
    └── js/main.js
```

## Run locally

### 1. Requirements

- Python 3.10 or newer
- pip

### 2. Download and open the project

Extract the ZIP file, open the extracted folder in VS Code, and open a terminal in that folder.

### 3. Create a virtual environment

**Windows**
```bash
py -m venv venv
venv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create database tables

```bash
python manage.py migrate
```

### 6. Create an administrator

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin username and password.

### 7. Start the development server

```bash
python manage.py runserver
```

Open the website at http://127.0.0.1:8000/ and the admin panel at http://127.0.0.1:8000/admin/.

## Add products

1. Sign in to `/admin/` using the superuser account.
2. Open **Products** and select **Add product**.
3. Enter the product name, description, price, stock quantity, and an image URL (optional).
4. Save the product. It will appear in the shop catalogue.

## Main application routes

| Route | Purpose |
|---|---|
| `/` | Product catalogue |
| `/product/<id>/` | Product details |
| `/cart/` | Shopping cart |
| `/register/` | Create an account |
| `/login/` | Sign in |
| `/checkout/` | Place an order (login required) |
| `/orders/` | View the signed-in user's orders |
| `/admin/` | Django administration |

## Database design

- **Product**: name, description, price, image URL, available stock, creation date.
- **Order**: customer, delivery name, phone, address, total, order status, creation date.
- **OrderItem**: related order, product reference, product-name snapshot, unit-price snapshot, quantity.
- **User**: Django's built-in user model stores account and authentication details.

The cart is stored in the visitor's Django session. A completed checkout creates an Order and associated OrderItem records.

## Test checklist

- [ ] Open the home page and confirm products are displayed.
- [ ] Open a product detail page.
- [ ] Register a new account.
- [ ] Log out and log back in.
- [ ] Add a product to the cart.
- [ ] Change the quantity and remove a product.
- [ ] Try checkout while logged out; confirm login is required.
- [ ] Place an order while logged in.
- [ ] Confirm the order appears in **My orders**.
- [ ] Confirm product stock decreases after the order.
- [ ] Open Django Admin and verify the product and order records.

## Screenshots for your submission

Capture your own screenshots after running the project. Suggested screenshots:

1. `01-homepage.png` — product catalogue.
2. `02-product-details.png` — an individual product page.
3. `03-shopping-cart.png` — cart with one or more products.
4. `04-registration-or-login.png` — account screen.
5. `05-checkout.png` — delivery form and order total.
6. `06-order-history.png` — placed order.
7. `07-admin-products.png` — product management in Django Admin.

Save them in a folder named `screenshots/` before submitting your GitHub repository.

## What I Learned

Through this project, I gained practical experience in:

- Building web applications using Django.
- Creating and managing database models.
- Implementing user registration and authentication.
- Developing shopping cart functionality.
- Handling order processing and stock management.
- Integrating frontend and backend components.
- Using Git and GitHub for version control.

## Limitations and production improvements

This is an educational starter project, not a production-ready store. It does not collect real payments or send order-confirmation emails. Before deployment, configure environment-based secrets, `DEBUG=False`, allowed hosts, HTTPS and secure cookies; add payment-gateway integration, email notifications, automated tests, logging, and production database settings. For production concurrency, review database locking and stock reservation behaviour for the chosen database.

## Author

god ferry lexto

GitHub: https://github.com/lexto111

Project: Nova Store — full stack E-commerce Website

Internship: CodeAlpha

Task: Simple E-commerce Store

If you find this project interesting, feel free to explore the repository.
