from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from .models import *  # импортируем модели для дальнейшей работы с ними


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не существует или не найдена</h1>')


# Create your views here.
# список меню - словари с заголовками и url-адресами
menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Главная", 'url_name': 'home'},
        {'title': "Добавить товар", 'url_name': 'add_product'},
        {'title': "Корзина", 'url_name': 'cart'},
        {'title': "Войти", 'url_name': 'login'},
        ]


def index(request):  # главная корзина
    products = Products.objects.all()
    categories = Сategories.objects.all()
    context = {
        'product': products,  # перечень (список) товаров
        'cats': categories,  # список категорий
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'shop/index.html', context=context)


def about(request):  # страница о сайте
    return render(request, 'shop/about.html', {'menu': menu, 'title': 'О сайте'})


def addprod(request):  # страница добавления продукта
    return HttpResponse("Добавление нового товара")


def login(request):  # страница авторизации
    return HttpResponse("Авторизация")


def cart(request):  # страница корзины пользователя
    return HttpResponse("Корзина")



def show_prod(request, prod_slug):
    prod = get_object_or_404(Products, slug=prod_slug)
    categories = Сategories.objects.all()

    context = {
        'product': prod,  # товар
        'cats': categories,  # категория товара
        'menu': menu,  # меню
        'title': prod.name,
        'cat_selected': prod.category,
    }

    return render(request, 'shop/product.html', context=context)


def show_category(request, cat_id):
    products = Products.objects.filter(category_id=cat_id)
    categories = Сategories.objects.all()

    if len(products) == 0:
        raise Http404()

    context = {
        'product': products,  # перечень (список) товаров
        'cats': categories,  # список категорий
        'menu': menu,
        'title': f'Категория {cat_id}',
        'cat_selected': cat_id,
    }
    return render(request, 'shop/index.html', context=context)


