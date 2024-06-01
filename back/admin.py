from django.contrib import admin
from .models import Category, SubCategory, Brand, Product, ProductImage, CartOrder, CartOrderItems


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(CartOrder)
admin.site.register(CartOrderItems)
