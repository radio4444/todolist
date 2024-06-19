from django.db import models


# Create your models here.
class TaskModel(models.Model):
	PRIORITY_CHOICES = {
		'Low': 'Low',
		'Medium': 'Medium',
		'High': 'High'
	}
	STATUS_CHOICES = {
		'Not started': 'Not started',
		'In Progress': 'In progress',
		'Complete': 'Complete'
	}

	task_name = models.CharField(max_length=200)
	description = models.CharField(max_length=400, blank=True)
	priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES)
	deadline = models.DateTimeField()
	status = models.CharField(max_length=11, choices=STATUS_CHOICES)
	created = models.DateTimeField(auto_now_add=True)
	edited = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.task_name
