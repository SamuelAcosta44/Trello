from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.getTasks),
    path('task/create/', views.addTask),
]