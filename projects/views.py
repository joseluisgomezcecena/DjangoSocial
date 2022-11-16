from django.shortcuts import render
from .models import Project


# Create your views here.
def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, project_id):
    project = Project.objects.get(id=project_id)
    tags = project.tags.all()
    return render(request, 'projects/single-project.html', {'project': project, 'tags': tags})


def create_project(request):
    context = {}
    return render(request, 'projects/project_form.html', context)
