from django.shortcuts import render
from account_profile.models import Account_profile

def index(request):
	if request.user.is_authenticated:
		current_user = request.user.username
		current_user_info = Account_profile.objects.get(login = current_user)
	else:
		current_user_info = []
	return render(request, 'main/homePage.html', {'page': 'main', 'user_info': current_user_info})