from . import views
import schedule.views as views
from django.urls import path

urlpatterns = [
    path('practice/', views.practice, name='practice'),
    path('tasks', views.tasks, name='tasks'),
    path('tasks2', views.TaskListView.as_view(), name='tasks2'),
]
