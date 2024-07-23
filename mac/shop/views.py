from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact, Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
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
    if request.method == "POST":
        name = request.POST.get('name' , '')
        email = request.POST.get('email' , '')
        phone = request.POST.get('phone' , '')
        desc = request.POST.get('desc' , '')
        print(name , email , phone ,desc)
        contact = Contact(name =name , email = email , phone = phone , desc = desc)
        contact.save()
    return render(request , 'shop/contact.html' )

def tracker(request):
    return render(request , 'shop/tracker.html' )

def search(request):
    return render(request , 'shop/search.html' )


def productview(request , myid):
    # fatch Product Using ID
    product = Product.objects.filter(id = myid)
    print(product)
    return render(request , 'shop/prodview.html' , {'product': product[0]} )



def checkout(request):
    return HttpResponse("This is checkout")