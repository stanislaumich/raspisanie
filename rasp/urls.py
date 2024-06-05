from django.contrib import admin
from django.urls import path, re_path, include

from . import views

urlpatterns = [
    #common
    path('predmet/', views.indexPredmet, name="predmetindex"),
    path("predmet/<int:id>/", views.detailPredmet, name="predmetdetail"),
    path("rasp/", views.indexRasp, name="rspindex"),
    path("rasp/<int:id>/", views.detailRasp, name="rspdetail"),
       # tests
    path("rasp/gen/", views.genRaspPers, name="rspgen"),
    path("rasp/test/", views.test, name="rsptest"),

]
