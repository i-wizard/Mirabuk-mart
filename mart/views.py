from django.shortcuts import render
from .models import products

# Create your views here.
from django.http import HttpResponse

# Create your views here.
def index(request): #when you request the home page the urls.py will allow views to call the index function which accepts request as an arguement, and the home function returns the hello world as an httpresponse
    #you will use render the requested file because the function is now returning a dynamic page not just a text
    prods=products.objects.all()

    return render(request, "home.html", {"prods":prods})