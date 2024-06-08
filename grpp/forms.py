from django.forms import ModelForm

from rasp.models import Rasp
from django.forms import ModelForm, Textarea
from django import forms
from grpp.models import Grp


class GrpList(ModelForm):
    name = forms.ModelChoiceField(queryset=Grp.objects.all())

    class Meta:
        model = Grp
        fields = ('name',)


class EditRasp(ModelForm):
    class Meta:
        model = Rasp
        fields = ('name', 'idgrp', 'idpers', 'idaud', 'idpredmet', 'idpara', 'dt')
