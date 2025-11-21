from django import forms
from .models import PomodoroSession

class PomodoroSessionForm(forms.ModelForm):
    class Meta:
        model = PomodoroSession
        fields = ["task", "start_time", "end_time", "is_completed", "duration_minutes"]
        widgets = {
            "start_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "end_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
