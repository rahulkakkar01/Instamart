from django import forms
from .models import product, Category

class productform(forms.ModelForm):
    class Meta:
        model = product
        fields = ['product_name', 'description', 'price', 'stock', 'category', 'image']
       

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']