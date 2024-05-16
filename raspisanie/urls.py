from django.contrib import admin
from django.urls import path, re_path, include
#from aud import views
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('grid/', views.grid, name='grid'),
    path('predmet/', include('predmet.urls')),
    path("person/", include('person.urls')),
	path("aud/", include('aud.urls')),
    path("grp/", include('grp.urls')),
]
