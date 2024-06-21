from django.urls import path
from . import views

urlpatterns = [
	path('', views.ReadTaskView.as_view(), name='home'),
	path('create/', views.CreateTaskView.as_view(), name='create'),
	path('update/<int:task_id>/', views.update_task, name='update'),
	path('delete/<int:pk>/', views.DeleteTaskView.as_view(), name='delete')
]
