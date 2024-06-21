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


class DeleteTaskView(generic.DeleteView):
	model = TaskModel
	success_url = reverse_lazy('home')
