import time

from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Aud, Para, MyPers
from .models import Grp
from .models import Person
from .models import Predmet, Rasp
from datetime import timedelta, datetime, date
from .forms import EditRasp, Login
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
    week = request.session.get('week', datetime.today().isocalendar()[1])
    people = MyPers.objects.filter(myid=request.session.get('userid',1)).all()
    # print(people)
    # wd = datetime.today().isocalendar()[1]  request.session['week'] = 'mini'
    #wd = week
    # paginator = Paginator(people, 100)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    return render(request, "rasp/indexPerson.html", context={"people": people})  # ,  "page_obj": page_obj


def detailPerson(request, id):
    t = id
    people = Person.objects.get(id=t)
    return render(request, "rasp/detailPerson.html", context={"p": people})


def indexGrp(request):
    g = Grp.objects.order_by("num")
    wd = 22
    return render(request, "rasp/indexGrp.html", context={"g": g, "wd": wd})


def detailGrp(request, id):
    t = id
    g = Grp.objects.get(id=t)
    wd = 22
    return render(request, "rasp/detailGrp.html", context={"g": g, "wd": wd})


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


def datefromiso(year, week, day):
    return datetime.strptime("%d%02d%d" % (year, week, day), "%Y%W%w")


def detailRaspPers(request, id, wd):
    t = id
    g = Rasp.objects.filter(idpers=t, dt__week=wd).order_by("dt", "idpara_id")
    pr = Person.objects.get(id=t)
    k = 0
    w = []
    dtb = datefromiso(date.today().year, wd, 1).date()
    dtb = dtb + timedelta(-1 * dtb.weekday() + 0)
    for i in range(6):
        for j in range(7):
            try:
                r = Rasp.objects.get(dt=dtb, idpara=j + 1, idpers=t)
                w.append({'v': 1, 'i': r, "np": j})
            except:
                w.append({'v': 0, 'i': Para.objects.get(id=j + 1), "np": j + 1})
            k = k + 1
        dtb = dtb + timedelta(1)
    request.session['week'] = wd
    cntx = {"r": w, "wdn": wd + 1, "wdp": wd - 1, "i": t,
            "dt1": 'Понедельник,  ' + (dtb + timedelta(-1 * dtb.weekday() + 0)).strftime("%B %d "),
            "dt2": 'Вторник,  ' + (dtb + timedelta(-1 * dtb.weekday() + 1)).strftime("%B %d "),
            "dt3": 'Среда,  ' + (dtb + timedelta(-1 * dtb.weekday() + 2)).strftime("%B %d "),
            "dt4": 'Четверг,  ' + (dtb + timedelta(-1 * dtb.weekday() + 3)).strftime("%B %d "),
            "dt5": 'Пятница,  ' + (dtb + timedelta(-1 * dtb.weekday() + 4)).strftime("%B %d "),
            "dt6": 'Суббота,  ' + (dtb + timedelta(-1 * dtb.weekday() + 5)).strftime("%B %d "),
            "d1": (dtb + timedelta(-1 * dtb.weekday() + 0)).strftime("%Y-%m-%d"),
            "d2": (dtb + timedelta(-1 * dtb.weekday() + 1)).strftime("%Y-%m-%d"),
            "d3": (dtb + timedelta(-1 * dtb.weekday() + 2)).strftime("%Y-%m-%d"),
            "d4": (dtb + timedelta(-1 * dtb.weekday() + 3)).strftime("%Y-%m-%d"),
            "d5": (dtb + timedelta(-1 * dtb.weekday() + 4)).strftime("%Y-%m-%d"),
            "d6": (dtb + timedelta(-1 * dtb.weekday() + 5)).strftime("%Y-%m-%d"),
            "r1": w[:7], "r2": w[7:14], "r3": w[14:21],
            "r4": w[21:28], "r5": w[28:35], "r6": w[35:42],
            "fiop": pr.fio, "idp": t, "wd": wd,
            "light1": 'text-light' if (dtb + timedelta(-1 * dtb.weekday() + 0)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "light2": 'text-light' if (dtb + timedelta(-1 * dtb.weekday() + 0)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "light3": 'text-light' if (dtb + timedelta(-1 * dtb.weekday() + 2)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "light4": 'text-light' if (dtb + timedelta(-1 * dtb.weekday() + 3)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "light5": 'text-light' if (dtb + timedelta(-1 * dtb.weekday() + 4)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "light6": 'text-light' if (dtb + timedelta(-1 * dtb.weekday() + 5)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "bg1": 'bg-primary' if (dtb + timedelta(-1 * dtb.weekday() + 0)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "bg2": 'bg-primary' if (dtb + timedelta(-1 * dtb.weekday() + 1)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "bg3": 'bg-primary' if (dtb + timedelta(-1 * dtb.weekday() + 2)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "bg4": 'bg-primary' if (dtb + timedelta(-1 * dtb.weekday() + 3)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "bg5": 'bg-primary' if (dtb + timedelta(-1 * dtb.weekday() + 4)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "bg6": 'bg-primary' if (dtb + timedelta(-1 * dtb.weekday() + 5)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            }
    return render(request, "rasp/detailRaspPers.html",
                  context=cntx)



def addRaspPers(request, id):
    res = ""
    dt = datetime.strptime(request.GET.get("dt"), '%Y-%m-%d').date()
    wd = dt.isocalendar()[1]
    idpara = request.GET.get("np")
    if request.method == "POST":
        form = EditRasp(request.POST)
        if form.is_valid():
            form.paraid = Para.objects.get(id=idpara)
            # r.name = form.cleaned_data["name"]
            # r.idgrp = form.cleaned_data["idgrp"]
            # r.idpers = form.cleaned_data["idpers"]
            # r.idaud = form.cleaned_data["idaud"]
            # r.idpredmet = form.cleaned_data["idpredmet"]
            form.save()
            res = "cохранено"
            #return HttpResponseRedirect("{% url 'rspperson' form.idpers.id , wd %}")
            return HttpResponseRedirect("/rasp/rasp/person/" + str(id) + '/' + str(wd) + '/')
    else:
        r = Rasp()
        r.idpara = Para.objects.get(id=idpara)
        r.dt = dt
        form = EditRasp(instance=r)
    return render(request, "rasp/editRasp.html", {'form': form, "res": res, "dt": dt, "idpara": idpara})


def editRaspPers(request, id):
    res = ""
    r = Rasp.objects.get(id=id)
    form = EditRasp(request.POST)
    wd = r.dt.isocalendar()[1]
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
            return HttpResponseRedirect("/rasp/rasp/person/" + str(r.idpers.id) + '/' + str(wd) + '/')
    else:
        form = EditRasp(instance=r)
        dt = r.dt
        idpara = r.idpara
    return render(request, "rasp/editRasp.html", {'form': form, "res": res, "dt": dt, "idpara": idpara})


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


def delRaspPers(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


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


def detailRaspGroup(request, id, wd):
    t = id
    g = Rasp.objects.filter(idgrp=t, dt__week=wd).order_by("dt", "idpara_id")
    if not g:
        r = Grp.objects.get(id=t)
        #dtb + timedelta(-1 * dtb.weekday() + 0)
        #dt = (wd*7)/30 datetime.date(year=2020, month=1, day=4)
        d = date.today() + timedelta(7)
        d = d + timedelta(-1 * d.weekday())
        dt = d.strftime("%Y-%m-%d")  # datetime.strptime(d, '%Y-%m-%d').date()
        np = 1
        cntx = {"r": r, "wdn": wd + 1, "wdp": wd - 1, "idp": t, "name": r.name, "wd": wd, "np": 1, "dt": dt}
        return render(request, 'rasp/404group.html', cntx)
    k = 0
    w = []
    dtb = datefromiso(date.today().year, wd, 1).date()
    dtb = dtb + timedelta(-1 * dtb.weekday() + 0)
    for i in range(6):
        for j in range(7):
            try:
                r = Rasp.objects.get(dt=dtb, idpara=j + 1, idgrp=t)
                w.append({'v': 1, 'i': r, "np": j})
            except:
                w.append({'v': 0, 'i': Para.objects.get(id=j + 1), "np": j + 1})
            k = k + 1
            #print(w)
        dtb = dtb + timedelta(1)
    cntx = {"r": w, "wdn": wd + 1, "wdp": wd - 1, "i": t, "wd": wd,
            "dt1": 'Понедельник,  ' + (dtb + timedelta(-1 * dtb.weekday() + 0)).strftime("%B %d "),
            "dt2": 'Вторник,  ' + (dtb + timedelta(-1 * dtb.weekday() + 1)).strftime("%B %d "),
            "dt3": 'Среда,  ' + (dtb + timedelta(-1 * dtb.weekday() + 2)).strftime("%B %d "),
            "dt4": 'Четверг,  ' + (dtb + timedelta(-1 * dtb.weekday() + 3)).strftime("%B %d "),
            "dt5": 'Пятница,  ' + (dtb + timedelta(-1 * dtb.weekday() + 4)).strftime("%B %d "),
            "dt6": 'Суббота,  ' + (dtb + timedelta(-1 * dtb.weekday() + 5)).strftime("%B %d "),
            "d1": (dtb + timedelta(-1 * dtb.weekday() + 0)).strftime("%Y-%m-%d"),
            "d2": (dtb + timedelta(-1 * dtb.weekday() + 1)).strftime("%Y-%m-%d"),
            "d3": (dtb + timedelta(-1 * dtb.weekday() + 2)).strftime("%Y-%m-%d"),
            "d4": (dtb + timedelta(-1 * dtb.weekday() + 3)).strftime("%Y-%m-%d"),
            "d5": (dtb + timedelta(-1 * dtb.weekday() + 4)).strftime("%Y-%m-%d"),
            "d6": (dtb + timedelta(-1 * dtb.weekday() + 5)).strftime("%Y-%m-%d"),
            "r1": w[:7],
            "r2": w[7:14],
            "r3": w[14:21],
            "r4": w[21:28],
            "r5": w[28:35],
            "r6": w[35:42],
            "name": g[0].idgrp.name,
            "idp": t,  #"wd": wd,
            "light1": 'text-light' if (dtb + timedelta(-1 * dtb.weekday() + 0)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "light2": 'text-light' if (dtb + timedelta(-1 * dtb.weekday() + 0)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "light3": 'text-light' if (dtb + timedelta(-1 * dtb.weekday() + 2)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "light4": 'text-light' if (dtb + timedelta(-1 * dtb.weekday() + 3)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "light5": 'text-light' if (dtb + timedelta(-1 * dtb.weekday() + 4)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "light6": 'text-light' if (dtb + timedelta(-1 * dtb.weekday() + 5)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "bg1": 'bg-primary' if (dtb + timedelta(-1 * dtb.weekday() + 0)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "bg2": 'bg-primary' if (dtb + timedelta(-1 * dtb.weekday() + 1)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "bg3": 'bg-primary' if (dtb + timedelta(-1 * dtb.weekday() + 2)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "bg4": 'bg-primary' if (dtb + timedelta(-1 * dtb.weekday() + 3)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "bg5": 'bg-primary' if (dtb + timedelta(-1 * dtb.weekday() + 4)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "bg6": 'bg-primary' if (dtb + timedelta(-1 * dtb.weekday() + 5)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            }
    return render(request, "rasp/detailRaspGroup.html",
                  context=cntx)


def delRaspGroup(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Group not found</h2>")


def editRaspGroup(request, id):
    res = ""
    r = Rasp.objects.get(id=id)
    form = EditRasp(request.POST)
    wd = r.dt.isocalendar()[1]
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
            return HttpResponseRedirect("/rasp/rasp/person/" + str(r.idpers.id) + '/' + str(wd) + '/')
    else:
        form = EditRasp(instance=r)
        dt = r.dt
        idpara = r.idpara
    return render(request, "rasp/editRasp.html", {'form': form, "res": res, "dt": dt, "idpara": idpara})


def addRaspGroup(request, id):
    res = ""
    dt = datetime.strptime(request.GET.get("dt"), '%Y-%m-%d').date()
    wd = dt.isocalendar()[1]
    idpara = request.GET.get("np")
    if request.method == "POST":
        form = EditRasp(request.POST)
        if form.is_valid():
            form.paraid = Para.objects.get(id=idpara)
            # r.name = form.cleaned_data["name"]
            # r.idgrp = form.cleaned_data["idgrp"]
            # r.idpers = form.cleaned_data["idpers"]
            # r.idaud = form.cleaned_data["idaud"]
            # r.idpredmet = form.cleaned_data["idpredmet"]
            form.save()
            res = "cохранено"
            #return HttpResponseRedirect("{% url 'rspperson' form.idpers.id , wd %}")
            return HttpResponseRedirect("/rasp/rasp/person/" + str(id) + '/' + str(wd) + '/')
    else:
        r = Rasp()
        r.idpara = Para.objects.get(id=idpara)
        r.dt = dt
        form = EditRasp(instance=r)
    return render(request, "rasp/editRasp.html", {'form': form, "res": res, "dt": dt, "idpara": idpara})


def login(request):
    #wd = request.session['week']
    form = Login(request.POST)
    if request.method == "POST":
        if form.is_valid():
            request.session['userid'] = form.cleaned_data["fio"].id
            return HttpResponseRedirect("/")
    else:
        form = Login()
    return render(request, "rasp/login.html", context={'form': form})
    # return HttpResponseRedirect("/")


def listAdd(request):
    #wd = request.session['week']
    form = Login(request.POST)
    if request.method == "POST":
        if form.is_valid():
            t = MyPers()
            #print(form.fio)
            t.myid = Person.objects.get(id=request.session['userid'])
            t.persid = Person.objects.get(id=form.cleaned_data["fio"].id)
            try:
                t.save()
                return HttpResponseRedirect("/")
                # render(request, "rasp/indexPerson.html")
            except:
                error = 'Не удалось добавить в список повторно'
                return render(request, "rasp/error.html", context={'error': error})

    else:
        form = Login()
    return render(request, "rasp/listadd.html", context={'form': form})


def listDel(request, id):
    m = MyPers.objects.get(pk=id)
    m.delete()
    #m.save()
    # db.session.commit()
    return HttpResponseRedirect("/")
    pass
