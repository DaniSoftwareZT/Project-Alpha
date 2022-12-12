from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from django.contrib.auth.decorators import login_required
from .forms import CreateProjectForm

# Create your views here.


@login_required
def list_projects(request):
    list_projects = Project.objects.filter(owner=request.user)
    context = {"list_projects": list_projects}
    return render(request, "projects/list.html", context)


@login_required
def show_project(request, id):
    show_project = get_object_or_404(Project, id=id)
    context = {"show_project": show_project}
    return render(request, "projects/detail.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            projects = form.save(commit=False)
            projects.owner = request.user
            projects.save()
            return redirect("list_projects")
    else:
        form = CreateProjectForm()
    context = {"form": form}
    return render(request, "projects/create.html", context)
