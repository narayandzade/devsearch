from django.shortcuts import render
from .models import Profiles

def profiles(request):
    profiles = Profiles.objects.all()
    context = {'profiles':profiles}
    return render(request, 'users/profiles.html', context)

def profile(request, id):
    profile = Profiles.objects.get(id=id)
    top_skills = profile.skill_set.exclude(description="")
    other_skills = profile.skill_set.filter(description="")
    
    context = {'profile':profile, 'top_skills':top_skills, 'other_skills':other_skills}
    return render(request, 'users/profile.html', context)