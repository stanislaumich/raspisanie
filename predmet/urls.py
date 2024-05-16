#<int:id>/
from . import views
from django.urls import path, re_path, include
app_name = 'predmet'
urlpatterns = [
    path('', views.index, name='index'),
    path("<int:id>/", views.detail, name='detail'),
]