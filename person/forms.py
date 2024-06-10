from django.forms import ModelForm
from django import forms
from django.views.generic import UpdateView

from person.models import Person
from rasp.models import Rasp


class Login(ModelForm):
    fio = forms.ModelChoiceField(queryset=Person.objects.all())

    class Meta:
        model = Person
        fields = ('fio', 'password')

class Register(ModelForm):
    # fio = forms.ModelChoiceField(queryset=Person.objects.all())

    class Meta:
        model = Person
        fields = ('fio', 'fam','name','otch','born','dolg','password')



class List(ModelForm):
    fio = forms.ModelChoiceField(queryset=Person.objects.all())

    class Meta:
        model = Person
        fields = ('fio',)

