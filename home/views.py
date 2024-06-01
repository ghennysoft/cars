from django.shortcuts import render, redirect, get_object_or_404
from back.models import Category, Brand, Product, CartOrder, CartOrderItems
from other.models import SocieteAviation, TrajetVoyage
from django.db.models import Q
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse


def Home(request):
    template_name = 'home/index.html'
    brands = Brand.objects.all().order_by('id')
    products = Product.objects.all().order_by('id')
    voyages = SocieteAviation.objects.all().order_by('id')
    context = {
        'brands': brands,
        'products': products,
        'voyages': voyages,
    }
    return render(request, template_name, context)


def shop(request):
    template_name = 'home/shop.html'
    products = Product.objects.all().order_by('-id')
    context = {
        'products': products,
    }
    return render(request, template_name, context)


def detail_product(request, prod_id):
    template_name = 'home/detail-product.html'
    product = get_object_or_404(Product, prod_id=prod_id)
    context = {
        'product': product,
    }
    return render(request, template_name, context)


def product_category(request, slug):
    template_name = 'home/product_category.html'
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(subcategory__category=category)
    context = {
        'category': category,
        'products': products,
    }
    return render(request, template_name, context)


def search(request):
    template_name = 'home/search.html'
    query = request.GET.get('q')
    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    context = {
        'query': query,
        'products': products,
    }
    return render(request, template_name, context)


# Add to cart
def add_to_cart(request):
    cart_product = {}
    cart_product[str(request.GET['id'])] = {
        'pid': request.GET['pid'],
        'name': request.GET['name'],
        'qty': request.GET['qty'],
        'price': request.GET['price'],
        'image': request.GET['image'],
    }
    if 'cart_data_obj' in request.session:
        if str(request.GET['id']) in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['qty'] = int(cart_product[str(request.GET['id'])]['qty'])
            cart_data.update(cart_data)
            request.session['cart_data_obj'] = cart_data
        else:
            cart_data = request.session['cart_data_obj']
            cart_data.update(cart_product)
            request.session['cart_data_obj'] = cart_data
    else:
        request.session['cart_data_obj'] = cart_product
    return JsonResponse({'data': request.session['cart_data_obj'], 'total_cart_items': len(request.session['cart_data_obj'])})



@login_required
def cart_list(request):
    template_name = 'home/cart.html'
    total_amt = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            total_amt += int(item['qty'])*float(item['price'])
        return render(request, template_name, {'cart_data': request.session['cart_data_obj'], 'total_cart_items': len(request.session['cart_data_obj']), 'total_amt': total_amt})
    return render(request, template_name, {'total_amt': int(total_amt)})

@login_required
def checkout(request):
    template_name = 'home/checkout.html'
    
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    phone = request.POST.get('phone')
    city = request.POST.get('city')
    adress = request.POST.get('adress')

    cart_total_amt = 0
    total_amt = 0

    if 'cart_data_obj' in request.session:

        if request.method=='POST':

            # Save order infos
            for p_id, item in request.session['cart_data_obj'].items():
                total_amt += int(item['qty'])*float(item['price'])
            
            order = CartOrder.objects.create(
                user = request.user,
                total = total_amt,
                first_name = first_name,
                last_name = last_name,
                phone = phone,
                city = city,
                adresse = adress,
            )

            # Save order items infos
            for p_id, item in request.session['cart_data_obj'].items():
                cart_total_amt += int(item['qty'])*float(item['price'])

                cart_order_products = CartOrderItems.objects.create(
                    order = order,
                    invoice_no = 'INVOICE_NO-' + str(order.id),
                    item = item['name'],
                    image = item['image'],
                    quantity = item['qty'],
                    price = item['price'],
                    total = float(item['qty'])*float(item['price']),
                )

            # Delete session
            del request.session['cart_data_obj']
                
            return redirect('home:command_success')
        

        for p_id, item in request.session['cart_data_obj'].items():
            total_amt += int(item['qty'])*float(item['price'])

        return render(request, template_name, {'cart_data': request.session['cart_data_obj'], 'total_cart_items': len(request.session['cart_data_obj']), 'total_amt': total_amt})

def command_success(request):
    template_name = 'home/command_success.html'
    return render(request, template_name)

def command_failed(request):
    template_name = 'home/command_failed.html'
    return render(request, template_name)
