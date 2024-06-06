from django.http import HttpResponseRedirect
from django.shortcuts import render
from mess.forms import MessAdd
from mess.models import Mess
from rasp.models import  Person

def getuser(request):
    return request.session.get('userid', 0)


def messClear(request, id):
    m = Mess.objects.get(pk=id)
    m.isActive = 0
    m.save()
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
            t.fromid = Person.objects.get(id=getuser(request))
            t.toid = Person.objects.get(id=form.cleaned_data["toid"].id)
            t.save()
            return HttpResponseRedirect("/")
    else:

        if id != 0:
            form = MessAdd(initial={'toid': id})
        else:
            form = MessAdd()

    return render(request, "mess/messadd.html", context={'form': form})
