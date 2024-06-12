from django.contrib import admin

from person.models import Person, MyPers, MyNote

admin.site.register(Person)
admin.site.register(MyPers)
admin.site.register(MyNote)

