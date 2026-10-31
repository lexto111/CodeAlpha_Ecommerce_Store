# Project Report: Nova Store — Simple E-commerce Website

## 1. Introduction
Nova Store is a web-based e-commerce application developed using Django and Python. The application allows visitors to browse available products, view product information, add items to a shopping cart, create an account, and place orders.

## 2. Objective
The objective is to demonstrate a basic full-stack shopping application with a frontend, backend, database, authentication, cart management, and order processing.

## 3. Tools and technologies
- Frontend: HTML, CSS, JavaScript
- Backend framework: Django (Python)
- Database: SQLite
- Authentication: Django authentication
- Development environment: Python and Visual Studio Code

## 4. Modules
### Product catalogue
Displays products with names, descriptions, prices, and optional image URLs.

### Product details
Shows the selected product's full description, price, and stock availability.

### Shopping cart
Stores cart contents in the user's session and supports quantity updates and item removal.

### User authentication
Allows users to register, log in, and log out.

### Checkout and order processing
Authenticated users submit delivery information. The application validates stock, creates an order and its line items, and reduces product stock.

### Order history
Displays the signed-in user's previous orders and their status.

### Admin management
Administrators can add and edit products and review orders through Django Admin.

## 5. Database design
| Model | Purpose |
|---|---|
| User | Stores account credentials and user information through Django |
| Product | Stores catalogue details and available stock |
| Order | Stores customer delivery details, total, status, and date |
| OrderItem | Stores each product, unit price, and quantity belonging to an order |

## 6. Application workflow
1. The administrator adds products through Django Admin.
2. A visitor opens the store and browses the catalogue.
3. The visitor opens a product and adds it to the cart.
4. The visitor registers or logs in.
5. The customer enters delivery information at checkout.
6. The backend checks stock and creates the order.
7. The customer can review the order in order history.

## 7. Testing plan
Test product display, product details, registration, login/logout, cart addition, quantity updates, removal, login-protected checkout, order creation, stock reduction, and order history. Record actual results after running the application; do not mark tests as passed until they have been performed.

## 8. Result
The project provides the core workflow of a simple online store. It demonstrates Django models, views, URL routing, templates, forms, sessions, authentication, database relationships, and admin management.

## 9. Future enhancements
- Integrate a secure payment gateway.
- Add product categories, search, sorting, and filtering.
- Add product reviews and ratings.
- Send order confirmation emails.
- Add order tracking and cancellation.
- Add automated unit and integration tests.
- Deploy with production-grade settings and a production database.

## 10. Conclusion
Nova Store demonstrates how a basic e-commerce application can be built with Django and standard frontend technologies. It can be extended with payment, notification, and deployment features as a future improvement.
