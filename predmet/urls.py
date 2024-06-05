from django.contrib import admin
from django.urls import path, re_path, include

import predmet
from predmet import views

urlpatterns = [
    # rasp for predmet
    path('', views.indexPredmet, name="predmetindex"),
    path("<int:id>/", views.detailPredmet, name="predmetdetail"),
    path("<int:id>/<int:wd>/", views.predmetRasp, name="predmetrasp"),
    # path("add/<int:id>/", views.addRaspPredmet, name="predmetadd"),
    # path("edit/<int:id>/", views.editRaspPredmet, name="predmetedit"),
    # path("del/<int:id>/", views.delRaspPredmet, name="predmetdel"),
    path("listadd/", views.predmetadd, name="predmetlistadd"),
    path("listdel/<int:id>/", views.predmetdel, name="predmetlistdel"),
]
