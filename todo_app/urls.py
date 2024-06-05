from django.urls import path
from . import views

urlpatterns = [
	path('', views.read_task, name='home'),
	path('create/', views.create_task, name='create'),
	path('update/<int:task_id>/', views.update_task, name='update'),
]
