from datetime import timezone
from events.models import Task

class NotificationService:

    def notify():
        Task.objects.filter(done=False and deadline>timezone.now())
