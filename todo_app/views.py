from django.shortcuts import render
from .models import TaskModel


# Create your views here.
def show_todolist(request):
	tasks = TaskModel.objects.all()
	return render(request, "todo_app/home.html", {'tasks': tasks})
