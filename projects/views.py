from django.shortcuts import render

# Create your views here.
def projects(request):
    return render(request, 'projects/projects.html')

def project(request, project_id):
    return render(request, 'projects/project.html')