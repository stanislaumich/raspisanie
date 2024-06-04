from datetime import datetime

from rasp.models import Person


def get_userfio(request):
    uid = request.session.get('userid', 1)
    p = Person.objects.get(id=uid)
    fio = p.fio
    return {'fio': fio, 'uid': uid}


def get_week(request):
    wd = request.session.get('week', datetime.today().isocalendar()[1])
    return {'wd': wd}
