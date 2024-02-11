from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    return render(request, 'home.html', {'home':home})

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')