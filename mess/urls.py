from django.contrib import admin
from django.urls import path, re_path, include

from .import views

urlpatterns = [
# rasp for mess
    path("clear/<int:id>/", views.messClear, name="messclear"),
    path("send/<int:id>/", views.messSend, name="messsend"),
]