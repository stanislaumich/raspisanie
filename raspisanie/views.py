from django.shortcuts import render
from datetime import timedelta, datetime, date
import locale
locale.setlocale(locale.LC_ALL, "")

from django.http import HttpResponse
def index(request):
    data = {"header": "Hello Django", "message": "Welcome to Python"}
    return render(request, "index.html", context=data)


def grid(request):
    #dtb = date(2024, 7, 6)
    dtb = datetime.now()
    #dw = dtb.weekday()
    #dtb = dtb + timedelta(-1 * dtb.weekday())
    #dtr = (dtb + timedelta(-1 * dtb.weekday())).strftime(",  %B %d ")
    #dr = dtb.strftime(",  %B %d ")#%m
    data = {"dt1": (dtb + timedelta(-1 * dtb.weekday()+0)).strftime(",  %B %d "),
            "dt2": (dtb + timedelta(-1 * dtb.weekday() + 1)).strftime(",  %B %d "),
            "dt3": (dtb + timedelta(-1 * dtb.weekday() + 2)).strftime(",  %B %d "),
            "dt4": (dtb + timedelta(-1 * dtb.weekday() + 3)).strftime(",  %B %d "),
            "dt5": (dtb + timedelta(-1 * dtb.weekday() + 4)).strftime(",  %B %d "),
            "dt6": (dtb + timedelta(-1 * dtb.weekday() + 5)).strftime(",  %B %d "),
            }

    return render(request, "grid.html", context=data)


def contact(request):
    data = {"header": "Hello Django", "message": "Contact"}
    return render(request, "contact.html", context=data)


