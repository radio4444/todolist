from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskModel
from .forms import TaskModelForm
from django.views import generic
from django.urls import reverse_lazy


# Create your views here.
class ReadTaskView(generic.ListView):
	template_name = 'todo_app/home.html'
	context_object_name = "tasks"

	def get_queryset(self):
		return TaskModel.objects.all()


class CreateTaskView(generic.CreateView):
	form_class = TaskModelForm
	template_name = 'todo_app/create_task.html'
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)


class UpdateTaskView(generic.UpdateView):
	model = TaskModel
	form_class = TaskModelForm
	template_name = 'todo_app/update_task.html'
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)


class DeleteTaskView(generic.DeleteView):
	model = TaskModel
	success_url = reverse_lazy('home')
