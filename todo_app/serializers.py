from rest_framework import serializers
from .models import TaskModel


class TaskSerializers(serializers.ModelSerializer):
	deadline = serializers.DateTimeField(format='%B %d, %Y, %I:%M, %p')
	created = serializers.DateTimeField(format='%B %d, %Y, %I:%M, %p', read_only=True)
	edited = serializers.DateTimeField(format='%B %d, %Y, %I:%M, %p', read_only=True)

	class Meta:
		model = TaskModel
		fields = ['id', 'task_name', 'description', 'priority',
		          'deadline', 'status', 'created', 'edited']
