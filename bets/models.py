from django.db import models
from drivers.models import Drivers
from account_profile.models import Account_profile
from races.models import Race
from django.utils import timezone

class Stake(models.Model):
	accounts = Account_profile.objects.all()
	USERS_CHOICES = []
	for account in accounts:
		USERS_CHOICES.append((account.account_name + ' ' + account.account_surname, account.account_name + ' ' + account.account_surname),)
	
	drivers_list = Drivers.objects.order_by('-reg_date')
	DRIVERS_CHOICES = []
	for driver in drivers_list:
		current_user_info = Account_profile.objects.get(login = driver.login)
		DRIVERS_CHOICES.append((current_user_info.account_name + ' ' + current_user_info.account_surname, current_user_info.account_name + ' ' + current_user_info.account_surname),)
	
	races = Race.objects.all()
	RACES_NAME = []
	for race in races:
		current_user_info = Account_profile.objects.get(login = driver.login)
		RACES_NAME.append((race.race_name, race.race_name),)

	PAYMNET_METHOD = [('card', 'card'),('cash', 'cash')]

	STATUS = [('True', 'True'),('False', 'False')]

	WON = [('Waiting', 'Waiting'),('Won', 'Won'),('Lost', 'Lost')]

	bet_code = models.CharField(max_length = 300, default = 'Bzz! #0000')
	name = models.CharField(max_length = 50, choices = USERS_CHOICES)
	winner_name = models.CharField(max_length = 50, choices = DRIVERS_CHOICES)
	race_name = models.CharField(max_length = 200, choices = RACES_NAME)
	payment_method = models.CharField(max_length = 10, choices = PAYMNET_METHOD)
	coeficient = models.FloatField()
	stake = models.FloatField()
	bank_account_number = models.CharField(max_length = 300, default = 'EE302200221043383149')
	bet_date = models.DateTimeField(default = timezone.now)
	won = models.CharField(max_length = 10, choices = WON, default = 'None')
	status_won = models.CharField(max_length = 10, choices = STATUS, default = 'False')
	status = models.CharField(max_length = 10, choices = STATUS, default = 'False')
	jackpot = models.FloatField(default = 0)

	def __str__(self):
		return self.bet_code