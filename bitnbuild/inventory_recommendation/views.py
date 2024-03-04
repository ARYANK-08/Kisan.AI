from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

def post_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list page
    else:
        form = ProductForm()
    return render(request, 'post_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def bids_page(request):
    return render(request, 'bids.html')

