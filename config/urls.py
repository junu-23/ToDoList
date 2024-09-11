from django.urls import path, include
from django.contrib import admin
from dodo import views


urlpatterns = [
    path('dodo/', include('dodo.urls')),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
