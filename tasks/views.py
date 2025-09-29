from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Task


def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')

        if title and description:
            if due_date and due_date < str(date.today()):
                return render(request, 'addtask.html', {
                    'error': " Cannot set previous date!",
                    'today': date.today()
                })


            Task.objects.create(
                title=title,
                description=description,
                created_at=timezone.now(),
                due_date=due_date if due_date else None
            )
            return redirect('task_list')

    return render(request, 'addtask.html', {'today': date.today()})


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        status = request.POST.get('status')

        if title and description:
            if due_date and due_date < str(date.today()):
                return render(request, 'update_task.html', {
                    'error': " Cannot set previous date!",
                    'today': date.today()
                })


            task.title = title
            task.description = description
            task.due_date = due_date if due_date else None
            task.complete_task = True if status == "on" else False
            task.save()
            return redirect('task_list')

    return render(request, 'update_task.html', {'task': task, 'today': date.today()})



def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    pending_count = Task.objects.all().filter(complete_task=False).count()
    today=date.today()
    return render(request, 'task_list.html', {'tasks': tasks,
                                                'pending_count':pending_count,
                                                'today':today})


def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.complete_task = True
    task.save()
    return redirect('task_list')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')




