from django.contrib import admin
from .models import Rasp, Para, Person, Grp, Aud, Predmet, MyPers, Mess

admin.site.register(Predmet)
admin.site.register(Aud)
admin.site.register(Grp)
admin.site.register(Rasp)
admin.site.register(Para)
admin.site.register(Person)
admin.site.register(Mess)
admin.site.register(MyPers)