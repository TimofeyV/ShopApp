from django.urls import path, include
from mainapp import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('orders/<int:days>/', views.orders_on_date, name='orders_on_date')
]