from django.contrib import admin

# Register your models here.
from .models import TodoItem


class TodoItemAdmin(admin.ModelAdmin):
	list_display = ['task', 'description', 'priority', 'deadline', 'status', 'created', 'edited']


admin.site.register(TodoItem, TodoItemAdmin)
