from django.shortcuts import render, redirect
from drivers.models import Drivers
from races.models import Race
from account_profile.models import Account_profile
from bets.models import Stake
from django.utils import timezone
import math

def bets(request):
	if request.user.is_authenticated:
		current_user = request.user.username
		current_user_info = Account_profile.objects.get(login = current_user)
	else:
		current_user_info = []
	races_list = Race.objects.all()

	for race in races_list:
		time_before_race = str(race.time_date - timezone.now())
		time_before_race = time_before_race[:-10]
		Race.objects.filter(race_name = race.race_name).update(time_before_race = time_before_race)

	races_list = Race.objects.order_by('-time_date')

	return render(request, 'bets/bets.html', {'page': 'bets', 'user_info': current_user_info, 'races_list': races_list,})

def bet_confirm(request):
	races_list = Race.objects.all()
	races = []
	all_drivers = []
	races_winners = {}
	driver_stat = {}
	driver_coeficient = {}
	for race in races_list:
		races.append(race.race_name)
		names = race.race_result.split('|')
		for elem in names:
			if elem == '':
				names.remove('')
		for elem in names:
			all_drivers.append(elem)
			driver_stat.update({elem: 0})
		races_winners.update({race.race_name: names})

	points = 100
	all_driver_points = 0
	race_i = 0
	while race_i < len(races):
		drivers = races_winners[races[race_i]]
		if len(drivers) > 0:
			i = 0
			while i < len(driver_stat):
				all_driver_points += driver_stat[all_drivers[i]]
				i += 1
			points += all_driver_points
			
			amount_drivers = len(drivers)
			points_amount = math.ceil(1/3 * amount_drivers)
			points_step = math.ceil(5 / points_amount)

			points_for_race = 0
			i = 1
			while i <= points_amount:
				points_for_race += points_step * i
				i += 1
			total_points = points + points_for_race

			drivers_with_points = []
			i = 0
			while points_amount > 0:
				drivers_with_points.append(drivers[i])
				points_amount -= 1
				i += 1

			drivers_with_old_points = []
			i = 0
			while i < len(all_drivers):
				if driver_stat[all_drivers[i]] != 0:
					if all_drivers[i] not in drivers_with_points:
						drivers_with_old_points.append(all_drivers[i])
				i += 1
			drivers_no_points = amount_drivers - len(drivers_with_points) - len(drivers_with_old_points)

			i = 0
			points_left = len(drivers_with_points)
			chances = []
			while i < amount_drivers:
				chance = driver_stat[drivers[i]]
				if drivers[i] in drivers_with_points:
					driver_stat[drivers[i]] += points_step * points_left
					chance += (total_points / amount_drivers) + points_step * points_left
					points_left -= 1
				elif chance != 0:
					chance += (total_points / amount_drivers) + points_step * points_left
				else:
					x = total_points
					y = 0
					while y < len(chances):
						x -= chances[y]
						y += 1
					chance += x / drivers_no_points
					drivers_no_points -= 1
				# print(drivers[i] + ' chance to win in next race is ' + str(round((chance * 100 / total_points), 2)) + '%')
				driver_coeficient.update({drivers[i]: round( ( 100/(chance * 100 / total_points) - 0.7 ), 2 )})
				chances.append(chance)
				i += 1
		race_i += 1
	# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
	drivers_list = Drivers.objects.order_by('-reg_date')
	for driver in drivers_list:
		profile = Account_profile.objects.get(login = driver.login)
		Drivers.objects.filter(login = driver.login).update(coeficient = driver_coeficient[profile.account_name + ' ' + profile.account_surname])
		

	if request.POST:
		race_name = request.POST['race_name']
		if request.user.is_authenticated:
			current_user = request.user.username
			current_user_info = Account_profile.objects.get(login = current_user)
		else:
			current_user_info = []
		accounts_info = Account_profile.objects.all()
		race = Race.objects.get(race_name = race_name)
		return render(request, 'bets/bet_confirm.html', {'page': 'bets', 
			'user_info': current_user_info, 
			'notification': False, 
			'drivers_list': drivers_list,  
			'accounts_info': accounts_info, 
			'race_name': race_name,
			'race': race,
			'driver_coeficient': driver_coeficient})
	else:
		return redirect('/bets')

def bet_result(request):
	if request.POST:
		if request.user.is_authenticated:
			current_user = request.user.username
			current_user_info = Account_profile.objects.get(login = current_user)
		else:
			current_user_info = []

		prev_bet_code = Stake.objects.order_by('-bet_date')
		if prev_bet_code:
			prev_bet_code = str(prev_bet_code[0])
			prev_bet_code = prev_bet_code.split('#')
			prev_bet_code = int(prev_bet_code[-1])
			prev_bet_code += 1
		else:
			prev_bet_code = 1

		driver_name = request.POST['driver_login']
		bet = request.POST['bet']
		race_name = request.POST['race_name']
		payment_type = request.POST['payment_type']
		coeficient = request.POST['coeficient']
		bank_account_number = 'EE302200221043383149'
		bet_code = 'Bzz! #' + str(prev_bet_code)
		return render(request, 'bets/bet_result.html', {
			'page': 'bets', 
			'user_info': current_user_info, 
			'notification': False,
			'driver_name': driver_name,
			'bet': bet,
			'race_name': race_name,
			'payment_type': payment_type,
			'bank_account_number': bank_account_number,
			'bet_code': bet_code,
			'coeficient': coeficient})
	else:
		return redirect('/bets')

def accept(request):
	if request.user.is_authenticated:
		current_user = request.user.username
		current_user_info = Account_profile.objects.get(login = current_user)
	else:
		current_user_info = []

	prev_bet_code = Stake.objects.order_by('-bet_date')
	if prev_bet_code:
		prev_bet_code = str(prev_bet_code[0])
		prev_bet_code = prev_bet_code.split('#')
		prev_bet_code = int(prev_bet_code[-1])
		prev_bet_code += 1
	else:
		prev_bet_code = 1

	driver_name = request.POST['driver_login']
	bet = request.POST['bet']
	race_name = request.POST['race_name']
	payment_type = request.POST['payment_type']
	coeficient = request.POST['coeficient']
	bank_account_number = 'EE302200221043383149'
	bet_code = 'Bzz! #' + str(prev_bet_code)

	if payment_type == 'cash':
		bank_account_number = 'none'

	a = Stake(
		name = current_user_info.account_name + ' ' + current_user_info.account_surname,
		winner_name = driver_name,
		race_name = race_name,
		payment_method = payment_type,
		coeficient = coeficient,
		stake = bet,
		bank_account_number = bank_account_number,
		bet_code = bet_code,
		bet_date = timezone.now(),
		status = 'False')
	a.save()

	transactions = Account_profile.objects.get(login = current_user_info.login).transaction_history
	Account_profile.objects.filter(login = current_user_info.login).update(transaction_history = transactions + timezone.now().strftime("%d-%B-%Y %H:%M") + ' (' + bet_code + ') ' + bet + ' евро на победу гоньщика ' + driver_name + ' с коэфицентом - (' + coeficient + ') (' + payment_type + ')' + '(False)|')

	return redirect('/bets')