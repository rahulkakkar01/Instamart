from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from Insta_Groceries.models import product, Category
from Insta_Groceries.forms import productform, CategoryForm  # Import from the main project forms

# Create your views here.
def home(request):
    prod = product.objects.all()
    if request.method == 'POST':
        # Add request.FILES to handle image uploads
        fm = productform(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect('home')
    else:
        fm = productform()
    return render(request, 'Insta_Groceries/home.html', {'prod': prod, 'fm': fm})

def product_list(request):
    # Get category parameter from URL
    category_id = request.GET.get('category')
    current_category = None
    
    # Get all categories for the filter buttons
    categories = Category.objects.all()
    
    # Filter products by category
    if category_id:
        try:
            current_category = Category.objects.get(id=category_id)
            # Only show products from selected category
            products = product.objects.filter(category=current_category)
        except (Category.DoesNotExist, ValueError):
            # Fallback if category doesn't exist
            products = product.objects.all()
    else:
        # Show all products when no category is selected
        products = product.objects.all()
        
    return render(request, 'Insta_Groceries/product_list.html', {
        'products': products,
        'categories': categories,
        'current_category': current_category
    })

def product_detail(request, product_id):
    product_item = get_object_or_404(product, id=product_id)
    return render(request, 'Insta_Groceries/product_detail.html', {'product': product_item})

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def edit_product(request, product_id):
    product_obj = get_object_or_404(product, id=product_id)
    
    if request.method == 'POST':
        form = productform(request.POST, request.FILES, instance=product_obj)
        if form.is_valid():
            form.save()
            # Redirect back to the product list, potentially with the same category filter
            category_id = request.GET.get('category')
            if category_id:
                return redirect(f"{reverse('Insta_Groceries:product_list')}?category={category_id}")
            return redirect('Insta_Groceries:product_list')
    else:
        form = productform(instance=product_obj)
    
    return render(request, 'Insta_Groceries/edit_product.html', {
        'form': form,
        'product': product_obj
    })

@user_passes_test(is_admin)
def delete_product(request, product_id):
    product_obj = get_object_or_404(product, id=product_id)
    
    # Store category ID for redirecting back to the same category
    category_id = request.GET.get('category')
    
    # Delete the product
    product_obj.delete()
    
    # Redirect back to the product list, potentially with the same category filter
    if category_id:
        return redirect(f"{reverse('Insta_Groceries:product_list')}?category={category_id}")
    return redirect('Insta_Groceries:product_list')

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'Insta_Groceries/add_category.html', {'form': form})

@user_passes_test(is_admin)
def add_product(request):
    if request.method == 'POST':
        form = productform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Insta_Groceries:product_list')
    else:
        form = productform()
    
    return render(request, 'Insta_Groceries/add_product.html', {
        'form': form,
        'categories': Category.objects.all()
    })

def cart_page(request):
    return render(request, 'Insta_Groceries/cart_page.html')