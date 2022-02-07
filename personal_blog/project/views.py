from django.shortcuts import render

from personal_blog.project.models import Project


def index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects/index.html", context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project": project
    }
    return render(request, "projects/project_detail.html", context)
