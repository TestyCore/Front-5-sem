from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from edostavka.models import Product
from .cart import Cart


@user_passes_test(lambda user: user.groups.filter(name='Customer').exists())
@require_POST
def cart_add(request, product_id):
    if not request.user.is_authenticated:
        return redirect('index')

    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart:cart_detail')


@user_passes_test(lambda user: user.groups.filter(name='Customer').exists())
def cart_remove(request, product_id):
    if not request.user.is_authenticated:
        return redirect('index')

    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


@user_passes_test(lambda user: user.groups.filter(name='Customer').exists())
def cart_detail(request):
    if not request.user.is_authenticated:
        return redirect('index')
    # cart = Cart(request)
    return render(request, 'cart/detail.html')
