from django.shortcuts import render
from datetime import timedelta, datetime, date
import locale

from alert.models import Alert
from mess.models import Mess
from rasp.models import Person

locale.setlocale(locale.LC_ALL, "")

from django.http import HttpResponse


def index(request):
    uid = request.session.get('userid', 1)
    mes = Mess.objects.filter(toid=uid, isActive=1).all()
    mesmy = Mess.objects.filter(fromid=uid, isActive=1).all()
    messys = Alert.objects.filter(toid=uid, isActive=1).all()
    data = {'a': 'fio', 'mes': mes, 'mesmy': mesmy, 'messys':messys}
    return render(request, "index.html", context=data)


def grid(request):
    #dtb = date(2024, 7, 6)
    dtb = datetime.now()
    #dw = dtb.weekday()
    #dtb = dtb + timedelta(-1 * dtb.weekday())
    #dtr = (dtb + timedelta(-1 * dtb.weekday())).strftime(",  %B %d ")
    #dr = dtb.strftime(",  %B %d ")#%m
    data = {"dt1": 'Понедельник,  ' + (dtb + timedelta(-1 * dtb.weekday() + 0)).strftime("%B %d "),
            "dt2": 'Вторник,  ' + (dtb + timedelta(-1 * dtb.weekday() + 1)).strftime("%B %d "),
            "dt3": 'Среда,  ' + (dtb + timedelta(-1 * dtb.weekday() + 2)).strftime("%B %d "),
            "dt4": 'Четверг,  ' + (dtb + timedelta(-1 * dtb.weekday() + 3)).strftime("%B %d "),
            "dt5": 'Пятница,  ' + (dtb + timedelta(-1 * dtb.weekday() + 4)).strftime("%B %d "),
            "dt6": 'Суббота,  ' + (dtb + timedelta(-1 * dtb.weekday() + 5)).strftime("%B %d "),
            }

    return render(request, "grid.html", context=data)


def contact(request):
    data = {"header": "Hello Django", "message": "Contact"}
    return render(request, "contact.html", context=data)
