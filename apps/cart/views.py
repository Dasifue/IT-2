from django.shortcuts import render, redirect

from .models import Cart, CartProduct

def add_to_cart_view(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.user.cart.status == Cart.WAITING:
        return redirect('index')

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


def remove_from_cart_view(request, cart_product_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.user.cart.status == Cart.WAITING:
        return redirect('index')
    
    try:
        cart_product = CartProduct.objects.get(id=cart_product_id)
    except CartProduct.DoesNotExist:
        pass
    else:
        cart_product.delete()
    
    return redirect(request.META.get('HTTP_REFERER', '/'))