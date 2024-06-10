from datetime import datetime, date, timedelta

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, UpdateView, DeleteView

from alert import utils
from para.models import Para
from person.models import Person, MyPers
from person.forms import Login, List, Register
from rasp.models import Rasp, Reserv
from raspisanie.settings import MEDIA_URL


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
            "fiop": pr.fio, "idp": t,  # "wd": wd,
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


# --------------------------------
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
                messages.success(request,
                                 f"Преподаватель  {Person.objects.get(pk=getuser(request))} зарегистрирован в системе")
                return HttpResponseRedirect("/")
            else:
                messages.success(request,
                                 f"В полном доступе отказано, разрешены только действия анонима")
                return HttpResponseRedirect("/")
    else:

        form = Login(initial={'fio': 0, 'password': '0'})
    return render(request, "person/login.html", context={'form': form})


def register(request):
    form = Register(request.POST)
    if request.method == "POST":
        if form.is_valid():
            p = Person()
            p.fio = form.cleaned_data["fio"].upper()
            p.fam = form.cleaned_data["fam"]
            p.name = form.cleaned_data["name"]
            p.otch = form.cleaned_data["otch"]
            p.born = form.cleaned_data["born"]
            p.dolg = form.cleaned_data["dolg"]
            p.password = form.cleaned_data["password"]
            p.save()
            request.session['userid'] = p.id
            messages.success(request,
                             f"Преподаватель  {Person.objects.get(pk=getuser(request))} зарегистрирован в системе")
            return HttpResponseRedirect("/")
    else:
        form = Register()
    return render(request, "person/register.html", context={'form': form})


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


def delRaspPersReserv(request, id):
    # r = Reserv.objects.get(pk=id)
    # utils.send(
    #     toid=r.idpers,
    #     fromid=r.idmaster,
    #     warn=0,
    #     short=f'Установлен резерв {r.idpara} {dt}')
    # r.delete()

    messages.success(request, f"Кнопка R для снятия и установки резерва")
    return HttpResponseRedirect("/")


def addRaspPersReserv(request, id):
    if id == 0:
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
        utils.send(
            toid=r.idpers,
            fromid=r.idmaster,
            warn=0,
            short=f'Установлен резерв {r.idpara} {dt}')
        messages.success(request, f"Резерв установлен")
    else:
        res = Reserv.objects.get(pk=id)
        if res.idmaster == getme(request):
            utils.send(
                toid=res.idpers,
                fromid=res.idmaster,
                warn=0,
                short=f'Снят резерв {res.idpara} {res.dt}')
            res.delete()
            messages.success(request, f"Резерв снят")
        elif res.idpers == getme(request):
            utils.send(
                toid=res.idpers,
                fromid=res.idmaster,
                warn=0,
                short=f'Снят резерв {res.idpara} {res.dt}')
            res.delete()
            messages.success(request, f"Резерв снят")
        else:
            # res.delete()
            messages.error(request,
                           f"Резерв можно снять только с себя или с тех на кого вы его установили. Чужой нельзя.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def profilePers(request, id):
    if request.method == "POST":
        old = request.POST.get("old")
        new1 = request.POST.get("new1")
        new2 = request.POST.get("new2")
        # print(old, new1, new2)
        uid = getme(request)
        data = {'photo': uid.profphoto.url, 'id': uid.id}
        p = Person.objects.all().filter(id=uid.id, password=old)
        if new1 == new2 and p:
            r = Person.objects.get(id=uid.id)
            r.password = new1
            r.save()
            messages.success(request, f"Пароль изменен")
        else:
            messages.error(request, f"Неверные данные")
        return render(request, "person/profile.html", context=data)
    else:
        uid = getme(request)
        data = {'photo': uid.profphoto.url, 'id': uid.id}
        return render(request, "person/profile.html", context=data)

