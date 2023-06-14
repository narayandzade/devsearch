from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.profiles, name="profiles"),
    path('profile/<str:id>/', views.profile, name="profile")
]
