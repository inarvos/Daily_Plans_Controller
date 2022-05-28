from django.contrib import admin
from .models import Event, Task

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'repeatable', 'description', 'start_date', 'duration') 
    list_display = ['id', 'name', 'repeatable', 'start_date', 'duration', 'end_date']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'parent', 'deadline', 'done')
    list_display = ['parent', 'id', 'name', 'description', 'deadline', 'done']
