from django.db import models
from taskcollection.models import TaskCollection
from enum import Enum

# Create your models here.
class ToDo(models.Model):
    collection = models.ForeignKey(TaskCollection, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title