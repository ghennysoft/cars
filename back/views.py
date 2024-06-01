from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import *
from .models import Product, Category, SubCategory
from .forms import ProductForm, CategoryForm, SubCategoryForm
from django.contrib.auth import get_user_model

User = get_user_model()

class Dashboard(View, LoginRequiredMixin):
    template_name = 'back/dashboard.html'
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        context = {
            'products': products.count(),
        }
        return render(request, self.template_name, context)


########## Product Management ##########
class ProductsList(View, LoginRequiredMixin):
    template_name = 'back/products.html'
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        context = {
            'products': products,
        }
        return render(request, self.template_name, context)

class AddProduct(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    template_name = 'back/add-product.html'
    success_url = '/back/products'

class UpdateProduct(UpdateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    template_name = 'back/update-product.html'
    success_url = '/back/products'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["secteurs"] = Secteur.objects.all()
    #     return context

@login_required
def DeleteProduct(request, pk):
    template_name = 'back/delete-product.html'
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        product.delete()
        return HttpResponseRedirect('/back/products')
    context = {
        'product': product,
    }
    return render(request, template_name, context)


########## Category Management ##########
class CategoryList(View, LoginRequiredMixin):
    template_name = 'back/categories.html'
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        context = {
            'categories': categories,
        }
        return render(request, self.template_name, context)

class AddCategory(CreateView, LoginRequiredMixin):
    model = Category
    form_class = CategoryForm
    template_name = 'back/add-category.html'
    success_url = '/back/categories/'

class UpdateCategory(UpdateView, LoginRequiredMixin):
    model = Category
    form_class = CategoryForm
    template_name = 'back/update-category.html'
    success_url = '/back/categories/'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["secteurs"] = Secteur.objects.all()
    #     return context

@login_required
def DeleteCategory(request, slug):
    template_name = 'back/delete-category.html'
    category = Category.objects.get(slug=slug)
    if request.method == "POST":
        category.delete()
        return HttpResponseRedirect('/back/categories')
    context = {
        'category': category,
    }
    return render(request, template_name, context)


########## SubCategory Management ##########
class SubCategoryList(View, LoginRequiredMixin):
    template_name = 'back/subcategories.html'
    def get(self, request, *args, **kwargs):
        subcategories = SubCategory.objects.all()
        context = {
            'subcategories': subcategories,
        }
        return render(request, self.template_name, context)

class AddSubCategory(CreateView, LoginRequiredMixin):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'back/add-subcategory.html'
    success_url = '/back/sub-categories/'

class UpdateSubCategory(UpdateView, LoginRequiredMixin):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'back/update-subcategory.html'
    success_url = '/back/sub-categories/'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["secteurs"] = Secteur.objects.all()
    #     return context

@login_required
def DeleteSubCategory(request, slug):
    template_name = 'back/delete-subcategory.html'
    subcategory = SubCategory.objects.get(slug=slug)
    if request.method == "POST":
        subcategory.delete()
        return HttpResponseRedirect('/back/sub-categories')
    context = {
        'subcategory': subcategory,
    }
    return render(request, template_name, context)
