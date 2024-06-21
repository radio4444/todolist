from django.shortcuts import get_object_or_404
from .models import TaskModel
from .forms import TaskModelForm
from django.views import generic
from django.urls import reverse_lazy


# Create your views here.
class ReadTaskView(generic.ListView):
	# ListView to display all tasks from TaskModel
	template_name = 'todo_app/home.html'
	context_object_name = "tasks"

	def get_queryset(self):
		# Retrieve all tasks from TaskModel
		return TaskModel.objects.all()


class CreateTaskView(generic.CreateView):
	# CreateView for creating a single task
	form_class = TaskModelForm
	template_name = 'todo_app/create_task.html'
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		# Save the form data if it is valid
		form.save()
		return super().form_valid(form)


class UpdateTaskView(generic.UpdateView):
	# UpdateView for updating a single task
	model = TaskModel
	form_class = TaskModelForm
	template_name = 'todo_app/update_task.html'
	success_url = reverse_lazy('home')

	def get_object(self, queryset=None):
		# Use get_object_or_404 to fetch the object based on pk
		pk = self.kwargs.get('pk')
		return get_object_or_404(TaskModel, pk=pk)

	def form_valid(self, form):
		# Save the form data if it is valid
		form.save()
		return super().form_valid(form)


class DeleteTaskView(generic.DeleteView):
	# DeleteView for deleting a single task
	model = TaskModel
	success_url = reverse_lazy('home')

	def get_object(self, queryset=None):
		# Use get_object_or_404 to fetch the object based on pk
		pk = self.kwargs.get('pk')
		return get_object_or_404(TaskModel, pk=pk)
