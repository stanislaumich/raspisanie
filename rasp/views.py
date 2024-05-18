from django.shortcuts import render
from .models import Aud
from .models import Grp
from .models import Person
from .models import Predmet, Rasp
from datetime import timedelta, datetime, date
import locale

locale.setlocale(locale.LC_ALL, "")


def indexPredmet(request):
    p = Predmet.objects.order_by("name")
    return render(request, "rasp/indexPredmet.html", context={"p": p})


def detailPredmet(request, id):
    t = id
    p = Predmet.objects.get(id=t)
    return render(request, "rasp/detailPredmet.html", context={"p": p})


def indexPerson(request):
    people = Person.objects.order_by("fio")
    wd = datetime.today().isocalendar()[1]
    return render(request, "rasp/indexPerson.html", context={"people": people, "wd": wd})


def detailPerson(request, id):
    t = id
    people = Person.objects.get(id=t)
    return render(request, "rasp/detailPerson.html", context={"p": people})


def indexAud(request):
    a = Aud.objects.order_by("name")
    return render(request, "rasp/indexAud.html", context={"aud": a})


def detailAud(request, id):
    t = id
    a = Aud.objects.get(id=t)
    return render(request, "rasp/detailAud.html", context={"a": a})


def indexGrp(request):
    g = Grp.objects.order_by("num")
    return render(request, "rasp/indexGrp.html", context={"g": g})


def detailGrp(request, id):
    t = id
    g = Grp.objects.get(id=t)
    return render(request, "rasp/detailGrp.html", context={"g": g})


def indexRasp(request):
    r = Rasp.objects.order_by("id")
    return render(request, "rasp/indexRasp.html", context={"r": r})


def detailRasp(request, id):
    t = id
    r = Rasp.objects.get(id=t)
    return render(request, "rasp/detailRasp.html", context={"r": r})


def detailRaspPers(request, id, wd):
    t = id
    # datetime.today().isocalendar()[1]
    r = Rasp.objects.filter(idpers=t, dt__week=wd)
    return render(request, "rasp/detailRaspPers.html", context={"r": r, "wdn": wd+1,"wdp": wd-1, "i":t})
