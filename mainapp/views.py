from datetime import date, timedelta, datetime
from django.shortcuts import render
import logging
from .models import Order, Product, User

logger = logging.getLogger(__name__)

menu = [
    {"name": "Главная", "url": "index"},
    {"name": "Обо мне", "url": "about"},
    {"name": "Товары", "url": "products"},
    {"name": "Контакты", "url": "index"},
    #  {'name': 'Регистрация',
    #   'url': "index"}
]


def index(request):
    logger.info("Index page accessed")
    context = {
        "title": "Главная",
        "menu": menu,
    }
    return render(request, "mainapp/index.html", context)


def about(request):
    context = {"title": "Информация", "menu": menu}
    logger.info("About page accessed")
    return render(request, "mainapp/about.html", context)


def products(request):
    logger.info("Orders page accessed")
    date = datetime.today()
    date_for_search = date - timedelta(7)
    products = Product.objects.filter(order__date_ordered__range=[date_for_search,date]).distinct()
    context = {"title": "Заказы", "menu": menu, "products": products,
    'days': 7}

    return render(request, "mainapp/products_for_day.html", context)


def products_on_date(request, days):
    logger.info("Orders for days page accessed")
    date = datetime.today()
    if days == 7:
        date_for_search = date - timedelta(7)
    elif days == 30:
        date_for_search = date - timedelta(30)
    elif days == 365:
        date_for_search = date - timedelta(365)
    products = Product.objects.filter(order__date_ordered__range=[date_for_search,date]).distinct() 
    context = {
    "title": "Заказы",
    "menu": menu, 
    "products": products,
    'days': days
    }

    return render(request, "mainapp/products_for_day.html", context)
