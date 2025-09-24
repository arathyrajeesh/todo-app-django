from django.contrib import admin
from .models import Task  

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'complete_task')
    list_filter = ('complete_task',)
    search_fields = ('title', 'description')
