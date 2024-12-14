from django.contrib import admin

from .models import CartProduct, Cart

class CartProductInline(admin.StackedInline):
    model = CartProduct
    extra = 0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'status']
    list_display_links = ['id', 'owner', 'status']
    list_filter = ['status']
    search_fields = ['owner__username', 'owner__email', 'owner__full_name']
    inlines = [CartProductInline]
