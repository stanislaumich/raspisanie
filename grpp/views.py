from datetime import datetime, timedelta, date

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse

# from aud.views import gen_rasp
from grpp.forms import EditRasp, GrpList
from grpp.models import MyGrp
from rasp.models import Grp, Para, Rasp, Person


def getuser(request):
    return request.session.get('userid', 0)


def datefromiso(year, week, day):
    return datetime.strptime("%d%02d%d" % (year, week, day), "%Y%W%w")


def indexGrp(request):
    g = MyGrp.objects.filter(myid=getuser(request)).all()
    return render(request, "grp/indexGrp.html", context={"g": g})


def detailGrp(request, id):
    t = id
    g = Grp.objects.get(id=t)
    wd = 22
    return render(request, "grp/detailGrp.html", context={"g": g})


# ++++++++++++++++++
def detailRaspGroup(request, id, wd):
    t = id
    a = Grp.objects.get(pk=id)
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
            "name": a.name,
            "idp": t,
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
    return render(request, "grp/detailRaspGrp.html",
                  context=cntx)


def delRaspGroup(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect(reverse('home'))
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Group not found</h2>")


# def editRaspGroup(request, id):
#     res = ""
#     r = Rasp.objects.get(id=id)
#     form = EditRasp(request.POST)
#     wd = r.dt.isocalendar()[1]
#     dt = r.dt
#     idpara = r.idpara
#     if request.method == "POST":
#         form = EditRasp(request.POST)
#         if form.is_valid():
#             r.id = id
#             r.name = form.cleaned_data["name"]
#             r.idgrp = form.cleaned_data["idgrp"]
#             r.idpers = form.cleaned_data["idpers"]
#             r.idaud = form.cleaned_data["idaud"]
#             r.idpredmet = form.cleaned_data["idpredmet"]
#             r.save()
#             res = "cохранено"
#             return HttpResponseRedirect("/rasp/rasp/person/" + str(r.idpers.id) + '/' + str(wd) + '/')
#     else:
#         form = EditRasp(instance=r)
#         dt = r.dt
#         idpara = r.idpara
#     return render(request, "rasp/editRasp.html", {'form': form, "res": res, "dt": dt, "idpara": idpara})
#
#
# def addRaspGroup(request, id):
#     res = ""
#     dt = datetime.strptime(request.GET.get("dt"), '%Y-%m-%d').date()
#     wd = dt.isocalendar()[1]
#     idpara = request.GET.get("np")
#     if request.method == "POST":
#         form = EditRasp(request.POST)
#         if form.is_valid():
#             form.paraid = Para.objects.get(id=idpara)
#             form.save()
#             res = "cохранено"
#             # return HttpResponseRedirect("{% url 'rspperson' form.idpers.id , wd %}")
#             return HttpResponseRedirect("/rasp/rasp/person/" + str(id) + '/' + str(wd) + '/')
#     else:
#         r = Rasp()
#         r.idpara = Para.objects.get(id=idpara)
#         r.dt = dt
#         form = EditRasp(instance=r)
#     return render(request, "rasp/editRasp.html", {'form': form, "res": res, "dt": dt, "idpara": idpara})


def grpadd(request):
    form = GrpList(request.POST)
    if request.method == "POST":
        if form.is_valid():
            t = MyGrp()
            t.myid = Person.objects.get(id=getuser(request))
            t.grpid = Grp.objects.get(id=form.cleaned_data["name"].id)
            try:
                t.save()
                messages.success(request, f"Группа  {t.grpid.name} добавлена")
                return HttpResponseRedirect(reverse('home'))
            except:
                messages.error(request, 'Не удалось добавить группу в список повторно')
                error = ''
                # return render(request, "grpp/error.html", context={'error': error})
                return HttpResponseRedirect(reverse('home'))

    else:
        form = GrpList()
    return render(request, "grp/listadd.html", context={'form': form})


def grpdel(request, id):
    m = MyGrp.objects.get(pk=id)
    messages.success(request, f"Группа {m.grpid.name} удалена")
    m.delete()
    return HttpResponseRedirect(reverse('home'))