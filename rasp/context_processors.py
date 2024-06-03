from datetime import datetime

from rasp.models import Person


def get_userfio(request):
    #uid = request.session['userid']
    uid = request.session.get('userid', 1)
    p = Person.objects.get(id=uid)
    fio = p.fio
    # fio = request.session['fio']
    return{'fio': fio, 'uid': uid}

def get_week(request):
    #wd = request.session['week']
    wd = request.session.get('week', datetime.today().isocalendar()[1])
    # p = Person.objects.get(id=uid)
    # fio = p.fio
    # fio = request.session['fio']
    return{'wd': wd}