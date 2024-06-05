from django.contrib import admin

from aud.models import MyAud
from rasp.models import Aud

admin.site.register(Aud)
admin.site.register(MyAud)
