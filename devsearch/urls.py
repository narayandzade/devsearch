from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def index(request):
    return HttpResponse("Home Page")

def projects(request):
    return HttpResponse("Here are our projects")

def project(request):
    return HttpResponse("Single Project")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('projects/', projects, name="projects"),
    path('project/', project, name="project"),
]
