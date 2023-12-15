from django.urls import path
from . import views

urlpatterns = [
    path('', views.getTasks),
    path('create/', views.addTask),
    path('update/<str:pk>/', views.updateTask),
    path('fix/<str:pk>/', views.patchTask),
]