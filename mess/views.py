from django.http import HttpResponseRedirect
from django.shortcuts import render

from rasp.forms import MessAdd
from rasp.models import Mess, Person


def messClear(request, id):
    m = Mess.objects.get(pk=id)
    m.isActive = 0
    m.save()
    #db.session.commit()
    return HttpResponseRedirect("/")


def messSend(request, id):
    form = MessAdd(request.POST)
    if request.method == "POST":
        if form.is_valid():
            t = Mess()
            # print(form.fio)
            t.long = form.cleaned_data["long"]
            t.short = form.cleaned_data["short"]
            t.warn = form.cleaned_data["warn"]
            t.fromid = Person.objects.get(id=request.session.get('userid'))
            t.toid = Person.objects.get(id=form.cleaned_data["toid"].id)
            t.save()
            return HttpResponseRedirect("/")
    else:

        if id != 0:
            form = MessAdd(initial={'toid': id})
        else:
            form = MessAdd()

    return render(request, "rasp/messadd.html", context={'form': form})
    #return HttpResponseRedirect("/")
