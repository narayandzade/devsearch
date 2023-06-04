from django.shortcuts import render
from django.http import HttpResponse

from .models import Project

from .forms import ProjectForm



def projects(request):
    page = "projects"
    page_id = 3444
    projects= Project.objects.all()

    context = { "page":page, "page_id":page_id ,"projects": projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):

    projectObj= Project.objects.get(id=pk)
   
    return render(request, 'projects/project.html', {"project": projectObj})

def createProject(request):
     
     form = ProjectForm()
     context={'form': form}
     return render(request,'projects/add_project.html',context ) 

