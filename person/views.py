from datetime import datetime, date, timedelta

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render

from grp.forms import EditRasp
from para.models import Para
from person.models import Person, MyPers
from person.forms import Login, List
from rasp.models import Rasp, Reserv


def datefromiso(year, week, day):
    return datetime.strptime("%d%02d%d" % (year, week, day), "%Y%W%w")

def isAdmin(request):
    return Person.objects.get(pk=request.session.get('userid', 0)).isAdmin == 1


def getuser(request):
    return request.session.get('userid', 0)


def getme(request):
    return Person.objects.get(pk=getuser(request))

def indexPerson(request):
    people = MyPers.objects.filter(myid=getuser(request)).all()
    # if isAdmin(request):
    #     messages.success(request, f"Администратор!!!!")

    return render(request, "person/indexPerson.html", context={"people": people})


def detailPerson(request, id):
    people = Person.objects.get(id=id)
    return render(request, "rasp/detailPerson.html", context={"p": people})


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
                try:
                    r = Reserv.objects.get(dt=dtb, idpara=j + 1, idpers=t)
                    w.append({'v': 2, 'i': r, "np": j})
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
            "fiop": pr.fio, "idp": t, #"wd": wd,
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
    return render(request, "person/detailRaspPers.html",
                  context=cntx)


def addRaspPers(request, id):
    res = ""
    dt = datetime.strptime(request.GET.get("dt"), '%Y-%m-%d').date()
    # wd = dt.isocalendar()[1]
    idpara = request.GET.get("np")
    if request.method == "POST":
        form = EditRasp(request.POST)
        if form.is_valid():
            form.paraid = Para.objects.get(id=idpara)
            form.save()
            res = "cохранено"
            messages.success(request, f"Занятие сохранено")
            # return HttpResponseRedirect(request.META.get('HTTP_REFERER')) работает только со ссылками
            return HttpResponseRedirect('/')
    else:
        r = Rasp()
        r.idpara = Para.objects.get(id=idpara)
        r.dt = dt
        r.idpers = Person.objects.get(pk=id)
        form = EditRasp(instance=r)
    return render(request, "rasp/editRasp.html", {'form': form, "res": res, "dt": dt, "idpara": idpara, 'zid':0})


def editRaspPers(request, id):
    res = ""
    r = Rasp.objects.get(id=id)
    rsp = r
    # form = EditRasp(request.POST)
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
            # return HttpResponseRedirect("/rasp/rasp/person/" + str(r.idpers.id) + '/' + str(wd) + '/')
            return HttpResponseRedirect("/")
    else:

        form = EditRasp(instance=r)
        dt = r.dt
        idpara = r.idpara
    return render(request, "rasp/editRasp.html", {'form': form, "res": res, "dt": dt, "idpara": idpara, 'rid' : rsp, 'zid':id})


def delRaspPers(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def listAdd(request):
    form = List(request.POST)
    if request.method == "POST":
        if form.is_valid():
            t = MyPers()
            t.myid = Person.objects.get(id=getuser(request))
            t.persid = Person.objects.get(id=form.cleaned_data["fio"].id)
            try:
                t.save()
                messages.success(request, f"Преподаватель  {t.persid.fio} добавлен")
                return HttpResponseRedirect('/person')
                # return render(request, url('personindex'))
            except:
                messages.error(request, f"Ошибка, преподаватель  {t.persid.fio} не добавлен!!!")
                error = 'Не удалось добавить в список повторно'
                # return render(request, "person/error.html", context={'error': error})
                return HttpResponseRedirect('/person')

    else:
        form = List()
    return render(request, "person/listadd.html", context={'form': form})


def listDel(request, id):
    m = MyPers.objects.get(pk=id)
    messages.success(request, f"Преподаватель  {m.persid.fio} удален из списка")
    m.delete()
    return HttpResponseRedirect("/person")


def login(request):
    form = Login(request.POST)
    if request.method == "POST":
        if form.is_valid():
            p = Person.objects.get(pk=form.cleaned_data["fio"].id)
            if form.cleaned_data["password"] == p.password:
                request.session['userid'] = form.cleaned_data["fio"].id
                messages.success(request, f"Преподаватель  {Person.objects.get(pk=getuser(request))} зарегистрирован в системе")
                return HttpResponseRedirect("/")
            else:
                messages.success(request,
                                 f"В полном доступе отказано, разрешены только действия анонима")
                return HttpResponseRedirect("/")
    else:

        form = Login(initial={'fio': 0, 'password': '0'})
    return render(request, "person/login.html", context={'form': form})
    # return HttpResponseRedirect("/")

def badlogin():
    pass
'''
<input type="hidden" name="return_to" value="{{ return_to_url }}">
return redirect(request.POST['return_to']))



'''


def logout(request):
    messages.success(request, f"Преподаватель  {Person.objects.get(pk=getuser(request))} вышел из системы")
    request.session['userid'] = 0
    request.session['password'] = ''
    return HttpResponseRedirect("/")


def delRaspPersReserv (request, id):
    # res = Reserv.objects.get(pk=id)
    # res.delete()
    messages.success(request, f"Кнопка R для снятия и установки резерва")
    return HttpResponseRedirect("/")


def addRaspPersReserv(request, id):
    if id==0:
        dt = datetime.strptime(request.GET.get("dt"), '%Y-%m-%d').date()
        idpara = request.GET.get("np")
        idp = request.GET.get("idp")
        r = Reserv()
        r.name = 'РЕЗЕРВ'
        r.idpara = Para.objects.get(id=idpara)
        r.dt = dt
        r.idpers = Person.objects.get(pk=idp)
        r.idmaster = getme(request)
        r.save()
        messages.success(request, f"Резерв установлен")
    else:
        res = Reserv.objects.get(pk=id)
        if res.idmaster == getme(request):
            res.delete()
            messages.success(request, f"Резерв снят")
        elif res.idpers == getme(request):
            res.delete()
            messages.success(request, f"Резерв снят")
        else:
            # res.delete()
            messages.error(request, f"Резерв можно снять только с себя или с тех на кого вы его установили. Чужой нельзя.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

