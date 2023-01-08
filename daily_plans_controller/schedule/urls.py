from . import views
import schedule.views as views
from django.urls import path

urlpatterns = [
    path('tasks1', views.tasks, name='tasks1'),
    path('tasks', views.TaskListView.as_view(), name='tasks'),
    path('events', views.EventListView.as_view(), name='events'),
    path('reminders', views.ReminderListView.as_view(), name='reminders'),
]
