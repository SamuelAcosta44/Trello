from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('tasks/', views.task_api_view, name='task-list'),
    path('<str:pk>/', views.task_api_view, name='task-detail'),
]