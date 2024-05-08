from django.shortcuts import render
import logging


logger = logging.getLogger(__name__)

menu = [
    {'name': 'Главная',
     'url': 'index'},
    {'name': 'Обо мне',
     'url': 'about'},
     {'name': 'Каталог',
     'url': 'index'},
     {'name': 'Контакты',
     'url': 'index'},
    #  {'name': 'Регистрация',
    #   'url': "index"} 
]


def index(request):
    logger.info("Index page accessed")
    context = {
        'title': 'Главная',
        'menu': menu,
    }
    return render(request, 'mainapp/index.html', context)


def about(request):
    context = {
        'title': "Информация",
        'menu': menu
    }
    logger.info("About page accessed")
    return render(request, 'mainapp/about.html', context)


def orders_on_date(request, days):
    context = {
        'title': "Заказы",
        'menu': menu,
    }
    logger.info('Orders for days page accessed')
    return render(request, 'mainapp/orders_for_day.html')