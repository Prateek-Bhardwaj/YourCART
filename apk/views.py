from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import logout
from django.contrib import messages
from .models import Product, Picture,Review, Booking, Category


# Create your views here.
def home(request):
    return render(request, 'temp/home.html')

class Index(View):
    def post(self, request):
        pass

    def get(self,request):
        products = Product.objects.all().order_by('-id')
        name = request.user
        context = {'products':products}
        return render(request, 'temp/index.html', context)


def log_in(request):
    return render(request, 'login.html')

def log_out(request):
    logout(request)
    messages.success(request, 'You are logged out. Please login to have a better experience.')
    return redirect('home')

def view(request, id=None):
    cart = request.session.get('cart')
    products = Product.objects.filter(id=id)
    product = Product.objects.get(id=id)
    rev = product.review_set.all().order_by('-date')
    orders = product.picture_set.all()
    context = {'products':products, 'orders':orders,'rev':rev}
    return render(request, 'temp/view.html', context)


def review(request):
    if request.method == 'POST':
        prodct = request.POST.get('product')
        prod = Product.objects.get(id=prodct)
        if prod is None:
            return redirect('home')
        product = prod
        customer = request.user
        content = request.POST.get('content')
        revu = Review(product=product, customer=customer, content=content)
        revu.save()
        messages.success(request, 'Thankyou for your valuable review.')
        return redirect(f'/view/{prod.id}')
    return render(request, 'view.html')

class Cart(View):
    def post(self, request):
        product = request.POST.get('product')
        prod = Product.objects.get(id=product)
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:    
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('cart :' , request.session['cart'])
        messages.success(request, 'Your cart has been edited.')
        return redirect(f'/view/{prod.id}')


    def get(self, request):
        cart = request.session.get('cart')
        if cart is not None:
            ids = list(cart.keys())
            product = Product.get_product_by_Id(ids)
        else:
            product = {}
            return redirect('home')
        print(product)
        context = {'product':product}
        return render(request, 'temp/cart.html', context)

class CartItem(View):
    def post(self, request):
        product = request.POST.get('product')
        prod = Product.objects.get(id=product)
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:    
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('cart :' , request.session['cart'])
        return redirect('cart')

def place(request):
    return render(request, "temp/place.html")

class Order(View):
    def post(self, request):
        address =  request.POST.get('address')
        phone = request.POST.get('phone')
        customer  = request.user
        cart = request.session.get('cart')
        products = Product.get_product_by_Id(list(cart.keys()))
        for product in products:
            order = Booking(customer=customer, product=product, price=product.price, image=product.image, address=address, phone=phone, quantity=int(cart.get(str(product.id))))
            order.save()
        request.session['cart'] = {}
        messages.success(request, 'Order placed successfully. Thanks for choosing')
        return redirect('home')

def book(request):
    if request.method == 'POST':
        prod = request.POST.get('product')
        product = Product.objects.get(id=prod)
        address = request.POST.get('address')
        phone= request.POST.get('phone')
        customer = request.user
        order = Booking(customer=customer, product=product, price=product.price, image=product.image, address=address, phone=phone)
        order.save()
        messages.success(request, 'Order placed successfully. Thanks for choosing')
        return redirect(f'/view/{product.id}')


def profile(request):
    name = request.user
    orders = Booking.objects.filter(customer=name)
    context  = {'orders':orders}
    return render(request, 'temp/profile.html', context)