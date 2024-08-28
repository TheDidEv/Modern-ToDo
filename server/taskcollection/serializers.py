from rest_framework import serializers
from .models import TaskCollection

class TaskCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCollection
        fields = ['id', 'user', 'title', 'create_at', 'update_at']