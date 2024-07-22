from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    # print(products)
    # n =len(products)
    # nSlides = n//4 + ceil((n/4)- (n//4))
    # params = {'no_of_slides': nSlides , 'range': range(1 , nSlides) , 'product': products}
    # allProdes = [[products , range(1 , nSlides), nSlides] , 
    #              [products , range(1 , nSlides), nSlides]
    #              ]
    allProdes = []
    catpods = Product.objects.values('category' , 'id')
    cats = {item['category'] for item in catpods}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)- (n//4))
        allProdes.append([prod , range(1 , nSlides) , nSlides])
    
    params = {'allProds': allProdes}
    return render(request , 'shop/index.html' , params)

def about(request):
    return render(request , 'shop/about.html' )

def contact(request):
    return render(request , 'shop/contact.html' )

def tracker(request):
    return render(request , 'shop/tracker.html' )

def search(request):
    return render(request , 'shop/search.html' )


def productview(request):
    return render(request , 'shop/prodview.html' )



def checkout(request):
    return HttpResponse("This is checkout")