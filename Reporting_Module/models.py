from django.db import models
from User_Authentication_Module.models import CustomUser

class DailyReport(models.Model):
    # User related to this report
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    # Report date
    date = models.DateField()

    # How many tasks were completed today
    tasks_completed = models.IntegerField(default=0)

    # How many pomodoro sessions completed
    pomodoros_completed = models.IntegerField(default=0)

    # Calculated productivity score
    productivity_score = models.FloatField(default=0.0)
