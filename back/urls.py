from django.urls import path
from .views import *

app_name = 'back'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),

    # Products
    path('products/', ProductsList.as_view(), name='products'),
    path('product/add/', AddProduct.as_view(), name='add-product'),
    path('product/<int:pk>/update/', UpdateProduct.as_view(), name='update-product'),
    path('product/<int:pk>/delete/', DeleteProduct, name='delete-product'),

    # Category
    path('categories/', CategoryList.as_view(), name='categories'),
    path('category/add/', AddCategory.as_view(), name='add-category'),
    path('category/<str:slug>/update/', UpdateCategory.as_view(), name='update-category'),
    path('category/<str:slug>/delete/', DeleteCategory, name='delete-category'),

    # SubCategory
    path('sub-categories/', SubCategoryList.as_view(), name='sub-categories'),
    path('sub-category/add/', AddSubCategory.as_view(), name='add-sub-category'),
    path('sub-category/<str:slug>/update/', UpdateSubCategory.as_view(), name='update-sub-category'),
    path('sub-category/<str:slug>/delete/', DeleteSubCategory, name='delete-sub-category'),
]
