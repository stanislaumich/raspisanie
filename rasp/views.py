from django.shortcuts import render
from .models import Aud
from .models import Grp
from .models import Person
from .models import Predmet

def indexPredmet(request):
    p = Predmet.objects.order_by("name")
    tit = "PredmetConfig.verbose_name"
    return render(request, "rasp/indexPredmet.html", context={"p": p, "tit": tit})

def detailPredmet(request, id):
    t = id
    p = Predmet.objects.get(id=t)
    tit = "PredmetConfig.verbose_name"
    return render(request, "rasp/detailPredmet.html", context={"p": p, "tit": tit})
def indexPerson(request):
    people = Person.objects.order_by("fio")
    return render(request, "rasp/indexPerson.html", context={"people": people})

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
