from django.shortcuts import render
from datetime import timedelta, datetime, date
import locale

from rasp.models import Person

locale.setlocale(locale.LC_ALL, "")

from django.http import HttpResponse
def index(request):
    # uid = request.session['userid']
    # p = Person.objects.get(id=uid)
    # fio = p.fio
    # fio = 'dfgb'#p.fio
    data = {'a': 'fio'}
    return render(request, "index.html", context=data)


def grid(request):
    #dtb = date(2024, 7, 6)
    dtb = datetime.now()
    #dw = dtb.weekday()
    #dtb = dtb + timedelta(-1 * dtb.weekday())
    #dtr = (dtb + timedelta(-1 * dtb.weekday())).strftime(",  %B %d ")
    #dr = dtb.strftime(",  %B %d ")#%m
    data = {"dt1": 'Понедельник,  '+(dtb + timedelta(-1 * dtb.weekday() + 0)).strftime("%B %d "),
            "dt2": 'Вторник,  '+(dtb + timedelta(-1 * dtb.weekday() + 1)).strftime("%B %d "),
            "dt3": 'Среда,  '+(dtb + timedelta(-1 * dtb.weekday() + 2)).strftime("%B %d "),
            "dt4": 'Четверг,  '+(dtb + timedelta(-1 * dtb.weekday() + 3)).strftime("%B %d "),
            "dt5": 'Пятница,  '+(dtb + timedelta(-1 * dtb.weekday() + 4)).strftime("%B %d "),
            "dt6": 'Суббота,  '+(dtb + timedelta(-1 * dtb.weekday() + 5)).strftime("%B %d "),
            }

    return render(request, "grid.html", context=data)


def contact(request):
    data = {"header": "Hello Django", "message": "Contact"}
    return render(request, "contact.html", context=data)


