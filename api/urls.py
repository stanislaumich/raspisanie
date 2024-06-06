from django.urls import path

from api import views

urlpatterns = [
    # rasp for person
    path("", views.apiIndex, name="apiindex"),
    # auth
    path("login/", views.apiLogin, name="apilogin"),
    path("logout/", views.apiLogout, name="apilogout"),
]