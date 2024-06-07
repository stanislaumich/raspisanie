import time

from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse_lazy

from person.models import Person
from .models import Rasp
from datetime import datetime
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
    # form_class = EditRasp
    model = Rasp
    queryset = Rasp.objects.all()
    fields = ['name', 'idgrp', 'idpers', 'idaud', 'idpredmet', 'idpara', 'dt']
    template_name = "rasp/editRasp.html"
    success_url = reverse_lazy('home')
    extra_context = {'zid': 0}


class AddRasp(CreateView):
    # form_class = EditRasp
    model = Rasp
    queryset = Rasp.objects.all()
    fields = ['name', 'idgrp', 'idpers', 'idaud', 'idpredmet', 'idpara', 'dt']
    template_name = "rasp/editRasp.html"
    success_url = reverse_lazy('home')
    extra_context = {'zid': 0}

    # def get_initial(self):
    #     initial = super(AddRasp, self).get_initial()
    #     initial['idpers'] = Person.objects.get(id=self.kwargs['person_id'])
    #     return initial
    # def save(self):


class DelRasp(DeleteView):
    # form_class = EditRasp
    model = Rasp
    queryset = Rasp.objects.all()
    fields = ['name', 'idgrp', 'idpers', 'idaud', 'idpredmet', 'idpara', 'dt']
    template_name = "rasp/delRasp.html"
    success_url = reverse_lazy('home')
    extra_context = {'zid': 0}

# ------------------------------------------
