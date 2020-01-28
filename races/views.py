from django.shortcuts import render, redirect
from races.models import Race
from account_profile.models import Account_profile
from .models import Race
from drivers.models import Drivers
from bets.models import Stake
from django.utils import timezone

def races(request):
	races_list = Race.objects.order_by('-time_date')
	if request.user.is_authenticated:
		current_user = request.user.username
		current_user_info = Account_profile.objects.get(login = current_user)
	else:
		current_user_info = []

	bets = Stake.objects.all()
	for race in races_list:
		bets_count = 0
		for bet in bets:
			if bet.status == 'True' and bet.race_name == race.race_name:
				bets_count += 1
		Race.objects.filter(race_name = race.race_name).update(stakes = bets_count)

	drivers = Drivers.objects.all()
	for race in races_list:
		drivers_count = 0
		for driver in drivers:
			acc = Account_profile.objects.get(login = driver.login)
			if driver.status == 'True' and acc.account_name in race.driver_list:
				drivers_count += 1
		Race.objects.filter(race_name = race.race_name).update(drivers = drivers_count)

	for race in races_list:
		bets_total = 0
		for bet in bets:
			if bet.status == 'True' and bet.race_name == race.race_name:
				bets_total += bet.stake
		Race.objects.filter(race_name = race.race_name).update(jackpot = bets_total)

	for race in races_list:
		time_before_race = str(race.time_date - timezone.now())
		time_before_race = time_before_race[:-7]
		if time_before_race[0] == 0 or time_before_race[0] == '-':
			Race.objects.filter(race_name = race.race_name).update(race_past = 'True')
		Race.objects.filter(race_name = race.race_name).update(time_before_race = time_before_race)

	races_list = Race.objects.order_by('-time_date')

	return render(request, 'races/races.html', {
		'page': 'races', 
		'user_info': current_user_info, 
		'races_list': races_list,
		})

def register(request):
	race_name = request.POST['name']
	race_info = Race.objects.get(race_name = race_name)
	if request.user.is_authenticated:
		current_user = request.user.username
		current_user_info = Account_profile.objects.get(login = current_user)
	else:
		current_user_info = []
	driver_check = Drivers.objects.get(login = current_user)
	if driver_check:
		if driver_check.status == 'True':
			if driver_check.login not in race_info.driver_list:
				drivers_registered = race_info.driver_list
				x = race_info.driver_list.split('\n')
				drivers_amount = len(x)
				drivers_registered += current_user_info.account_name + ' ' + current_user_info.account_surname + '|'

				return redirect('/races')
		else:
			return redirect('/races')