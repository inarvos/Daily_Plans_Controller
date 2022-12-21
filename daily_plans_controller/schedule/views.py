from django.http.response import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def practice(request):
    return render(request, 'practice.html', {'curr_date':datetime.datetime.now()})
