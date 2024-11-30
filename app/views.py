from django.shortcuts import render, get_object_or_404

from .models import Category, Product

def render_index(request):

    categories = Category.objects.all()[:6]
    products = Product.objects.all()[:8]

    context = {
        "categories": categories,
        "products": products
    }
    return render(request, "index.html", context)


def get_products_by_category(request, pk):

    category = get_object_or_404(Category, id=pk)
    products = Product.objects.filter(category=category.id)

    context = {
        "category": category,
        "products": products
    }
    return render(request, "category.html", context)

def get_product_by_id(request, pk):

    product = get_object_or_404(Product, id=pk)

    context = {
        "product": product
    }
    return render(request, "product.html", context)
