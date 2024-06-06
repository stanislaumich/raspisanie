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

class List(ModelForm):
    fio = forms.ModelChoiceField(queryset=Person.objects.all())

    class Meta:
        model = Person
        fields = ('fio',)

class EditRasp(ModelForm):
    class Meta:
        model = Rasp
        fields = ('name', 'idgrp', 'idpers', 'idaud', 'idpredmet', 'idpara', 'dt')

