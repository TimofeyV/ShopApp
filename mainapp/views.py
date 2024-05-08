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
    return render(request, 'index.html', context)


def about(request):
    context = {
        'title': "Информация",
        'menu': menu
    }
    logger.info("About page accessed")
    return render(request, 'about.html', context)