from django.contrib import admin
from django.urls import path, re_path, include

from rasp import views

urlpatterns = [
    #common
    path("", views.indexRasp, name="rspindex"),
    path("<int:id>/", views.detailRasp, name="rspdetail"),
    path("del/<int:id>/", views.delRaspPers, name="rspdelete"),
       # tests
    path("gen/", views.genRaspPers, name="rspgen"),
    path("test/", views.test, name="rsptest"),

]
