from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import UpdateView

from person import views
from . import views
from .forms import EditPhoto

urlpatterns = [
    # rasp for person
    path("", views.indexPerson, name="personindex"),
    path("<int:id>/", views.detailPerson, name="persondetail"),
    path("<int:id>/<int:wd>/", views.detailRaspPers, name="rspperson"),

    # path("add/<int:id>/", views.addRaspPers, name="rspadd"),
    # path("edit2/<int:id>/", views.editRaspPers, name="rspedit2"), #   <int:id>/ UpdateView.as_view
    # path("edit/<int:pk>/", views.EditRasp.as_view(), name="rspedit"), #   <int:id>/ UpdateView.as_view
    # path("del/<int:pk>/", views.DelRasp.as_view(), name="rspdel"), #   <int:id>/ DeleteView.as_view

    # path("del2/<int:id>/", views.delRaspPers, name="rspdel2"),

    path("listadd/", views.listAdd, name="rsplistadd"),
    path("listdel/<int:id>/", views.listDel, name="rsplistdel"),
    # auth
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("badlogin/", views.badlogin, name="badlogin"),
    path("logout/", views.logout, name="logout"),
    path("profile/<int:id>/", views.profilePers, name="profile"),
    path("profilephoto/<int:pk>", EditPhoto.as_view(), name="profilephoto"),

    path("delreserv/<int:id>/", views.delRaspPersReserv, name="rspdelreserv"),
    path("addreserv/<int:id>/", views.addRaspPersReserv, name="rspaddreserv"),
]
