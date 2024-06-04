from django import forms
from django.forms import ModelForm, Textarea

from mess.models import Mess
from rasp.models import Person


class MessAdd(ModelForm):
    toid = forms.ModelChoiceField(queryset=Person.objects.all())

    class Meta:
        model = Mess
        fields = ('short', 'long', 'warn', 'toid')
        widgets = {
            "long": Textarea(attrs={"cols": 40, "rows": 10}),
            "short": Textarea(attrs={"cols": 40, "rows": 3}),
        }
        labels = {
            "long": "Writer",
        }
