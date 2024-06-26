from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskAPIViewSet)

urlpatterns = [
	path('', views.ReadTaskView.as_view(), name='home'),
	path('create/', views.CreateTaskView.as_view(), name='create'),
	path('update/<int:pk>/', views.UpdateTaskView.as_view(), name='update'),
	path('delete/<int:pk>/', views.DeleteTaskView.as_view(), name='delete'),
	path('api/', include(router.urls), name='api'),
	path('ajax/', views.ajax_index, name='ajax'),
]
