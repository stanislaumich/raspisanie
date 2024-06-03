from rasp.models import Person


def get_userfio(request):
    uid = request.session['userid']
    p = Person.objects.get(id=uid)
    fio = p.fio
    # fio = request.session['fio']
    return{'fio': fio, 'uid': uid}

def get_week(request):
    wd = request.session['week']
    # p = Person.objects.get(id=uid)
    # fio = p.fio
    # fio = request.session['fio']
    return{'wd': wd}