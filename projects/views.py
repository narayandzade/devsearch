from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    page = "projects"
    page_id = 1
    context = { "page":page, "page_id":page_id }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    return render(request, 'projects/project.html', str(pk))
