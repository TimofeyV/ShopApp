from django.urls import path, include
from mainapp import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('products/', views.products, name='products'),
    path('products/<int:days>/', views.products_on_date, name='products_for_date')
]