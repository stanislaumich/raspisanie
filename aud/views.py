from django.shortcuts import render
from .models import Aud
from django.http import HttpResponse

def index(request):
    a = Aud.objects.order_by("name")
    return render(request, "aud/aud.html", context={"aud": a})
def aud(request, id):
    t=id
    a = Aud.objects.get(id=t)
    return render(request, "aud/audone.html", context={"a": a})