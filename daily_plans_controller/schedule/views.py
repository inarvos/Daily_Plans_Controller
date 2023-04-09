from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from schedule.models import Task, Event, Reminder
from django.urls import reverse_lazy

# Create your views here.

def tasks(request):
    tasks = [t for t in list(Task.objects.all())]
    return render(request, 'task/list.html', {'tasks':tasks})

class TaskListView(ListView):
    model = Task
    template_name = 'task/task_list.html'
    paginate_by = 10

    #def get_queryset(self, **kwargs):
        #tasks = [t for t in Task.objects.all()]
        #return Task.objects.all()

class EventListView(ListView):
    model = Event
    template_name = 'event/event_list.html'
    paginate_by = 10

    #def get_queryset(self, **kwargs):
        #events = [e for e in Event.objects.all()]
        #return Event.objects.all()

class EventDeleteView(DeleteView):
    model = Event
    #success_url = reverse_lazy('events')
    success_url = "/"
    template_name = 'event/event_confirm_delete.html'

    #def get(self, *args, **kwargs):
    #return self.delete(*args, **kwargs)

class ReminderListView(ListView):
    model = Reminder
    template_name = 'reminder/reminder_list.html'
    paginate_by = 10

    #def get_queryset(self, **kwargs):
        #reminders = [r for r in Reminder.objects.all()]
        #return Reminder.objects.all()
