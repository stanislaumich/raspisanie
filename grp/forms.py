from django.forms import ModelForm

from rasp.models import Rasp


class EditRasp(ModelForm):
    class Meta:
        model = Rasp
        fields = ('name', 'idgrp', 'idpers', 'idaud', 'idpredmet', 'idpara', 'dt')


