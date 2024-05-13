from django.shortcuts import render
#from .models import Person
from django.http import HttpResponse
def index(request):
    data = {"header": "Hello Django", "message": "Welcome to Python"}
    return render(request, "index.html", context=data)


def about(request):
    data = {"header": "Hello Django", "message": "About"}
    return render(request, "about.html", context=data)


def contact(request):
    data = {"header": "Hello Django", "message": "Contact"}
    return render(request, "contact.html", context=data)

