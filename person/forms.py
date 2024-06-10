from django.forms import ModelForm
from django import forms
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from person.models import Person


class Login(ModelForm):
    fio = forms.ModelChoiceField(queryset=Person.objects.all())

    class Meta:
        model = Person
        fields = ('fio', 'password')


class Register(ModelForm):
    # fio = forms.ModelChoiceField(queryset=Person.objects.all())

    class Meta:
        model = Person
        fields = ('fio', 'fam', 'name', 'otch', 'born', 'dolg', 'password')


class List(ModelForm):
    fio = forms.ModelChoiceField(queryset=Person.objects.all())

    class Meta:
        model = Person
        fields = ('fio',)


class EditPhoto(UpdateView):
    model = Person
    queryset = Person.objects.all()
    fields = ['profphoto']
    template_name = "person/profilephoto.html"
    success_url = reverse_lazy('home')
    extra_context = {'zid': 0}
