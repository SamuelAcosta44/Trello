from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('tasks/', views.task_api_view, name='tasks'),
    path('tasks/status/<str:status>/', views.filter_by_status, name='filter-by-status'),
    path('tasks/date/<str:deadline>/', views.filter_by_deadline, name='filter-by-deadline'),
    path('tasks/name/<str:name>/', views.filter_by_name, name='filter-by-name'),
]