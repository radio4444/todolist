from django import forms
from .models import TaskModel


class TaskModelForm(forms.ModelForm):
	class Meta:
		model = TaskModel
		fields = ['task_name', 'description', 'priority',
		          'deadline', 'status']
		widgets = {
			'deadline': forms.DateInput(attrs={'type': 'date'})
		}
