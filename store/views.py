from django.shortcuts import render,redirect
from .models import *
# Create your views here.


def store(request):
    products = Product.objects.all()
    quantity = 0
    if request.user.is_authenticated:
        items = Order_item.objects.filter(customer=request.user)

        for i in items:
            quantity += i.quantity
    context = {'products': products,'quantity':quantity}
    return render(request, 'store.html', context)


def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        item, created = Order_item.objects.get_or_create(product=product, customer=request.user)
        item.quantity += 1
        item.save()
        items = Order_item.objects.filter(customer=request.user)
        return redirect('store')
    else:
        return redirect('login')


def add(request, product_id):
    product = Product.objects.get(id=product_id)
    item, created = Order_item.objects.get_or_create(product=product,customer=request.user)
    item.quantity += 1
    item.save()
    items = Order_item.objects.filter(customer=request.user)
    return redirect('cart')

def remove(request, product_id):
    product = Product.objects.get(id=product_id)
    item = Order_item.objects.get(product=product, customer=request.user)
    if item.quantity > 1:
        item.quantity -=1
        item.save()
    elif item.quantity == 1:
        item.delete()
    return redirect('cart')
def cart(request):

    if request.user.is_authenticated:
        items = Order_item.objects.filter(customer=request.user)

        quantity = 0
        price = 0
        item_total = 0
        for item in items:
            price += item.product.price * item.quantity
            quantity += item.quantity

        context = {'items': items, 'quantity': quantity,'price': price}
        return render(request, 'cart.html', context)
    else:
        return redirect('login')


def checkout(request):

    if request.user.is_authenticated:
        items = Order_item.objects.filter(customer=request.user)

        quantity = 0
        price = 0
        item_total = 0
        for item in items:
            price += item.product.price * item.quantity
            quantity += item.quantity

        context = {'items': items, 'quantity': quantity, 'price': price}
        return render(request, 'checkout.html', context)
    else:
        return redirect('login')
