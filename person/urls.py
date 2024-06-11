from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import UpdateView

from person import views
from . import views
from .forms import EditPhoto
from .views import EditNotePers, AddNotePers

urlpatterns = [
    # rasp for person
    path("", views.indexPerson, name="personindex"),
    path("<int:id>/", views.detailPerson, name="persondetail"),
    path("<int:id>/<int:wd>/", views.detailRaspPers, name="rspperson"),

    path("editnotepers/<int:pk>", EditNotePers.as_view(), name="editnotepers"),
    path("addnotepers/", AddNotePers.as_view(), name="addnotepers"),

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
