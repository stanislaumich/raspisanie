from datetime import datetime

from rasp.models import Person

def getuser(request):
    return request.session.get('userid', 0)


def get_userfio(request):
    uid = getuser(request)
    try:
        p = Person.objects.get(id=uid)
        fio = p.fio
        return {'fio': fio, 'uid': uid}
    except:
        return {'fio': 'АНОНИМ', 'uid': 0}



def get_week(request):
    wd = request.session.get('week', datetime.today().isocalendar()[1])
    return {'wd': wd}
