from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateTaskForm
from .models import Task

# Create your views here.


@login_required
def create_task(request):
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = CreateTaskForm()
    context = {"form": form}
    return render(request, "tasks/create.html", context)


@login_required
def show_my_tasks(request):
    show_my_tasks = Task.objects.filter(assignee=request.user)
    context = {"show_my_tasks": show_my_tasks}
    return render(request, "tasks/list.html", context)
