from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_task, name='addtask_view'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/complete/<int:task_id>/', views.complete_task, name='complete_task'),
]
