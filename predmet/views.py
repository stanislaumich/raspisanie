from django.shortcuts import render

from .apps import PredmetConfig
from .models import Predmet
from django.http import HttpResponse


def index(request):
    p = Predmet.objects.order_by("name")
    tit = PredmetConfig.verbose_name
    return render(request, "predmet/predmet.html", context={"p": p, "tit": tit})


def detail(request, id):
    t = id
    p = Predmet.objects.get(id=t)
    tit = PredmetConfig.verbose_name
    return render(request, "predmet/detail.html", context={"p": p, "tit": tit})
