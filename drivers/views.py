from django.shortcuts import render, redirect
from drivers.models import Drivers
from django.utils import timezone
from account_profile.models import Account_profile
from django.http import HttpResponse

def drivers(request):
	drivers_list = Drivers.objects.order_by('-reg_date')
	if request.user.is_authenticated:
		current_user = request.user.username
		current_user_info = Account_profile.objects.get(login = current_user)
	else:
		current_user_info = []
	accounts_info = Account_profile.objects.all()
	return render(request, 'drivers/drivers.html', {'page': 'drivers', 'user_info': current_user_info, 'drivers_list': drivers_list, 'accounts_info': accounts_info})

def driver_reg(request):
	if request.user.is_authenticated:
		current_user = request.user.username
		current_user_info = Account_profile.objects.get(login = current_user)
	else:
		return redirect('/accounts/login')

	drivers = Drivers.objects.all()
	for driver in drivers:
		if current_user_info.login == driver.login:
			return render(request, 'main/includes/error.html', {'error_title': 'У вас уже создан профиль гонщика!', 'error_text': 'У каждого созданного аккаунта не может быть более одного профиля гонщика!'})
	for driver in drivers:
		if current_user_info.driving_license == 'True':
			return redirect('/drivers/register/reg_result')
		elif current_user_info.driving_license == 'False':
			return render(request, 'main/includes/error.html', {'error_title': 'У вас нет прав!', 'error_text': 'Для того, чтобы зарегестрировать свой профиль у вас должны быть права!<br>Если у вас есть права, то укажите это в разделе "Профиль"',})
		else:
			return render(request, 'main/includes/error.html', {'error_title': 'Упс! Что-то пошло не так!', 'error_text': 'При повторении ошибки свяжитесь с техподдержкой "..."',})

def reg_result(request):
	if request.user.is_authenticated:
		current_user = request.user.username
		current_user_info = Account_profile.objects.get(login = current_user)
	else:
		current_user_info = []
	login = current_user_info.login

	a = Drivers(login = login, reg_date = timezone.now(), status = False)
	a.save()

	return render(request, 'drivers/reg_result.html')