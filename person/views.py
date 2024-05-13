from django.shortcuts import render
from .models import Person
from django.http import HttpResponse


def index(request):
    people = Person.objects.order_by("fio")
    return render(request, "person.html", context={"people": people})


def person(request, id):
    t=id
    people = Person.objects.get(id=t)
    return render(request, "personone.html", context={"p": people})
