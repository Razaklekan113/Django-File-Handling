from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_form, name='upload_form'),
    path('list/', views.list_files, name='list_files'),
    path('delete/<int:pk>/', views.delete_file, name='delete_file'),
]