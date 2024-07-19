from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request , 'shop/index.html')

def about(request):
    return HttpResponse("This is about")

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