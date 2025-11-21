from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import PomodoroSession
from ..forms import PomodoroSessionForm

@login_required
def session_list(request):
    sessions = PomodoroSession.objects.filter(user=request.user).order_by("-start_time")
    return render(request, "pomodoro/session_list.html", {"sessions": sessions})

@login_required
def session_create(request):
    if request.method == "POST":
        form = PomodoroSessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.save()
            return redirect("session_list")
    else:
        form = PomodoroSessionForm()
    return render(request, "pomodoro/session_form.html", {"form": form})
