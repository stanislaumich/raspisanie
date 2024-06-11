from django.contrib import admin
from django.urls import path, re_path, include

import predmet
from predmet import views

urlpatterns = [
    # rasp for predmet
    path('', views.indexPredmet, name="predmetindex"),
    path("<int:id>/", views.detailPredmet, name="predmetdetail"),
    path("<int:id>/<int:wd>/", views.predmetRasp, name="predmetrasp"),

    path("predmetaddall/", views.AddPredmetAll.as_view(), name="predmetaddall"),
    path("predmetdelall/<int:pk>/", views.DelPredmetAll.as_view(), name="predmetdelall"),

    path("listadd/", views.predmetadd, name="predmetlistadd"),
    path("listdel/<int:id>/", views.predmetdel, name="predmetlistdel"),
]
