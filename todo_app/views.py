from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskModel
from .forms import TaskModelForm
from django.views import generic


# Create your views here.
class ReadTaskView(generic.ListView):
	template_name = 'todo_app/home.html'
	context_object_name = "tasks"

	def get_queryset(self):
		return TaskModel.objects.all()


def create_task(request):  # Create a single task
	if request.method == 'POST':
		form = TaskModelForm(request.POST)
		if form.is_valid():  # Handle validation of user data
			form.save()
			return redirect('home')  # redirect to read_task
	else:
		form = TaskModelForm()  # render the form
	return render(request, 'todo_app/create_task.html', {'form': form})


def update_task(request, task_id):
	task = get_object_or_404(TaskModel, pk=task_id)
	if request.method == 'POST':
		form = TaskModelForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = TaskModelForm(instance=task)
	return render(request, 'todo_app/update_task.html', {'form': form})


def delete_task(request, task_id):
	TaskModel.objects.filter(id=task_id).delete()
	return redirect('home')
