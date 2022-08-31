from django.db import models
from django.urls import reverse
# Create your models here.



class Сategories(models.Model):  # БД Категории
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')  # Название категории
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='URL')  # URL-адрес

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']  # сортировка по полям

    def __str__(self):  # отображение заголовков записи модели
        return self.name

    def get_absolute_url(self):  # формирование маршрута с идентификатором
        return reverse('category', kwargs={'cat_id': self.pk})


class Products(models.Model):  # БД Товары
    name = models.CharField(max_length=255, verbose_name='Наименование')  # название товара
    category = models.ForeignKey('Сategories', on_delete=models.PROTECT, verbose_name='Категория')  # категория товара (запрещено удаление)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='URL')  # url-адрес
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')  # стоимость
    description = models.TextField(blank=True, verbose_name='Описание')  # описание товара
    rating = models.FloatField(null=True, verbose_name='Рейтинг')  # рейтинг товара по отзывам
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    count = models.PositiveIntegerField(verbose_name='Количество')  # количество товара на складе (в наличии)
    seller = models.ForeignKey('Sellers', on_delete=models.CASCADE, verbose_name='Продавец')  # продавец этого товара
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')  # время создания товара
    time_update = models.DateTimeField(auto_now=True)  # время внесения изменений в товар

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name', 'category']  # сортировка по полям

    def __str__(self):  # отображение заголовков записи модели
        return self.name

    def get_absolute_url(self):  # формирование маршрута с идентификатором
        return reverse('product', kwargs={'prod_slug': self.slug})


class Comment(models.Model):  # БД коментариев к товарам
    # ссылка на название товара
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    text = models.TextField()  # отзыв о товаре
    rating = models.IntegerField(null=False, default=1)  # оценка товара

    class Meta:
        constraints = [models.CheckConstraint(
            name="%(app_label)s_%(class)s_rating_range",
            check=models.Q(rating__range=(1, 5)),
            )
        ]


class ProductImages(models.Model):  # БД изображений товаров
    # ссылка на название товара
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)


class Sellers(models.Model):  # БД продавцов
    login = models.CharField(max_length=150, unique=True)  # логин
    password = models.CharField(max_length=128)  # пароль
    f_name = models.CharField(max_length=150)  # имя
    l_name = models.CharField(max_length=150, blank=True)  # фамилия
    email = models.EmailField()  # электронная почта
    num_phone = models.PositiveSmallIntegerField(default=0, blank=True)   # телефонный номер

    def __str__(self):
        return self.login


class Customers(models.Model):  # БД покупателей
    login = models.CharField(max_length=150, unique=True)  # логин
    password = models.CharField(max_length=128)  # пароль
    f_name = models.CharField(max_length=150)  # имя
    l_name = models.CharField(max_length=150, null=True, blank=True)  # фамилия
    email = models.EmailField()  # электронная почта
    num_phone = models.PositiveSmallIntegerField(null=True, blank=True)   # телефонный номер

