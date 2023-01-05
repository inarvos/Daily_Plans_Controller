from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
import datetime
from schedule.models import Task

# Create your views here.

def practice(request):
    return render(request, 'practice.html', {'curr_date':datetime.datetime.now()})

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
