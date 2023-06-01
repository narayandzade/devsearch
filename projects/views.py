from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    page = "projects"
    page_id = 3444
    context = { "page":page, "page_id":page_id }
    return render(request, 'projects/projects.html', context)

def project(request, pk):

    context= {"pk": pk}
    return render(request, 'projects/project.html', context)
