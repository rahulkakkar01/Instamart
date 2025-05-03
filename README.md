# Instamart - Online Grocery Shopping Platform


Project Overview
Instamart is a fully-featured online grocery shopping platform built with Django. The application allows users to browse grocery products, add them to cart, and complete purchases. With a responsive design and modern UI, Instamart provides a seamless shopping experience for customers looking to purchase groceries online.

Features
User Authentication: Secure signup, login, and profile management
Product Browsing: Browse products by categories with intuitive navigation
Shopping Cart: Add products to cart, update quantities, and proceed to checkout
Admin Panel: Manage products, categories, and orders through Django's admin interface
Responsive Design: Optimized for both desktop and mobile devices
Dynamic UI Elements: Floating veggie animations, interactive reviews, and category navigation
Search Functionality: Find products quickly with search capability
Tech Stack
Backend: Django (Python web framework)
Frontend: HTML, CSS, JavaScript
Database: SQLite (development) / PostgreSQL (production)
Media Storage: Django's built-in media handling system
Authentication: Django's authentication system
# Installation

Clone the repository:
```
git clone https://github.com/yourusername/instamart.git

cd instamart
```
Create and activate a virtual environment:
```
python -m venv venv
# For Windows
venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate
```
Install dependencies:
```
pip install -r requirements.txt
```
Apply migrations:
```
python manage.py migrate
```
Create a superuser:
```
python manage.py createsuperuser
```
Run the development server:
```
python manage.py runserver
```
Access the application at http://127.0.0.1:8000/
# Project Structure
```
Instamart/
├── accounts/                  # User authentication app
│   ├── templates/
│   │   └── accounts/          # Authentication templates
│   ├── views.py               # Authentication views
│   └── urls.py                # Authentication URLs
├── Insta_Groceries/           # Main groceries app
│   ├── templates/
│   │   └── Insta_Groceries/   # Main application templates
│   ├── static/                # Static assets
│   ├── models.py              # Database models
│   ├── views.py               # Application views
│   └── urls.py                # Application URLs
├── Instamart/                 # Project settings directory
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL configuration
│   └── wsgi.py                # WSGI configuration
├── media/                     # Media files (product images)
├── manage.py                  # Django management script
└── requirements.txt           # Project dependencies
```
Usage
For Customers
Browse Products: Navigate through categories or use the search bar to find products
Add to Cart: Click "Add to Cart" to add products to your shopping cart
Manage Cart: View your cart, update quantities, or remove items
Checkout: Complete your purchase by providing delivery and payment information
For Administrators
Access the admin panel at http://127.0.0.1:8000/admin/
Log in with your superuser credentials
Manage products, categories, and user accounts
View and process orders
Key Components
Home Page
Features a dynamic navigation bar
Displays featured products and categories
Shows customer reviews and trust indicators
Product Listing
Displays products in a grid layout with essential information
Filters products by categories
Provides search functionality
Authentication Pages
User-friendly signup and login forms
Error handling and validation
Secure password management
Shopping Cart
Real-time cart updates
Quantity management
Order summary before checkout
Development Guidelines
Follow PEP 8 style guidelines for Python code
Use semantic HTML and CSS BEM naming convention
Keep JavaScript modular and focused on specific functionality
Document code with clear comments and docstrings
Write tests for critical functionality


Contributors
Rahul Kakkar - Project Lead and Developer


Acknowledgments
Django documentation and community
Bootstrap framework for UI components
FontAwesome for icons

