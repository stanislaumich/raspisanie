from django.urls import path, re_path, include

from . import views

# rasp for groups
urlpatterns = [
path("", views.indexGrp, name="grpindex"),
path("<int:id>/", views.detailGrp, name="grpdetail"),

path("<int:id>/<int:wd>/", views.detailRaspGroup, name="grpdetailrasp"),
path("add/", views.grpadd, name="grpadd"),
path("edit/<int:id>/", views.editRaspGroup, name="grpedit"),
path("del/<int:id>/", views.grpdel, name="grpdel"),

]
