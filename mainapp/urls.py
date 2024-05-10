from django.urls import path, include
from mainapp import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('products/', views.products, name='products'),
    path('products/<int:days>/', views.products_on_date, name='products_for_date'),
    path('registration/', views.add_user, name = 'registration'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<int:id>/', views.product_detail, name='product_detail'),
    path('catalog/<int:id>/addimage', views.add_product_image, name="add_product_image"),
]