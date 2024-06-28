from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from . import views, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    # path('grid/', views.grid, name='grid'),
    path('mess/', include('mess.urls'), name='mess'),
    path('alert/', include('alert.urls'), name='alert'),
    path('aud/', include('aud.urls'), name='aud'),
    path('grpp/', include('grpp.urls'), name='grpp'),
    path('person/', include('person.urls'), name='person'),
    path('predmet/', include('predmet.urls'), name="predmet"),
    path('rasp/', include('rasp.urls'), name='rasp'),

    path('test/', views.test, name='test'),

    re_path(r'^api/person/$', views.person_list),
    re_path(r'^api/person/(\d+)$', views.person_detail),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
