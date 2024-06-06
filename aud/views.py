from datetime import datetime, date, timedelta

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

from aud.forms import AudList
from aud.models import Aud
from rasp.models import Rasp, Para, MyAud, Person

def getuser(request):
    return request.session.get('userid', 0)

def datefromiso(year, week, day):
    return datetime.strptime("%d%02d%d" % (year, week, day), "%Y%W%w")


def indexAud(request):
    a = MyAud.objects.filter(myid=getuser(request)).all()
    return render(request, "aud/indexAud.html", context={"aud": a})


def detailAud(request, id):
    t = id
    a = Aud.objects.get(id=t)
    return render(request, "aud/detailAud.html", context={"a": a})

def detailRaspAud(request, id, wd):
    t = id
    # g = Rasp.objects.filter(idaud=t, dt__week=wd).order_by("dt", "idpara_id")

    a = Aud.objects.get(pk = id)
    k = 0
    w = []

    dtb = datefromiso(date.today().year, wd, 1).date()
    dtb = dtb + timedelta(-1 * dtb.weekday() + 0)
    for i in range(6):
        for j in range(7):
            try:
                r = Rasp.objects.get(dt=dtb, idpara=j + 1, idaud=t)
                w.append({'v': 1, 'i': r, "np": j})
            except:
                w.append({'v': 0, 'i': Para.objects.get(id=j + 1), "np": j + 1})
            k = k + 1
        dtb = dtb + timedelta(1)

    request.session['week'] = wd
    cntx = {"r": w, "wdn": wd + 1, "wdp": wd - 1, "i": t, "wd": wd,
            "dt1": '(' + a.name + ')  -+-   Понедельник,  ' + (
                        dtb + timedelta(-1 * dtb.weekday() + 0)).strftime("%B %d "),
            "dt2": '(' + a.name + ')  -+-   Вторник,  ' + (dtb + timedelta(-1 * dtb.weekday() + 1)).strftime(
                "%B %d "),
            "dt3": '(' + a.name + ')  -+-   Среда,  ' + (dtb + timedelta(-1 * dtb.weekday() + 2)).strftime(
                "%B %d "),
            "dt4": '(' + a.name + ')  -+-   Четверг,  ' + (dtb + timedelta(-1 * dtb.weekday() + 3)).strftime(
                "%B %d "),
            "dt5": '(' + a.name + ')  -+-   Пятница,  ' + (dtb + timedelta(-1 * dtb.weekday() + 4)).strftime(
                "%B %d "),
            "dt6": '(' + a.name + ')  -+-   Суббота,  ' + (dtb + timedelta(-1 * dtb.weekday() + 5)).strftime(
                "%B %d "),
            "d1": (dtb + timedelta(-1 * dtb.weekday() + 0)).strftime("%Y-%m-%d"),
            "d2": (dtb + timedelta(-1 * dtb.weekday() + 1)).strftime("%Y-%m-%d"),
            "d3": (dtb + timedelta(-1 * dtb.weekday() + 2)).strftime("%Y-%m-%d"),
            "d4": (dtb + timedelta(-1 * dtb.weekday() + 3)).strftime("%Y-%m-%d"),
            "d5": (dtb + timedelta(-1 * dtb.weekday() + 4)).strftime("%Y-%m-%d"),
            "d6": (dtb + timedelta(-1 * dtb.weekday() + 5)).strftime("%Y-%m-%d"),
            "r1": w[:7], "r2": w[7:14], "r3": w[14:21],
            "r4": w[21:28], "r5": w[28:35], "r6": w[35:42],
            "aname": a.name, "idp": 1,
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
    return render(request, "aud/detailRaspAud.html",
                  context=cntx)


def audadd(request):
    form = AudList(request.POST)
    if request.method == "POST":
        if form.is_valid():
            t = MyAud()
            t.myid = Person.objects.get(id=getuser(request))
            t.audid = Aud.objects.get(id=form.cleaned_data["name"].id)
            try:
                t.save()
                messages.success(request, f"Аудитория  {t.audid.name} добавлена")
                return HttpResponseRedirect('/aud')
            except:
                messages.error(request, 'Не удалось добавить аудиторию в список повторно')
                error = form.errors
                return render(request, "aud/error.html", context={'error': error})

    else:
        form = AudList()
    return render(request, "aud/listadd.html", context={'form': form})


def auddel(request, id):
    m = MyAud.objects.get(pk=id)
    messages.success(request, f"Аудитория {m.audid.name} удалена")
    m.delete()
    return HttpResponseRedirect('/aud')
