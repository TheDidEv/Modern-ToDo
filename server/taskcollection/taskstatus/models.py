from taskcollection.models import TaskCollection

from django.db import models

class TaskStatus(models.Model):
    collection = models.ForeignKey(TaskCollection, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)