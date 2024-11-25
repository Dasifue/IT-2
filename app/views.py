from django.shortcuts import render

from .models import Category, Product

def render_index(request):

    categories = Category.objects.all()[:6]
    products = Product.objects.all()[:8]

    context = {
        "categories": categories,
        "products": products
    }
    return render(request, "index.html", context)
