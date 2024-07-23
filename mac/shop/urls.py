from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name="shopHome"),
    path('about/', views.about , name="AboutUs"),
    path('contact/', views.contact , name="ContactUs"),
    path('tracker/', views.tracker , name="Trackeingstatus"),
    path('search/', views.search , name="Search"),
    path('products/<int:myid>', views.productview , name="Search"),
    path('checkout/', views.checkout , name="Checkout"),
]
