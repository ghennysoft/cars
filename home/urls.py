from django.urls import path
from .views import Home, shop, product_category, detail_product, search, cart_list, add_to_cart, checkout, command_success, command_failed

app_name='home'

urlpatterns = [
    path('', Home, name='home'),
    path('shop/', shop, name='shop'),
    path('<str:slug>/products/', product_category, name='product_category'),
    path('product/<str:prod_id>', detail_product, name='detail-product'),
    path('search/', search, name='search'),
    path('cart/', cart_list, name='cart'),
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    path('checkout/', checkout, name='checkout'),
    path('command_success/', command_success, name='command_success'),
    path('command_failed/', command_failed, name='command_failed'),
]
