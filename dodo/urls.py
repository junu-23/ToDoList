from django.urls import path
from . import views

app_name = 'dodo'

urlpatterns = [
    path('modify/<int:pk>', views.doit_modify, name='doit_modify'),
    path('delete/<int:pk>', views.doit_delete, name='doit_delete'),
    path('done/delete/<int:pk>', views.done_delete, name='done_delete'),
    path('create/', views.doit_create, name='doit_create'),
    path('', views.index, name='index'),
    path('<int:pk>/', views.DoitDetail, name='doit_detail'),
    path('done/', views.done_list, name='done_list'), #  완료 리스트
    path('done/<int:pk>/', views.doit_done, name='doit_done'),
    #  완료된 작업목록 보기
]