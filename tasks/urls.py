from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ana sayfa URL'si
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/completed/', views.completed_tasks, name='completed_tasks'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/update/<int:task_id>/', views.task_update, name='task_update'),
    path('tasks/delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('tasks/toggle_complete/<int:task_id>/', views.task_toggle_complete, name='task_toggle_complete'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]
