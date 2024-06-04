from django.contrib import admin
from django.urls import path, re_path, include

from . import views

urlpatterns = [
    # url for aud
    path("", views.indexAud, name="audindex"),
    path("<int:id>/", views.detailAud, name="auddetail"),
    path("<int:id>/<int:wd>/", views.detailRaspAud, name="audrasp"),

]
