from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import UpdateView

from person import views


urlpatterns = [
    # rasp for person
    path("", views.indexPerson, name="personindex"),
    path("<int:id>/", views.detailPerson, name="persondetail"),
    path("<int:id>/<int:wd>/", views.detailRaspPers, name="rspperson"),

    path("add/<int:id>/", views.addRaspPers, name="rspadd"),
    path("edit/<int:id>/", views.editRaspPers, name="rspedit"), #   <int:id>/ UpdateView.as_view
    path("edit2/<int:pk>/", views.EditRaspPers.as_view(), name="rspedit2"), #   <int:id>/ UpdateView.as_view

    path("del/<int:id>/", views.delRaspPers, name="rspdel"),

    path("listadd/", views.listAdd, name="rsplistadd"),
    path("listdel/<int:id>/", views.listDel, name="rsplistdel"),
    # auth
    path("login/", views.login, name="login"),
    path("badlogin/", views.badlogin, name="badlogin"),
    path("logout/", views.logout, name="logout"),

    path("delreserv/<int:id>/", views.delRaspPersReserv, name="rspdelreserv"),
    path("addreserv/<int:id>/", views.addRaspPersReserv, name="rspaddreserv"),
]
