from django.forms import ModelForm
from django import forms

from person.models import Person


class Login(ModelForm):
    fio = forms.ModelChoiceField(queryset=Person.objects.all())

    class Meta:
        model = Person
        fields = ('fio', 'password')

class List(ModelForm):
    fio = forms.ModelChoiceField(queryset=Person.objects.all())

    class Meta:
        model = Person
        fields = ('fio',)



