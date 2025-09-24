from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200, default="Untitled Task")
    description = models.TextField(default="No description")  
    created_at = models.DateField(default=timezone.now)  
    complete_task = models.BooleanField(default=False)

    def __str__(self):
        return self.title
