from django.contrib import admin
from .models import Notification, Task, Event

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'parent', 'deadline', 'postponed', 'deadline_reminder', 'postponed_reminder', 'done')
    list_display = ['parent', 'id', 'name', 'description', 'deadline', 'postponed', 'deadline_reminder', 'postponed_reminder', 'done']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'repeatable', 'description', 'start_date', 'duration', 'reminder') 
    list_display = ['id', 'name', 'repeatable', 'description', 'start_date', 'duration', 'reminder', 'end_date']
