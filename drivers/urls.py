from django.urls import path, include
from django.views.generic import ListView, DetailView
from . import views

urlpatterns = [
	path('', views.drivers, name="drivers"),
	path('register/', views.driver_reg, name="driver_reg"),
	path('register/reg_result', views.reg_result, name="reg_result"),
]