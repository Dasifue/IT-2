from django.contrib import admin

from .models import Category, Product, Comment, CommentProductImage

admin.site.register(Category)
admin.site.register(Product)


class CommentProductImageInline(admin.StackedInline):
    model = CommentProductImage
    extra = 0

@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ['id', 'product', 'rating', 'created']
    list_display_links = ['id', 'rating', 'created', 'product']
    list_filter = ['rating']
    search_fields = ['product__name']
    inlines = [CommentProductImageInline]
