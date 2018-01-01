# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_app.models import User
from .models import Product
# Route to index --> /wish
def index(request):
    context={
        'cur_user': User.objects.get(id=request.session['id']),
        'other_users': User.objects.filter(id=request.session['id']),
        'products': Product.objects.exclude(items__id=request.session['id']),
        'user_wishlist': Product.objects.filter(items__id=request.session['id']),
}
    return render(request,'wish_app/index.html', context)
# Route to add a product --> /wish/add
def add(request):
    return render(request,'wish_app/add.html',{'cur_user': User.objects.get(id=request.session['id'])})
# Route to create a product --> /wish/create
def create(request):
    user = User.objects.get(id=request.session['id'])
    product = Product.objects.create(name=request.POST['product'])
    user.products.add(product)
    return redirect('/wish')
#Route to show a product --> /wish/show/{{ product.id }}
def show(request,id):
    return render(request,'wish_app/product.html', {'productInfo': Product.objects.get(id=id)})
# Route to add a product to user wishlist --> /wish/addProduct/{{ product.id }}
def addProduct(request,id):
    product = Product.objects.get(id=id)
    user = User.objects.get(id=request.session['id'])
    user.products.add(product)
    return redirect('/wish')
# Route to remove item from user wishlist --> /wish/remove/{{ product.id }}
def remove(request,id):
    product = Product.objects.get(id=id)
    user = User.objects.get(id=request.session['id'])
    user.products.remove(product)
    return redirect('/wish')
# Route to user page --> /wish/userPage
def userPage(request):
    return render(request,'wish_app/user.html', {'allProducts': Product.objects.all()})
# Route to destroy product --> /wish/delete/{{ product.id }}
def delete(request,id):
    Product.objects.get(id=id).delete()
    return redirect('/wish')

def api(request):
    return render(request,'wish_app/apiPrac.html')




###





# Route
