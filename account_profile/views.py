from django.shortcuts import render, redirect
from .models import Account_profile
from bets.models import Stake
from races.models import Race
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import include, path
from django.core.files.storage import FileSystemStorage

def account_profile(request):
	if request.user.is_authenticated:
		current_user = request.user.username
		current_user_info = Account_profile.objects.get(login = current_user)
	else:
		return redirect('/accounts/login')

	races_list = Race.objects.order_by('-time_date')
	races_participated = 0
	upcoming_races = []
	races_past = []
	if current_user_info != []:
		for race in races_list:
			if current_user_info.account_name in race.driver_list and race.race_past == 'True':
				races_participated += 1
				races_past.append(race.race_name + ' (' + race.time_date.strftime("%d-%B-%Y %H:%M") + ')')
			if current_user_info.account_name in race.driver_list and race.race_past == 'False':
				upcoming_races.append(race.race_name + ' (' + race.time_date.strftime("%d-%B-%Y %H:%M") + ')')
			Account_profile.objects.filter(login = current_user_info.login).update(races_participated = races_participated)

	stakes = Stake.objects.all()
	jackpot = 0
	for stake in stakes:
		if stake.bet_code[:17] == 'Race_registration':
			jackpot += stake.stake
			Stake.objects.filter(bet_code = stake.bet_code).update(jackpot = jackpot)

	races_won = 0
	if current_user_info != []:
		for race in races_list:
			for stake in Stake.objects.filter(race_name = race.race_name):
				if race.time_date < timezone.now():
					if current_user_info.account_name in race.winner:
						Stake.objects.filter(bet_code = stake.bet_code).update(won = 'Won')
					else:
						Stake.objects.filter(bet_code = stake.bet_code).update(won = 'Lost')
				else:
					Stake.objects.filter(bet_code = stake.bet_code).update(won = 'Waiting')

			if current_user_info.account_name in race.winner:
				races_won += 1
			Account_profile.objects.filter(login = current_user_info.login).update(races_won = races_won)

		current_user_info = Account_profile.objects.get(login = current_user)

	transactions = Stake.objects.filter(name = current_user_info.account_name + ' ' + current_user_info.account_surname).order_by('-bet_date')
	return render(request, 'account_profile/account_profile.html', {
		'page': 'account_profile', 
		'user_info': current_user_info, 
		'notification': False,
		'upcoming_races': upcoming_races,
		'races_past': races_past,
		'transactions': transactions,})


def register(request):
	if request.user.is_authenticated:
		current_user = request.user.username
		current_user_info = Account_profile.objects.get(login = current_user)
	else:
		current_user_info = []
	if request.POST:
		if request.FILES:
			upload_file = request.FILES['account_pic_file']
			fs = FileSystemStorage()
			fs.save(upload_file.name, upload_file)
			account_pic = '/media/' + upload_file.name
		else:
			account_pic = request.POST['account_pic']

		account_name = request.POST['account_name']
		account_surname = request.POST['account_surname']
		login = request.POST['login']
		password = request.POST['password']
		password_repeat = request.POST['password_repeat']
		email = request.POST['email']
		about = request.POST['about']
		if request.POST['driving_license'] == 'yes':
			driving_license = True
		else:
			driving_license = False

		all_users = Account_profile.objects.all()
		users =[]
		for user in all_users:
			users.append(user.login)
		if login not in users:
			if password == password_repeat:
				a = Account_profile(
					account_name = account_name,
					account_surname = account_surname,
					login = login,
					password = password,
					email = email,
					account_create_date = timezone.now(),
					account_pic = account_pic,
					about = about,
					driving_license = driving_license)
				
				if account_pic == '':
					a = Account_profile(
					account_name = account_name,
					account_surname = account_surname,
					login = login,
					password = password,
					email = email,
					account_create_date = timezone.now(),
					about = about,
					driving_license = driving_license)
				a.save()

				user = User.objects.create_user(username = login, email = email, password = password, first_name = account_name, last_name = account_surname)

				return HttpResponseRedirect('/accounts/login')

	return render(request, 'account_profile/account_register.html', {'page': 'account_profile', 'user_info': current_user_info, 'notification': False})


def edit(request):
	if request.user.is_authenticated:
		current_user = request.user.username
		current_user_info = Account_profile.objects.get(login = current_user)

		if request.FILES:
			upload_file = request.FILES['account_pic_file']
			fs = FileSystemStorage()
			fs.save(upload_file.name, upload_file)
			img = '/media/' + upload_file.name
		else:
			img = request.POST['account_pic']

		if request.POST['driving_license'] == 'yes':
			driving_license = 'True'
		else:
			driving_license = 'False'

		about = request.POST['about']
		Account_profile.objects.filter(login = current_user).update(about = about, account_pic = img, driving_license = driving_license)
	else:
		current_user_info = []

	return HttpResponseRedirect('/account_profile')