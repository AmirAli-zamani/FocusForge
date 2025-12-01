from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import JsonResponse


from ..models import PomodoroSession
from ..forms import PomodoroSessionForm
from Task_Management_Module.models import Task


@login_required
def session_list(request):
    sessions = PomodoroSession.objects.filter(user=request.user).order_by("-start_time")
    tasks = Task.objects.filter(owner=request.user)  # ✅ الان Task شناسایی میشه
    return render(request, "pomodoro/session_list.html", {"sessions": sessions, "tasks": tasks})

@login_required
def session_create(request):
    if request.method == "POST":
        form = PomodoroSessionForm(request.POST, user=request.user)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.save()
            return redirect("pomodoro_engine_module:session_list")
        else:
            print("FORM ERRORS:", form.errors)  # موقت برای دیباگ
    else:
        form = PomodoroSessionForm(user=request.user)

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

    # اگر AJAX بود، JSON بده
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': session.status})

    # اگر معمولی بود، redirect کن
    return redirect(request.META.get('HTTP_REFERER', 'pomodoro_engine_module:session_list'))



@login_required
def session_complete(request, pk):
    session = PomodoroSession.objects.get(pk=pk, user=request.user)
    session.status = "completed"
    session.end_time = timezone.now()
    diff = session.end_time - session.start_time
    session.actual_duration_seconds = int(diff.total_seconds())
    session.save()
    return redirect("pomodoro_engine_module:session_list")



@login_required
def start_session_for_task(request, task_id):
    from Task_Management_Module.models import Task
    from ..models import PomodoroSession
    from django.utils import timezone

    task = Task.objects.get(id=task_id, owner=request.user)

    # بررسی: آیا Session در حال اجرا روی این تسک هست؟
    existing_session = PomodoroSession.objects.filter(
        user=request.user, task=task, status="running"
    ).first()

    if existing_session:
        # اگر Session فعال هست، مستقیم به صفحه run هدایت کن
        return redirect("pomodoro_engine_module:session_run", session_id=existing_session.id)
    
    # اگر Session فعالی نبود، یک Session جدید بساز
    session = PomodoroSession.objects.create(
        user=request.user,
        task=task,
        start_time=timezone.now(),
        duration_minutes=task.default_duration if hasattr(task, 'default_duration') else 25,
        status="running"
    )
    return redirect("pomodoro_engine_module:session_run", session_id=session.id)



@login_required
def session_run(request, session_id):
    session = PomodoroSession.objects.get(id=session_id, user=request.user)
    return render(request, "pomodoro/session_run.html", {"session": session})


@login_required
def session_delete(request, session_id):
    session = PomodoroSession.objects.get(id=session_id, user=request.user)
    if request.method == "POST":
        session.delete()
        return redirect("pomodoro_engine_module:session_list")
    return redirect("pomodoro_engine_module:session_list")
