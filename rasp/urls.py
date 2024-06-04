from django.contrib import admin
from django.urls import path, re_path, include

from . import views

urlpatterns = [
    #common
    path('predmet/', views.indexPredmet, name="predmetindex"),
    path("predmet/<int:id>/", views.detailPredmet, name="predmetdetail"),
    path("person/", views.indexPerson, name="personindex"),
    path("person/<int:id>/", views.detailPerson, name="persondetail"),


    path("rasp/", views.indexRasp, name="rspindex"),
    path("rasp/<int:id>/", views.detailRasp, name="rspdetail"),

    # rasp for person
    path("rasp/person/<int:id>/<int:wd>/", views.detailRaspPers, name="rspperson"),
    path("rasp/person/add/<int:id>/", views.addRaspPers, name="rspadd"),
    path("rasp/person/edit/<int:id>/", views.editRaspPers, name="rspedit"),
    path("rasp/person/del/<int:id>/", views.delRaspPers, name="rspdel"),
    path("rasp/person/listadd/", views.listAdd, name="rsplistadd"),
    path("rasp/person/listdel/<int:id>/", views.listDel, name="rsplistdel"),

        # tests
    path("rasp/gen/", views.genRaspPers, name="rspgen"),
    path("rasp/test/", views.test, name="rsptest"),

    # auth
    path("login/", views.login, name="login"),

]
