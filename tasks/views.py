from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Task

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')

        if title and description:
            Task.objects.create(
                title=title,
                description=description,
                created_at=due_date or timezone.now()
            )
            messages.success(request, "Task added successfully!")
            return redirect('task_list')  
        else:
            messages.error(request, "Please fill all required fields!")

    return render(request, 'addtask.html')


def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')  
    return render(request, 'task_list.html', {'tasks': tasks})


def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.complete_task = True
    task.save()
    messages.success(request, f"Task '{task.title}' marked as completed!")
    return redirect('task_list')
