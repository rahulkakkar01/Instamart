from django.contrib import admin
from .models import Category, product

# Register Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# Register product model
@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category')
    list_filter = ('category',)
    search_fields = ('product_name', 'description')
