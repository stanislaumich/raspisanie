import time

from django.contrib import messages
from django.core.paginator import Paginator
from django.forms import SelectDateWidget, ModelForm, forms, IntegerField
from django.forms.utils import ErrorList
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, request, response
from django.urls import reverse_lazy, reverse
from alert import utils

from aud.models import Aud
from grpp.models import Grp
from para.models import Para
from person.models import Person
from predmet.models import Predmet

from .models import Rasp
from datetime import datetime, timedelta
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
import locale

locale.setlocale(locale.LC_ALL, "")


def getuser(request):
    return request.session.get('userid', 0)


def datefromiso(year, week, day):
    return datetime.strptime("%d%02d%d" % (year, week, day), "%Y%W%w")


def page_not_found_view(request, exception):
    return render(request, 'rasp/404.html', status=404)


def indexRasp(request):
    r = Rasp.objects.order_by("id")
    paginator = Paginator(r, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "rasp/indexRasp.html", context={"r": r, "page_obj": page_obj})


def detailRasp(request, id):
    t = id
    r = Rasp.objects.get(id=t)
    return render(request, "rasp/detailRasp.html", context={"r": r})


# ------------------------------------------


class EditRasp(UpdateView):
    model = Rasp
    queryset = Rasp.objects.all()
    fields = ['name', 'idgrp', 'idpers', 'idaud', 'idpredmet', 'idpara', 'dt']
    template_name = "rasp/editRasp.html"
    success_url = reverse_lazy('home')
    extra_context = {'zid': 0}


class AddRasp(CreateView):
    model = Rasp
    queryset = Rasp.objects.all()
    template_name = "rasp/editRasp.html"
    fields = ('name', 'idgrp', 'idpers', 'idaud', 'idpredmet', 'idpara', 'dt')
    widgets = {'dt': SelectDateWidget(years=range(2024, 2100))}
    success_url = reverse_lazy('home')
    extra_context = {'zid': 0}

    def get_initial(self):
        initial = super(AddRasp, self).get_initial()
        initial['dt'] = self.request.GET.get('dt')
        initial['idpara'] = Para.objects.get(id=self.request.GET.get('np'))
        if self.request.GET.get('idpers'):
            initial['idpers'] = Person.objects.get(id=self.request.GET.get('idpers'))
        if self.request.GET.get('idpredmet'):
            initial['idpredmet'] = Predmet.objects.get(id=self.request.GET.get('idpredmet'))
        if self.request.GET.get('idaud'):
            initial['idaud'] = Aud.objects.get(id=self.request.GET.get('idaud'))
        if self.request.GET.get('idgrp'):
            initial['idgrp'] = Grp.objects.get(id=self.request.GET.get('idgrp'))
        return initial

    def form_valid(self, form):
        f = super(AddRasp, self)
        # print(f)
        utils.send(
            toid=Person.objects.get(pk=form.instance.idpers.pk),
            fromid=Person.objects.get(pk=self.request.session.get('userid')),
            warn=0,
            short='Добавлено  расписание')
        form.save()
        return super().form_valid(form)


class DelRasp(DeleteView):
    # form_class = EditRasp
    model = Rasp
    queryset = Rasp.objects.all()
    fields = ['name', 'idgrp', 'idpers', 'idaud', 'idpredmet', 'idpara', 'dt']
    template_name = "rasp/delRasp.html"
    success_url = reverse_lazy('home')
    extra_context = {'zid': 0}

# ------------------------------------------
class Clone(forms.Form):
    n = IntegerField()
    def __init__(
            self,
            data=None,
            files=None,
            auto_id="id_%s",
            prefix=None,
            initial=None,
            error_class=ErrorList,
            label_suffix=None,
            empty_permitted=False,
            field_order=None,
            use_required_attribute=None,
            renderer=None,
    ):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, field_order,
                         use_required_attribute, renderer)
        # self.n = 1

    class Meta:
        fields = ('n',)

def clonerasp(request,id):
    form = Clone(request.POST)
    if request.method == "POST":
        if form.is_valid():
            r = Rasp.objects.get(pk=id)
            r.name = 'Занятие 1'
            r.save()
            n = form.cleaned_data['n']
            c = 0
            print(n)
            for i in range(n):
                p = Rasp()
                p.idpers = r.idpers
                p.idpara = r.idpara
                p.idaud = r.idaud
                p.idgrp = r.idgrp
                p.idpredmet = r.idpredmet
                p.name = 'Занятие '+str(c+2)
                p.dt = r.dt + timedelta(7*(c+1))
                try:
                    p.save()
                    messages.success(request, f"Запись продублирована")
                    c = c + 1
                except:
                    messages.error(request, f"Ошибка записи {p.dt}, место занято")


            return HttpResponseRedirect(reverse('home'))
    else:
        form = Clone()
    return render(request, "person/clone.html")
