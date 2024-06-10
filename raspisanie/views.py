import locale

from django.shortcuts import render

from alert.models import Alert
from mess.models import Mess

locale.setlocale(locale.LC_ALL, "")


def index(request):
    uid = request.session.get('userid', 0)
    mes = Mess.objects.filter(toid=uid, isActive=1).all().order_by('-id')
    mesmy = Mess.objects.filter(fromid=uid, isActive=1).all().order_by('-id')
    messys = Alert.objects.filter(toid=uid, isActive=1).all().order_by('-id')
    data = {'a': 'fio', 'mes': mes, 'mesmy': mesmy, 'messys':messys}
    return render(request, "index.html", context=data)

