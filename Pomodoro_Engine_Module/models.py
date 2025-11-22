from django.db import models
from User_Authentication_Module.models import CustomUser
from Task_Management_Module.models import Task

class PomodoroSession(models.Model):
    STATUS_CHOICES = [
        ("running", "Running"),
        ("paused", "Paused"),
        ("completed", "Completed"),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
    
    start_time = models.DateTimeField()
    
    end_time = models.DateTimeField(null=True, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="running")
    actual_duration_seconds = models.IntegerField(default=0)
    
    duration_minutes = models.IntegerField(default=25)

    def __str__(self):
        return f"{self.user.username} - {self.status}"
