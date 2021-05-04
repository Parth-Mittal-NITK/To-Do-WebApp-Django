from django.contrib import admin 
from django.urls import path 
from tasks import views

urlpatterns = [
    path("", views.index, name = 'index'),
    path("update_task/<int:myid>", views.update_task, name="update_task"),
    path("delete_task/<int:myid>", views.delete_task, name="delete_task"),
]