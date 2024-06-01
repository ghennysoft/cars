from django import forms
from .models import Category, SubCategory, Brand, Product, ProductImage


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image']


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['category', 'name']


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'image']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['subcategory', 'name', 'image', 'description', 'price', 'old_price']


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']
        