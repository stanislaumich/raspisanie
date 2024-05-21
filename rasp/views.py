from django.shortcuts import render
from .models import Aud, Para
from .models import Grp
from .models import Person
from .models import Predmet, Rasp
from datetime import timedelta, datetime, date
from .forms import EditRasp
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
    r = Rasp.objects.filter(idpers=t, dt__week=wd).order_by("dt", "idpara_id")
    # grp = Grp.objects.get(id=2)
    # pers = Person.objects.get(id=1)
    # aud = Aud.objects.get(id=3)
    # pred = Predmet.objects.get(id=4)
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
            }
    return render(request, "rasp/detailRaspPers.html",
                  context=cntx)


def editRaspPers(request, id):
    res = ""
    #form = EditRasp(request)
    #r = Rasp.objects.get(id=id)
    if request.method == "POST":
        #form = EditRasp(request.POST)
        if form.is_valid():
            # r.name = form.cleaned_data["name"]
            # r.dt = form.cleaned_data["dt"]
            # r.idgrp = form.cleaned_data["idgrp"]
            # r.idpers = form.cleaned_data["idpers"]
            # r.idpara = form.cleaned_data["idpara"]
            # r.idaud = form.cleaned_data["idaud"]
            # r.idpredmet = form.cleaned_data["idpredmet"]
            form.save()
            res = "Сохранено"
        return render(request, "rasp/editRasp.html",
                  {'form': form, "res":res})
    else:
        r = Rasp.objects.get(id=id)
        form = EditRasp(instance=r)
        return render(request, "rasp/editRasp.html",
                      {'form': form, "res":res})

def delRaspPers(request, id):
    pass

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

# def delete(request, id):
#     try:
#         person = Person.objects.get(id=id)
#         person.delete()
#         return HttpResponseRedirect("/")
#     except Person.DoesNotExist:
#         return HttpResponseNotFound("<h2>Person not found</h2>")