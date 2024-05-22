from django.contrib import admin
from django.urls import path, re_path, include

from .import views

urlpatterns = [
    path('predmet/', views.indexPredmet, name="predmet"),
    path("predmet/<int:id>/", views.detailPredmet, name="predmet"),
    path("person/", views.indexPerson, name="person"),
    path("person/<int:id>/", views.detailPerson, name="person"),
	path("aud/", views.indexAud, name="aud"),
    path("aud/<int:id>/", views.detailAud, name="aud"),
    path("grp/", views.indexGrp, name="grp"),
    path("grp/<int:id>/", views.detailGrp, name="grp"),
    path("rasp/", views.indexRasp, name="rsp"),
    path("rasp/<int:id>/", views.detailRasp, name="rsp"),
    path("rasp/person/<int:id>/<int:wd>/", views.detailRaspPers, name="rspperson"),
    path("rasp/person/edit/<int:id>/", views.editRaspPers, name="rspedit"),
    path("rasp/person/check/", views.detailRaspPers, name="rspcheck"),
    path("rasp/person/del/<int:id>/", views.delRaspPers, name="rspdel"),
    path("rasp/gen/", views.genRaspPers, name="rspgen"),
]