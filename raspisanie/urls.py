from django.contrib import admin
from django.urls import path, re_path, include
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    # path('grid/', views.grid, name='grid'),
    path('mess/', include('mess.urls'), name='mess'),
    path('alert/', include('alert.urls'), name='alert'),
    path('aud/', include('aud.urls'), name='aud'),
    path('grp/', include('grp.urls'), name='grp'),
    path('person/', include('person.urls'), name='person'),
    path('predmet/', include('predmet.urls'), name="predmet"),
    path('rasp/', include('rasp.urls'), name='rasp'),

]
