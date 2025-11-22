from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Task, Category
from ..forms import TaskForm

@login_required
def task_list(request):
    tasks = Task.objects.filter(owner=request.user).order_by("-created_at")
    return render(request, "tasks/task_list.html", {"tasks": tasks})


@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect("task_management_module:task_list")

    else:
        form = TaskForm()

    return render(request, "tasks/task_form.html", {"form": form})


@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id, owner=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_management_module:task_list")

    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/task_form.html", {"form": form})


@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, owner=request.user)
    task.delete()
    return redirect("task_management_module:task_list")
