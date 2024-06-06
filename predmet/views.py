from datetime import date, timedelta, datetime

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from para.models import Para
from person.models import Person
from predmet.forms import PredmetList, EditPredmet
from predmet.models import Predmet, MyPredmet
from rasp.models import Rasp


def datefromiso(year, week, day):
    return datetime.strptime("%d%02d%d" % (year, week, day), "%Y%W%w")


def getuser(request):
    return request.session.get('userid', 0)


def indexPredmet(request):
    p = MyPredmet.objects.filter(myid=getuser(request)).all()
    return render(request, "predmet/indexPredmet.html", context={"p": p})


def detailPredmet(request, id):
    t = id
    p = Predmet.objects.get(id=t)
    return render(request, "predmet/detailPredmet.html", context={"p": p})




def predmetRasp(request, id, wd):
    t = id
    a = Predmet.objects.get(pk=id)
    dtb = datefromiso(date.today().year, wd, 1).date()
    dtb = dtb + timedelta(-1 * dtb.weekday() + 0)
    k = 0
    w = []
    for i in range(6):
        for j in range(7):
            try:
                r = Rasp.objects.get(dt=dtb, idpara=j + 1, idgrp=t)
                w.append({'v': 1, 'i': r, "np": j})
            except:
                w.append({'v': 0, 'i': Para.objects.get(id=j + 1), "np": j + 1})
            k = k + 1
        dtb = dtb + timedelta(1)

    request.session['week'] = wd

    cntx = {"r": w, "wdn": wd + 1, "wdp": wd - 1, "i": t, "wd": wd,
            "dt1": '(' + a.name + ')  -+-   Понедельник,  ' + (
                    dtb + timedelta(-1 * dtb.weekday() + 0)).strftime("%B %d "),
            "dt2": '(' + a.name + ')  -+-   Вторник,  ' + (
                        dtb + timedelta(-1 * dtb.weekday() + 1)).strftime(
                "%B %d "),
            "dt3": '(' + a.name + ')  -+-   Среда,  ' + (dtb + timedelta(-1 * dtb.weekday() + 2)).strftime(
                "%B %d "),
            "dt4": '(' + a.name + ')  -+-   Четверг,  ' + (
                        dtb + timedelta(-1 * dtb.weekday() + 3)).strftime(
                "%B %d "),
            "dt5": '(' + a.name + ')  -+-   Пятница,  ' + (
                        dtb + timedelta(-1 * dtb.weekday() + 4)).strftime(
                "%B %d "),
            "dt6": '(' + a.name + ')  -+-   Суббота,  ' + (
                        dtb + timedelta(-1 * dtb.weekday() + 5)).strftime(
                "%B %d "),
            "d1": (dtb + timedelta(-1 * dtb.weekday() + 0)).strftime("%Y-%m-%d"),
            "d2": (dtb + timedelta(-1 * dtb.weekday() + 1)).strftime("%Y-%m-%d"),
            "d3": (dtb + timedelta(-1 * dtb.weekday() + 2)).strftime("%Y-%m-%d"),
            "d4": (dtb + timedelta(-1 * dtb.weekday() + 3)).strftime("%Y-%m-%d"),
            "d5": (dtb + timedelta(-1 * dtb.weekday() + 4)).strftime("%Y-%m-%d"),
            "d6": (dtb + timedelta(-1 * dtb.weekday() + 5)).strftime("%Y-%m-%d"),
            "r1": w[:7], "r2": w[7:14], "r3": w[14:21],
            "r4": w[21:28], "r5": w[28:35], "r6": w[35:42],
            "aname": a.name, "idp": t,
            "light1": 'text-light' if (dtb + timedelta(-1 * dtb.weekday() + 0)).strftime(
                "%B %d ") == datetime.today().strftime("%B %d ") else '',
            "light2": 'text-light' if (dtb + timedelta(-1 * dtb.weekday() + 1)).strftime(
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
    return render(request, "predmet/detailRaspPredmet.html",
                  context=cntx)


def addRaspPredmet(request,id):
    res = ""
    dt = datetime.strptime(request.GET.get("dt"), '%Y-%m-%d').date()
    wd = dt.isocalendar()[1]
    idpara = request.GET.get("np")
    if request.method == "POST":
        form = EditPredmet(request.POST)
        if form.is_valid():
            form.paraid = Para.objects.get(id=idpara)
            form.save()
            res = "cохранено"
            # return HttpResponseRedirect("{% url 'rspperson' form.idpers.id , wd %}")
            # return HttpResponseRedirect("/rasp/rasp/person/" + str(id) + '/' + str(wd) + '/')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        r = Rasp()
        r.idpara = Para.objects.get(id=idpara)
        r.dt = dt
        form = EditPredmet(instance=r)
    return render(request, "rasp/editRasp.html", {'form': form, "res": res, "dt": dt, "idpara": idpara})

def editRaspPredmet(request,id):
    res = ""
    r = Rasp.objects.get(id=id)
    form = EditPredmet(request.POST)
    wd = r.dt.isocalendar()[1]
    dt = r.dt
    idpara = r.idpara
    if request.method == "POST":
        form = EditPredmet(request.POST)
        if form.is_valid():
            # r.id = id
            r = Rasp.objects.get(id=id)
            r.name = form.cleaned_data["name"]
            r.idgrp = form.cleaned_data["idgrp"]
            r.idpers = form.cleaned_data["idpers"]
            r.idaud = form.cleaned_data["idaud"]
            r.idpredmet = form.cleaned_data["idpredmet"]
            r.save(force_update=True)

            # res = "cохранено"
            messages.success('Сохранено')
            # return HttpResponseRedirect("/rasp/rasp/person/" + str(r.idpers.id) + '/' + str(wd) + '/')
            # return HttpResponseRedirect('/')
            return render(request, "predmet/indexPredmet.html")
    else:
        form = EditPredmet(instance=r)
        dt = r.dt
        idpara = r.idpara
    return render(request, "rasp/editRasp.html", {'form': form, "res": res, "dt": dt, "idpara": idpara, 'zid': id})



def predmetadd(request):
    form = PredmetList(request.POST)
    if request.method == "POST":
        if form.is_valid():
            t = MyPredmet()
            t.myid = Person.objects.get(id=getuser(request))
            t.predmetid = Predmet.objects.get(id=form.cleaned_data["name"].id)
            try:
                t.save()
                messages.success(request, f"Предмет  {t.predmetid.name} добавлен")
                return HttpResponseRedirect('/predmet')
            except:
                messages.error(request, 'Не удалось добавить предмет в список повторно')
                error = form.errors
                # return render(request, "predmet/error.html", context={'error': error})
                return HttpResponseRedirect('/predmet')

    else:
        form = PredmetList()
    return render(request, "predmet/listadd.html", context={'form': form})


def predmetdel(request, id):
    m = MyPredmet.objects.get(pk=id)
    messages.success(request, f"Предмет {m.predmetid.name} удален")
    m.delete()
    return HttpResponseRedirect('/predmet')
