from django.urls import path
from . import views

app_name = 'Insta_Groceries'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),  # Add this line
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('product/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('category/add/', views.add_category, name='add_category'),
    path('cart/', views.cart_page, name='cart_page'),
      # Add this line
    # Add more URL patterns as needed
]