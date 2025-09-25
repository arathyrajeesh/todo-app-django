from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  
    path('add/', views.add_task, name='addtask_view'),
    path('tasks/complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('tasks/delete/<int:task_id>', views.delete_task, name='delete_task'),
    path('tasks/update/<int:task_id>', views.update_task, name='update_task'),

]

