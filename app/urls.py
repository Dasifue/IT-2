from django.urls import path

from . import views

urlpatterns = [
    path('', views.render_index, name='index'),
    path('category/<int:pk>', views.get_products_by_category, name='category')
]