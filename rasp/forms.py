from django import forms
from django.forms import ModelForm

from .models import Rasp, Person


class EditRasp(ModelForm):
    class Meta:
        model = Rasp
        fields = ('name', 'idgrp', 'idpers', 'idaud', 'idpredmet', 'idpara', 'dt')

class Login(ModelForm):
    fio = forms.ModelChoiceField(queryset=Person.objects.all())
    class Meta:
        model = Person
        fields = ('fio',)

