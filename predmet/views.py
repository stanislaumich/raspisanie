from django.shortcuts import render
from .models import Predmet
from django.http import HttpResponse


def index(request):
    p = Predmet.objects.order_by("name")
    return render(request, "predmet/predmet.html", context={"p": p})


def detail(request, id):
    t = id
    p = Predmet.objects.get(id=t)
    return render(request, "predmet/detail.html", context={"p": p})
