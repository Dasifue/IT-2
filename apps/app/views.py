from django.shortcuts import render, get_object_or_404, redirect

from .models import Category, Product, Comment, CommentProductImage
from .forms import CommentCreationForm

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
    products = Product.objects.filter(category=category).order_by('-created')
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'category.html', context)

def get_product_by_id(request, pk): 
 
    product = get_object_or_404(Product, id=pk) 
    form = CommentCreationForm() 
 
    if request.method == "POST": 
        form = CommentCreationForm(data=request.POST) 
        if form.is_valid(): 
            comment = form.save(commit=True) 
            photos = request.FILES.getlist('photos') 
            if photos: 
                for file in photos: 
                    CommentProductImage.objects.create(comment=comment, image=file) 
 
    context = { 
        "product": product, 
        "form": form 
    } 
    return render(request, "product.html", context)

