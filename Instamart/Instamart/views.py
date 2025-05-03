from django.shortcuts import render, redirect
from Insta_Groceries.forms import productform
from Insta_Groceries.models import product, Category  # Add Category import


def home(request):
    products = product.objects.all()
    categories = Category.objects.all()  # Get all categories
    return render(request, 'Insta_Groceries/home.html', {
        'prod': products,
        'categories': categories  # Pass categories to the template
    })

def edit_product(request, product_id):
    prod = product.objects.get(id=product_id)
    if request.method == 'POST':
        # Add request.FILES to handle image uploads
        fm = productform(request.POST, request.FILES, instance=prod)
        if fm.is_valid():
            fm.save()
            return redirect('home')
    else:
        fm = productform(instance=prod)
    return render(request, 'Insta_Groceries/edit_product.html', {'fm': fm})