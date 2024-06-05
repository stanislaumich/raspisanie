from django.contrib import admin
from django.urls import path, re_path, include

from . import views

urlpatterns = [
    #common
    path("", views.indexRasp, name="rspindex"),
    path("<int:id>/", views.detailRasp, name="rspdetail"),
       # tests
    path("gen/", views.genRaspPers, name="rspgen"),
    path("test/", views.test, name="rsptest"),

]
