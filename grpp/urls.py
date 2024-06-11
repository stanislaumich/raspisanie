from django.urls import path
from . import views

# rasp for groups
urlpatterns = [
path("", views.indexGrp, name="grpindex"),
path("<int:id>/", views.detailGrp, name="grpdetail"),

path("<int:id>/<int:wd>/", views.detailRaspGroup, name="grpdetailrasp"),

path("grpaddall/", views.AddGrpAll.as_view(), name="grpaddall"),
path("grpdelall/<int:pk>/", views.DelGrpAll.as_view(), name="grpdelall"),

path("add/", views.grpadd, name="grpadd"),
path("del/<int:id>/", views.grpdel, name="grpdel"),

]
