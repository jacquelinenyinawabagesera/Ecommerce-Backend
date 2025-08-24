from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from catalogue.models import Product

def get_or_create_cart(request):
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart = Cart.objects.filter(id=cart_id).first()
        if cart:
            return cart
    cart = Cart.objects.create()
    request.session['cart_id'] = cart.id
    return cart

def get_cart_count(request):
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.filter(id=cart_id).first()
    return sum(item.quantity for item in cart.items.all()) if cart else 0

def update_cart_item(request, product_id):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, id=product_id)
    item = CartItem.objects.filter(cart=cart, product=product).first()
    try:
        quantity = int(request.POST.get('quantity', 1))
    except (TypeError, ValueError):
        quantity = 1

    if item:
        if quantity < 1:
            item.delete()
        else:
            item.quantity = quantity
            item.save()
    return redirect('cart:cart_detail')

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_or_create_cart(request)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.filter(id=cart_id).first()
    items = cart.items.all() if cart else []
    total = sum(item.product.price * item.quantity for item in items)
    cart_count = sum(item.quantity for item in items)
    return render(request, 'cart/cart_detail.html', {
        'items': items,
        'total': total,
        'cart_count': cart_count
    })

def remove_from_cart(request, product_id):
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.filter(id=cart_id).first()
    if cart:
        cart.items.filter(product_id=product_id).delete()
    return redirect('cart:cart_detail')