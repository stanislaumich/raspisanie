from django.contrib import admin
from django.urls import path, re_path, include
#from rasp import views
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('grid/', views.grid, name='grid'),
    path('rasp/', include('rasp.urls'), name='rasp'),#include('rasp.urls')

]
