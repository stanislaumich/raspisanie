from django.contrib import admin
from django.urls import path, re_path, include

from .import views

urlpatterns = [
#common
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
# rasp for person
    path("rasp/person/<int:id>/<int:wd>/", views.detailRaspPers, name="rspperson"),
    path("rasp/person/add/<int:id>/", views.addRaspPers, name="rspadd"),
    path("rasp/person/edit/<int:id>/", views.editRaspPers, name="rspedit"),
    path("rasp/person/del/<int:id>/", views.delRaspPers, name="rspdel"),
# rasp for groups
    path("rasp/group/<int:id>/<int:wd>/", views.detailRaspGroup, name="rspgroup"),
    path("rasp/group/add/<int:id>/", views.addRaspGroup, name="rspaddgroup"),
    path("rasp/group/edit/<int:id>/", views.editRaspGroup, name="rspeditgroup"),
    path("rasp/group/del/<int:id>/", views.delRaspGroup, name="rspdelgroup"),
# rasp for aud
    path("rasp/aud/<int:id>/<int:wd>/", views.detailRaspAud, name="rspaud"),
# tests
    path("rasp/gen/", views.genRaspPers, name="rspgen"),
    path("rasp/test/", views.test, name="rsptest"),
# auth
    path("login/", views.login, name="login"),

]