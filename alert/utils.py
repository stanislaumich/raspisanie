from alert.models import Alert


def send(toid,fromid,warn,short):
    a = Alert()
    a.toid = toid
    a.fromid = fromid
    a.warn = warn
    a.short = short
    try:
        a.save()
        return 1
    except:
        return 0

