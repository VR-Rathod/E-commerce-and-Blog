from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    n =len(products)
    nSlides = n//4 + ceil((n/4)- (n//4))
    # params = {'no_of_slides': nSlides , 'range': range(1 , nSlides) , 'product': products}
    allProdes = [[products , range(1 , len(products)), nSlides] , 
                 [products , range(1 , len(products)), nSlides]
                 ]
    params = {'allProds': allProdes}
    return render(request , 'shop/index.html' , params)

def about(request):
    return render(request , 'shop/about.html')

def contact(request):
    return HttpResponse("This is contact")

def tracker(request):
    return HttpResponse("This is tracker")

def search(request):
    return HttpResponse("This is search")

def productview(request):
    return HttpResponse("This is productview")

def checkout(request):
    return HttpResponse("This is checkout")