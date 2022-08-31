from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addprod/', addprod, name='add_product'),
    path('login/', login, name='login'),
    path('cart/', cart, name='cart'),
    path('product/<slug:prod_slug>/', show_prod, name='product'),
    path('category/<int:cat_id>/', show_category, name='category'),
]

