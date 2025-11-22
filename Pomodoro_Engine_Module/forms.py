from django import forms
from .models import PomodoroSession
from Task_Management_Module.models import Task

class PomodoroSessionForm(forms.ModelForm):
    class Meta:
        model = PomodoroSession
        fields = ["task", "start_time", "end_time", "status", "duration_minutes"]
        widgets = {
            "start_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "end_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None) 
        super().__init__(*args, **kwargs)
        if user:
            # فقط تسک‌های کاربر جاری
            self.fields["task"].queryset = Task.objects.filter(owner=user)
        # اختیاری بودن end_time
        self.fields["end_time"].required = False
