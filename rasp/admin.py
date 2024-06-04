from django.contrib import admin
from .models import Rasp, Para, Person, Grp, Predmet, MyPers

admin.site.register(Predmet)
admin.site.register(Grp)
admin.site.register(Rasp)
admin.site.register(Para)
admin.site.register(Person)
admin.site.register(MyPers)