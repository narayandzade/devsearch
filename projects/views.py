from django.shortcuts import render, redirect
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
     if request.method == "POST":
         form = ProjectForm(request.POST, request.FILES)
         if form.is_valid():
             project = form.save(commit=False)
             project.featured_image = form.cleaned_data['featured_image']
             #form.save()
             project.save()
             return redirect('projects')
     
     context={'form': form}
     return render(request,'projects/add_project.html',context ) 

def updateProject(request, id):
    single_project = Project.objects.get(id=id)
    form = ProjectForm(instance=single_project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=single_project)
        if form.is_valid():
            project = form.save(commit=False)
            project.featured_image = form.cleaned_data['featured_image']
            #form.save()
            project.save()
            return redirect('projects')
    context={'form': form}
    return render(request,'projects/add_project.html',context ) 

def deleteProject(request, id):
    project = Project.objects.get(id=id)
    if request.method == "POST":
        project.delete()
        return redirect("projects")
    context ={'project':project}
    return render(request, 'projects/delete_form.html', context)