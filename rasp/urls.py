from django.contrib import admin
from django.urls import path, re_path, include

from .import views

urlpatterns = [
    path('predmet/', views.indexPredmet, name="predmetindex"),
    path("predmet/<int:id>/", views.detailPredmet, name="predmetdetail"),
    path("person/", views.indexPerson, name="personindex"),
    path("person/<int:id>/", views.detailPerson, name="persondetail"),
	path("aud/", views.indexAud, name="audindex"),
    path("aud/<int:id>/", views.detailAud, name="auddetail"),
    path("grp/", views.indexGrp, name="grpindex"),
    path("grp/<int:id>/", views.detailGrp, name="grpdetail"),
    path("rasp/", views.indexRasp, name="rspindex"),
    path("rasp/<int:id>/", views.detailRasp, name="rspdetail"),

    path("rasp/person/<int:id>/<int:wd>/", views.detailRaspPers, name="rspperson"),
    path("rasp/person/edit/<int:id>/", views.editRaspPers, name="rspedit"),
    path("rasp/person/del/<int:id>/", views.delRaspPers, name="rspdel"),
    #path("rasp/person/check/", views.detailRaspPers, name="rspcheck"),

    #path("rasp/gen/", views.genRaspPers, name="rspgen"),
]