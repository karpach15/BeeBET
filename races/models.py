from django.db import models
from drivers.models import Drivers
from account_profile.models import Account_profile

class Race(models.Model):
	RACE_PAST = [('True', 'True'), ('False', 'False')]
	OPENED = [('Closed', 'Closed'), ('Opened', 'Opened')]
	drivers_list = Drivers.objects.order_by('-reg_date')
	DRIVERS_LIST = []
	DRIVERS_LIST.append(('None', 'None'),)
	for driver in drivers_list:
		current_user_info = Account_profile.objects.get(login = driver.login)
		DRIVERS_LIST.append((current_user_info.account_name + ' ' + current_user_info.account_surname, current_user_info.account_name + ' ' + current_user_info.account_surname),)

	race_name = models.CharField(max_length = 120)
	time_date = models.DateTimeField()
	start = models.CharField(max_length = 120)
	finish = models.CharField(max_length = 120)
	distance = models.FloatField(max_length = 50)
	min_stake = models.FloatField(default = 3)
	jackpot = models.FloatField(default = 0)
	winner = models.CharField(max_length = 120, choices = DRIVERS_LIST, default = 'None')
	drivers = models.IntegerField(default = 0)
	driver_list = models.TextField(default = '|')
	race_result = models.TextField(blank = True)
	stakes = models.IntegerField(default = 0)
	race_past = models.CharField(max_length = 5, choices = RACE_PAST, default = 'False')
	allowed_cars = models.CharField(max_length = 100, default = 'no limits')
	time_before_race = models.CharField(max_length = 100)
	entery_price = models.FloatField(default = 5)
	opened = models.CharField(max_length = 10, default = 'Closed', choices = OPENED)

	def __str__(self):
		return self.race_name