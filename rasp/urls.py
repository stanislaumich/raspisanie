from django.contrib import admin
from django.urls import path, re_path, include

from rasp import views

urlpatterns = [
    #common
    path("", views.indexRasp, name="rspindex"),
    path("<int:id>/", views.detailRasp, name="rspdetail"),

    path("rspedit/<int:pk>/", views.EditRasp.as_view(), name="rspedit"),
    path("rspadd/", views.AddRasp.as_view(), name="rspadd"),
    path("rspdel/<int:pk>/", views.DelRasp.as_view(), name="rspdel"),
    path("rspclone/<int:id>/", views.clonerasp, name="rspclone"),


    path("rspxlspers/<int:id>/<int:wd>/", views.rspxlspers, name="rspxlspers"),



]
