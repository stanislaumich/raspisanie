from . import views
from django.urls import path, re_path, include
app_name = 'grp'
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path("<int:id>/", views.detail, name='detail'),
]