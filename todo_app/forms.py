from django import forms
from .models import TaskModel


class TaskModelForm(forms.ModelForm):
	class Meta:
		model = TaskModel
		fields = ['task_name', 'description', 'priority',
		          'deadline', 'status']
		# widgets = {
		# 	'deadline': forms.DateInput(attrs={'type': 'date'})
		# }
		widgets = {
			'task_name': forms.TextInput(attrs={'class': 'form-control'}),
			'description': forms.Textarea(attrs={'class': 'form-control'}),
			'priority': forms.Select(attrs={'class': 'form-control'}),
			'deadline': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
			'status': forms.Select(attrs={'class': 'form-control'}),
		}
