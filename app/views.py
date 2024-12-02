from django.shortcuts import render, get_object_or_404, redirect

from .models import Category, Product, Comment, CommentProductImage

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


def create_comment(request):
    data = {
        "email": request.POST['email'],
        "text": request.POST['text'],
        "rating": request.POST['rating'],
        "product_id": request.POST['product_id']
    }
    Comment.objects.create(**data)
    return redirect(request.META.get("HTTP_REFERER", '/'))
