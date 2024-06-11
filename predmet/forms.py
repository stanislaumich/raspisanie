from django.forms import ModelForm

from predmet.models import Predmet
from rasp.models import Rasp
from django.forms import ModelForm, Textarea
from django import forms
from grpp.models import Grp


class PredmetList(ModelForm):
    name = forms.ModelChoiceField(queryset=Predmet.objects.all())

    class Meta:
        model = Predmet
        fields = ('name',)


