from django.contrib import admin
from .models import *

# Логин и пароль: admin
# Register your models here.

# Классы моделей отображаемые в админке


class ProductAdmin(admin.ModelAdmin):  # отображение товаров
    # список, что видно на "админ панели"
    list_display = ('id', 'name', 'category', 'price')
    list_display_links = ('id', 'name')  # на что можно перейти
    search_fields = ('name', 'category')  # по каким полям можно искать
    list_editable = ('price', )  # список редактируемых полей
    list_filter = ('name', 'price', 'time_create')  # поля фильтров
    prepopulated_fields = {"slug": ("name",)}  # поле переводимое в URL-адрес


class CategoryAdmin(admin.ModelAdmin):  # отображение категорий товаров
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


# Регистрация класов на странице админа


admin.site.register(Products, ProductAdmin)
admin.site.register(Сategories, CategoryAdmin)
