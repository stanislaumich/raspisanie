#<int:id>/
from . import views
from django.urls import path, re_path, include
app_name = 'person'
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    #path('about', views.about),
    #path('aud', audviews.aud),
    path("<int:id>/", views.detail, name='detail'),
	#path("aud/", include('aud.urls')),
]