from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product
from cart.views import get_cart_count 

def list_products(request):
    products = Product.objects.all()
    cart_count = get_cart_count(request)
    return render(request, 'catalogue/products.html', {'products': products, 'cart_count': cart_count})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    cart_count = get_cart_count(request)
    return render(request, "catalogue/product_details.html", {"product": product, "cart_count": cart_count})

@login_required(login_url="/accounts/login/")
def create_product(request):
    cart_count = get_cart_count(request)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list_products")
    else:
        form = ProductForm()
    return render(request, "catalogue/create_product.html", {"form": form, "cart_count": cart_count})