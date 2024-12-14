from django.db import models

from apps.users.models import User

class Cart(models.Model):
    ACTIVE = 'active'
    WAITING = 'waiting'

    CartStatuses = (
        (ACTIVE, 'Active'),
        (WAITING, 'Waiting for payment')
    )

    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="cart"
    )
    products = models.ManyToManyField(
        "app.Product", through="cart.CartProduct"
    )
    status = models.CharField(max_length=20, choices=CartStatuses, default=ACTIVE)


class CartProduct(models.Model):

    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="cart_products"
    )
    product = models.ForeignKey(
        "app.Product", on_delete=models.CASCADE, related_name="cart_products"
    )
    quantity = models.PositiveSmallIntegerField(default=1)
