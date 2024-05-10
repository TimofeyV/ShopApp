from datetime import date, timedelta, datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
import logging
from .models import Order, Product, User
from .forms import UserForm, AddImageForm
from django.core.files.storage import FileSystemStorage


logger = logging.getLogger(__name__)

menu = [
    {"name": "Главная", "url": "index"},
    {"name": "Обо мне", "url": "about"},
    {"name": "Заказы", "url": "products"},
    {"name": "Товары", "url": "catalog"},
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


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            logger.info(f'Получили {name=}, {email=}, {phone=}, {address=}.')
    else:
        form = UserForm()
        context = {
            "title": "Регистрация",
            "menu": menu,
            'form': form
        }     
        return render(request, 'mainapp/user_form.html', context)


def catalog(request):
    products = Product.objects.all()
    context = {
        "title": "Товары",
        "menu": menu,
        'products': products
    }
    return render(request, 'mainapp/catalog.html', context)


def product_detail(request, id):
    product = get_object_or_404(Product, pk = id)
    context = {
        "title": product.name,
        "menu": menu,
        'product': product,
    }
    return render(request, 'mainapp/product_detail.html', context)


def add_product_image(request, id):  
    product = get_object_or_404(Product, pk = id) 
    if request.method == 'POST':
        form = AddImageForm(request.POST, request.FILES)              
        if form.is_valid():
            image = form.cleaned_data['image']
            product.image = image
            product.save()     
            logger.info(f'Success upload image')
            return redirect("catalog")

    else:
        # product = get_object_or_404(Product, pk = id)
        form = AddImageForm(instance=product)
        context = {
            "title": "Добавить изображение",
            "menu": menu,
            'form': form
        }           
        logger.info("Add image for product page accessed")
        return render(request, 'mainapp/add_image_form.html', context)

