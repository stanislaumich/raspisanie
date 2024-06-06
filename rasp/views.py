import time

from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Aud, Para
from .models import Grp
from .models import Person, MyPers
from .models import Predmet, Rasp
from datetime import timedelta, datetime, date
from django.views.generic import DetailView, UpdateView
import locale

locale.setlocale(locale.LC_ALL, "")

def getuser(request):
    return request.session.get('userid', 0)


def datefromiso(year, week, day):
    return datetime.strptime("%d%02d%d" % (year, week, day), "%Y%W%w")

def page_not_found_view(request, exception):
    return render(request, 'rasp/404.html', status=404)





def indexRasp(request):
    r = Rasp.objects.order_by("id")
    paginator = Paginator(r, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "rasp/indexRasp.html", context={"r": r, "page_obj": page_obj})


def detailRasp(request, id):
    t = id
    r = Rasp.objects.get(id=t)
    return render(request, "rasp/detailRasp.html", context={"r": r})



def delRaspPers(request, id):
    try:
        r = Rasp.objects.get(id=id)
        r.delete()
        messages.info(request, 'Запись расписания удалена')
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")




def genRaspPers(request):
    dt = datetime.today() + timedelta(-10)
    dte = dt + timedelta(200)
    while dt < dte:
        print(dt)
        for i in range(7):
            r = Rasp()
            r.dt = dt
            r.name = '---'
            r.idgrp = Grp.objects.get(id=0)
            r.idpers = Person.objects.get(id=1)
            r.idaud = Aud.objects.get(id=0)
            r.idpredmet = Predmet.objects.get(id=0)
            r.idpara = Para.objects.get(id=i + 1)
            r.save()
        dt = dt + timedelta(1)
    return render(request, "rasp/detailRasp.html", context={"r": 1})



def test(request):
    k = 0
    w = []
    dtb = datetime.today()
    dtb = dtb + timedelta(-1 * dtb.weekday() + 0)
    for i in range(6):
        for j in range(7):
            try:
                r = Rasp.objects.get(dt=dtb, idpara=j + 1, idpers=1)
                w.append({'v': 1, 'i': r})
            except:
                w.append({'v': 0, 'i': Para.objects.get(id=j + 1)})
            k = k + 1
            #print(w)
        dtb = dtb + timedelta(1)

    return render(request, "rasp/test.html", context={"r": w})






