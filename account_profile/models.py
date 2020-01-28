from django.db import models
from django.utils import timezone

class Account_profile(models.Model):
	DRIVING_LICENSE = [('True', 'True'), ('False', 'False')]

	account_name = models.CharField(max_length = 50)
	account_surname = models.CharField(max_length = 50)
	login = models.CharField(max_length = 100)
	password = models.CharField(max_length = 100)
	races_participated = models.IntegerField(default = 0)
	races_won = models.IntegerField(default = 0)
	about = models.TextField(blank=True)
	account_create_date = models.DateTimeField(default = timezone.now)
	driving_license = models.CharField(max_length = 5, default = False, choices = DRIVING_LICENSE)
	transaction_history = models.TextField(default = '|')
	account_pic = models.CharField(default="https://image.flaticon.com/icons/png/512/64/64572.png", max_length = 250)
	email = models.CharField(max_length = 100, default = None)

	def __str__(self):
		return (self.account_name + ' ' + self.account_surname )