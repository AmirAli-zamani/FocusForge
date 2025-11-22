from django.db import models
from django.utils import timezone
from User_Authentication_Module.models import CustomUser
from Pomodoro_Engine_Module.models import PomodoroSession
from Task_Management_Module.models import Task


class DailyReport(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    tasks_completed = models.IntegerField(default=0)
    pomodoros_completed = models.IntegerField(default=0)
    productivity_score = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.username} - {self.date}"

    def generate_for_date(self, report_date=None):
        if report_date is None:
            report_date = timezone.localdate()

        # Count completed tasks
        self.tasks_completed = Task.objects.filter(
            user=self.user, 
            is_completed=True,
            completed_at__date=report_date
        ).count()

        # Count completed pomodoro sessions
        self.pomodoros_completed = PomodoroSession.objects.filter(
            user=self.user, 
            status="completed", 
            end_time__date=report_date
        ).count()

        # Simple productivity score
        self.productivity_score = self.tasks_completed * 1.5 + self.pomodoros_completed
        self.date = report_date
        self.save()
