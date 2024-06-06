from datetime import datetime

from django.shortcuts import render


def datefromiso(year, week, day):
    return datetime.strptime("%d%02d%d" % (year, week, day), "%Y%W%w")


def getuser(request):
    return request.session.get('userid', 0)


def apiIndex(request):
    if not getuser(request):

        return 0
    else:

        return 0



def apiLogin(request):
    request.session['userid'] = 1
    return 0


def apiLogout(request):
    request.session['userid'] = 0
    return 0
