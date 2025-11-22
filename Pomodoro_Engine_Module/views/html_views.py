from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

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
            return redirect("pomodoro_engine_module:session_list")
    else:
        form = PomodoroSessionForm()
    return render(request, "pomodoro/session_create.html", {"form": form})

@login_required
def update_session(request, session_id):
    session = PomodoroSession.objects.get(id=session_id, user=request.user)

    action = request.POST.get("action")
    if action == "pause":
        session.status = "paused"
    elif action == "resume":
        session.status = "running"
    elif action == "stop":
        session.status = "completed"
        session.end_time = timezone.now()
        diff = session.end_time - session.start_time
        session.actual_duration_seconds = int(diff.total_seconds())

    session.save()
    return redirect("pomodoro_engine_module:session_run", session_id=session.id)



@login_required
def session_complete(request, pk):
    session = PomodoroSession.objects.get(pk=pk, user=request.user)
    session.status = "completed"
    session.end_time = timezone.now()
    session.save()
    return redirect("pomodoro_engine_module:session_list")



def start_session(request):
    session = PomodoroSession.objects.create(
        user=request.user,
        start_time=timezone.now(),
        status="running"
    )
    return redirect("pomodoro_engine_module:session_run", session.id)


@login_required
def session_run(request, session_id):
    session = PomodoroSession.objects.get(id=session_id, user=request.user)
    return render(request, "pomodoro/session_run.html", {"session": session})
