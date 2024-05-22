from django import forms
from django.forms import ModelForm

from .models import  Rasp


class EditRasp(ModelForm):
    class Meta:
        model = Rasp
        fields = ('name', 'idgrp', 'idpers', 'idaud', 'idpredmet')

