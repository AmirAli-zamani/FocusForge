from django.db import models
from User_Authentication_Module.models import CustomUser
from Task_Management_Module.models import Task

class PomodoroSession(models.Model):
    # The user performing the pomodoro session
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    # Optional link to a task
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)

    # Start time of the session
    start_time = models.DateTimeField()

    # End time (optional if session not finished)
    end_time = models.DateTimeField(null=True, blank=True)

    # Whether the session was completed
    is_completed = models.BooleanField(default=False)

    # Duration in minutes (default = 25)
    duration_minutes = models.IntegerField(default=25)
