from django.contrib import admin

# Register your models here.
from .models import TaskModel


class TaskModelAdmin(admin.ModelAdmin):
	list_display = ['task_name', 'description', 'priority', 'deadline', 'status', 'created', 'edited']


admin.site.register(TaskModel, TaskModelAdmin)
