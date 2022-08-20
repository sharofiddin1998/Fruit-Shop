from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from fruits.models import *
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
def BASE(request):
    return render(request, 'main/base.html')

def HOME(request):
    categories=Categories.objects.all()
    tag=Tag.objects.all()
    product=Product.objects.all()
    context={
        'categories':categories,
        'product':product,
        'tag':tag,
    }
    return render(request, 'main/home.html',context)

def LOGIN(request): 
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Email and Password are Invalid')
            return redirect('login')
    

    return render(request, 'registration/login.html')
def LOGOUT(request):
    logout(request)
    return redirect('login')

def REGISTER(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        customer=User.objects.create_user(username,email,pass1)
        customer.first_name=first_name
        customer.last_name=last_name
        customer.save()
        return redirect('home')
    return render(request, 'registration/registration.html')

def BLOG(request):
    product=Product.objects.all()
    categories=Categories.objects.all()
    tag=Tag.objects.all()
    filter_price=Filter_Price.objects.all()
    categoryID=request.GET.get('categories')
    FILTER_PRICE_ID=request.GET.get('filter_price')
    # create_dateID=request.GET.get('create_date')
    if categoryID:
        product=Product.objects.filter(categories=categoryID)
    elif FILTER_PRICE_ID:
        product=Product.objects.filter(filter_price=FILTER_PRICE_ID)
    # elif create_dateID:
    #     product=Product.objects.filter(status='Publish').order_by('id')
    context={
    'product':product,
    'categories':categories,
    'filter_price':filter_price,
    'tag':tag,
    }
    return render(request, 'main/blog.html',context)

def BLOG_DETAILS(request,id):
    prod=Product.objects.filter(id=id).first()
    categories=Categories.objects.all()
    context={
    'prod':prod,
    'categories':categories,
    }
    return render(request, 'main/blog_details.html',context)

def SHOP(request):
    product=Product.objects.all()
    categories=Categories.objects.all()
    context={
        'product':product,
        'categories':categories,
    }
    return render(request, 'main/shop.html',context)

# def SHOP_DETAILS(request):
#     prod=Product.objects.filter(id=id).first()
#     categories=Categories.objects.all()
#     context={
#         'prod':prod,
#         'categories':categories,
#     }
#     return render(request, 'main/shop_details.html',context)

# # Cart

@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_detail(request):
    return render(request, 'Cart/cart_details.html')

def Check_out(request):
    return render(request,'Cart/checkout.html')