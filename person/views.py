from django.shortcuts import render
from .models import Person
from django.http import HttpResponse


def index(request):
    people = Person.objects.order_by("fio")
    return render(request, "person/person.html", context={"people": people})


def detail(request, id):
    t = id
    people = Person.objects.get(id=t)
    return render(request, "person/detail.html", context={"p": people})
