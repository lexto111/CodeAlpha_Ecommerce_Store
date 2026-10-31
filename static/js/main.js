// Small progressive enhancement: confirm before removing an item.
document.querySelectorAll('form[action*="/cart/remove/"]').forEach((form) => {
  form.addEventListener('submit', (event) => {
    if (!window.confirm('Remove this item from your cart?')) event.preventDefault();
  });
});
