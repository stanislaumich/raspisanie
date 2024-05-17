from django.contrib import admin
from django.urls import path, re_path, include
#from aud import views
from .import views
urlpatterns = [
    path('predmet/', views.indexPredmet, name="predmet"),
    path("person/", views.indexPerson, name="person"),
	path("aud/", views.indexAud, name="aud"),
    path("aud/<int:id>/", views.detailAud, name="aud"),
    path("grp/", views.indexGrp, name="grp"),
]