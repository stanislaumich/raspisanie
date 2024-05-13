#<int:id>/
from . import views
from django.urls import path, re_path, include
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    #path('about', views.about),
    #path('aud', audviews.aud),
    path("<int:id>/", views.person),
	#path("aud/", include('aud.urls')),
]