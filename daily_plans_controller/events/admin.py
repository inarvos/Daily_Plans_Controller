from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'repeatable', 'description', 'start_date', 'duration') 
    list_display = ['id', 'name', 'repeatable', 'start_date', 'duration', 'end_date']
