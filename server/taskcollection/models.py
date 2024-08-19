from django.db import models
from django.contrib.auth.models import User

class TaskCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_collections')
    title = models.CharField(max_length=50)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title
