from rest_framework import serializers
from .models import Task, Priority

class TaskSerializer(serializers.ModelSerializer):
    priority = serializers.PrimaryKeyRelatedField(queryset=Priority.objects.all())

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'deadline', 'comment', 'status', 'priority']
    