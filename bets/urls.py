from django.urls import path, include
from django.views.generic import ListView, DetailView
from . import views

urlpatterns = [
	path('', views.bets, name="bets"),
	path('bet_confirm/', views.bet_confirm, name="bet_confirm"),
	path('bet_confirm/bet_result/', views.bet_result, name="bet_result"),
	path('bet_confirm/bet_result/accept/', views.accept, name="accept"),
]