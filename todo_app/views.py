from django.shortcuts import render, redirect
from .models import TaskModel
from .forms import TaskModelForm


# Create your views here.
def read_task(request):  # shows the list of task item
	tasks = TaskModel.objects.all()
	return render(request, "todo_app/home.html", {'tasks': tasks})


def create_task(request):  # Create task
	if request.method == 'POST':
		form = TaskModelForm(request.POST)
		if form.is_valid():  # Handle validation of user data
			form.save()
			return redirect('home')  # redirect to read_task
	else:
		form = TaskModelForm()  # render the form
	return render(request, 'todo_app/create_task.html', {'form': form})
