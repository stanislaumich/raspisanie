from django.shortcuts import render
from .models import Grp
from django.http import HttpResponse


def index(request):
    g = Grp.objects.order_by("num")
    return render(request, "grp/grp.html", context={"g": g})


def detail(request, id):
    t = id
    g = Grp.objects.get(id=t)
    return render(request, "grp/detail.html", context={"g": g})
