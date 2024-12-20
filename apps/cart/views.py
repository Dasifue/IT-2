from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Cart, CartProduct


def cart_active(func):
    def wrapper(request, *args, **kwargs):
        if request.user.cart.status == Cart.WAITING:
            return redirect('index')
        return func(request, *args, **kwargs)
    return wrapper

@login_required
@cart_active
def add_to_cart_view(request, product_id):

    quantity = int(request.GET.get('quantity', 1))

    cart_product = CartProduct.objects.filter(
        cart=request.user.cart,
        product_id=product_id
    )
    if cart_product.exists():
        cart_product = cart_product.first()
        cart_product.quantity += quantity
        cart_product.save()
    else:
        CartProduct.objects.create(
            cart=request.user.cart,
            product_id=product_id,
            quantity=quantity,
        )

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
@cart_active
def remove_from_cart_view(request, cart_product_id):
    
    try:
        cart_product = CartProduct.objects.get(id=cart_product_id)
    except CartProduct.DoesNotExist:
        pass
    else:
        cart_product.delete()
    
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
@cart_active
def change_cart_product_quantity_view(request, cart_product_id):
    quantity = request.GET.get('quantity')
    if quantity is None:
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    quantity = int(quantity)
    if 1 > quantity > 100:
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    try:
        cart_product = CartProduct.objects.get(id=cart_product_id)
    except CartProduct.DoesNotExist:
        return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        cart_product.quantity = quantity
        cart_product.save()
    
    return redirect(request.META.get('HTTP_REFERER', '/'))