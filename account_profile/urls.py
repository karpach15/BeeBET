from django.urls import path, include
from django.views.generic import ListView, DetailView
from . import views

urlpatterns = [
	path('', views.account_profile, name="account_profile"),
	path('register/', views.register, name="register"),
	path('edit/', views.edit, name="edit"),
]