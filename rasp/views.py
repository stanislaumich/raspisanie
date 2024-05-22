from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Aud, Para
from .models import Grp
from .models import Person
from .models import Predmet, Rasp
from datetime import timedelta, datetime, date
from .forms import EditRasp
from django.views.generic import DetailView, UpdateView
import locale

locale.setlocale(locale.LC_ALL, "")

def page_not_found_view(request, exception):
    return render(request, 'rasp/404.html', status=404)

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
    paginator = Paginator(r, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "rasp/indexRasp.html", context={"r": r,"page_obj": page_obj})


def detailRasp(request, id):
    t = id
    r = Rasp.objects.get(id=t)
    return render(request, "rasp/detailRasp.html", context={"r": r})


def detailRaspPers(request, id, wd):
    t = id

    r = Rasp.objects.filter(idpers=t, dt__week=wd).order_by("dt", "idpara_id")
    if not r:
        r = Person.objects.get(id=t)
        cntx = {"r": r, "wdn": wd + 1, "wdp": wd - 1, "idp":id, "fio":r.fio}
        return render(request, 'rasp/404pers.html', cntx)
    dtb = r.first().dt
    cntx = {"r": r, "wdn": wd + 1, "wdp": wd - 1, "i": t,
            "dt1": 'Понедельник,  ' + (dtb + timedelta(-1 * dtb.weekday() + 0)).strftime("%B %d "),
            "dt2": 'Вторник,  ' + (dtb + timedelta(-1 * dtb.weekday() + 1)).strftime("%B %d "),
            "dt3": 'Среда,  ' + (dtb + timedelta(-1 * dtb.weekday() + 2)).strftime("%B %d "),
            "dt4": 'Четверг,  ' + (dtb + timedelta(-1 * dtb.weekday() + 3)).strftime("%B %d "),
            "dt5": 'Пятница,  ' + (dtb + timedelta(-1 * dtb.weekday() + 4)).strftime("%B %d "),
            "dt6": 'Суббота,  ' + (dtb + timedelta(-1 * dtb.weekday() + 5)).strftime("%B %d "),
            "r1": r[:7], "r2": r[7:14], "r3": r[14:21],
            "r4": r[21:28], "r5": r[28:35], "r6": r[35:42],
            "fio": r[0].idpers.fio, "idp": r[0].idpers.id,
            "light1":'text-light' if (dtb + timedelta(-1 * dtb.weekday() + 0)).strftime("%B %d ")==datetime.today().strftime("%B %d ") else '',
            "light2":'text-light' if (dtb + timedelta(-1 * dtb.weekday() + 0)).strftime("%B %d ")==datetime.today().strftime("%B %d ") else '',
            "light3":'text-light' if (dtb + timedelta(-1 * dtb.weekday() + 2)).strftime("%B %d ")==datetime.today().strftime("%B %d ") else '',
            "light4":'text-light' if (dtb + timedelta(-1 * dtb.weekday() + 3)).strftime("%B %d ")==datetime.today().strftime("%B %d ") else '',
            "light5":'text-light' if (dtb + timedelta(-1 * dtb.weekday() + 4)).strftime("%B %d ")==datetime.today().strftime("%B %d ") else '',
            "light6":'text-light' if (dtb + timedelta(-1 * dtb.weekday() + 5)).strftime("%B %d ")==datetime.today().strftime("%B %d ") else '',
            "bg1": 'bg-primary' if (dtb + timedelta(-1 * dtb.weekday() + 0)).strftime("%B %d ")==datetime.today().strftime("%B %d ") else '',
            "bg2": 'bg-primary' if (dtb + timedelta(-1 * dtb.weekday() + 1)).strftime("%B %d ")==datetime.today().strftime("%B %d ") else '',
            "bg3": 'bg-primary' if (dtb + timedelta(-1 * dtb.weekday() + 2)).strftime("%B %d ")==datetime.today().strftime("%B %d ") else '',
            "bg4": 'bg-primary' if (dtb + timedelta(-1 * dtb.weekday() + 3)).strftime("%B %d ")==datetime.today().strftime("%B %d ") else '',
            "bg5": 'bg-primary' if (dtb + timedelta(-1 * dtb.weekday() + 4)).strftime("%B %d ")==datetime.today().strftime("%B %d ") else '',
            "bg6": 'bg-primary' if (dtb + timedelta(-1 * dtb.weekday() + 5)).strftime("%B %d ")==datetime.today().strftime("%B %d ") else '',
            }
    return render(request, "rasp/detailRaspPers.html",
                  context=cntx)


def editRaspPers(request, id):
    res = ""
    r = Rasp.objects.get(id=id)
    form = EditRasp(request.POST)
    wd = wd = r.dt.isocalendar()[1]
    dt = r.dt
    idpara = r.idpara
    if request.method == "POST":
        form = EditRasp(request.POST)
        if form.is_valid():
            r.id = id
            r.name = form.cleaned_data["name"]
            r.idgrp = form.cleaned_data["idgrp"]
            r.idpers = form.cleaned_data["idpers"]
            r.idaud = form.cleaned_data["idaud"]
            r.idpredmet = form.cleaned_data["idpredmet"]
            r.save()
            res = "cохранено"
            return HttpResponseRedirect("/rasp/rasp/"+str(r.idpers.id))
            #return render(request, "rasp/editRasp.html",
            #       {'form': form, "res":res, "dt":dt, "idpara":idpara})
    else:
        form = EditRasp(instance=r)
        dt = r.dt
        idpara = r.idpara
    return render(request, "rasp/editRasp.html",{'form': form, "res":res, "dt":dt, "idpara":idpara})

def genRaspPers(request):
    dt = datetime.today()
    dte = dt + timedelta(200)
    while dt < dte:
        print(dt)
        for i in range(7):
            r = Rasp()
            r.dt = dt
            r.name = 'AUTO'
            r.idgrp = Grp.objects.get(id=2)
            r.idpers = Person.objects.get(id=1)
            r.idaud = Aud.objects.get(id=3)
            r.idpredmet = Predmet.objects.get(id=4)
            r.idpara = Para.objects.get(id=i+1)
            r.save()
        dt = dt+timedelta(1)
    return render(request, "rasp/detailRasp.html", context={"r": 1})

def delRaspPers(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")