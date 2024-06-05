from django import forms
from django.forms import ModelForm, Textarea

from aud.models import Aud


class AudList(ModelForm):
    name = forms.ModelChoiceField(queryset=Aud.objects.all())

    class Meta:
        model = Aud
        fields = ('name',)
