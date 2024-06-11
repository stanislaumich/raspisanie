from django.contrib import admin
from django.urls import path, re_path, include

from . import views

urlpatterns = [
    # url for aud
    path("", views.indexAud, name="audindex"),
    path("<int:id>/", views.detailAud, name="auddetail"),
    path("<int:id>/<int:wd>/", views.detailRaspAud, name="audrasp"),
    path("audadd/", views.audadd, name="audadd"),
    path("auddel/<int:id>/", views.auddel, name="auddel"),

    path("audaddall/", views.AddAudAll.as_view(), name="audaddall"),
    path("auddelall/<int:pk>/", views.DelAudAll.as_view(), name="auddelall"),

]
