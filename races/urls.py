from django.urls import path, include
from django.views.generic import ListView, DetailView
from . import views

urlpatterns = [
	path('', views.races, name="races"),
	path('register/', views.register, name="register"),
]