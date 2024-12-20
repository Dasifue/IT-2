from django.urls import path

from . import views

urlpatterns = [
    path('add/<int:product_id>', views.add_to_cart_view, name='add_to_cart'),
    path('remove/<int:cart_product_id>', views.remove_from_cart_view, name='remove_from_cart'),
    path('change-quantity/<int:cart_product_id>', views.change_cart_product_quantity_view, name='change_cart_product_quantity'),
]
