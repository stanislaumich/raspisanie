from django.urls import path, re_path, include

from . import views

# rasp for groups
urlpatterns = [
path("", views.indexGrp, name="grpindex"),
path("<int:id>/", views.detailGrp, name="grpdetail"),

path("<int:id>/<int:wd>/", views.detailRaspGroup, name="grpdetailrasp"),

# path("editrasp/<int:id>/", views.editRaspGroup, name="grpeditrasp"),
# path("addrasp/<int:id>/", views.addRaspGroup, name="grpaddrasp"),

path("add/", views.grpadd, name="grpadd"),
path("del/<int:id>/", views.grpdel, name="grpdel"),

]
