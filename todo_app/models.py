from django.db import models


# Create your models here.
class TodoItem(models.Model):
	PRIORITY_CHOICES = {
		'low': 'Low',
		'med': 'Medium',
		'high': 'High'
	}
	STATUS_CHOICES = {
		'not started': 'Not started',
		'in progress': 'In progress',
		'complete': 'Complete'
	}

	task = models.CharField(max_length=200)
	description = models.CharField(max_length=400, blank=True)
	priority = models.CharField(max_length=4, choices=PRIORITY_CHOICES)
	deadline = models.DateTimeField()
	status = models.CharField(max_length=11, choices=STATUS_CHOICES)
	created = models.DateTimeField(auto_now_add=True)
	edited = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.task
