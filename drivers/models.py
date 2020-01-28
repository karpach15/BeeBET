from django.db import models
from django.utils import timezone

class Drivers(models.Model):
	STATUS_CHOICES = [('True', 'True'), ('False', 'False')]

	login = models.CharField(max_length = 30)
	coeficient = models.FloatField(default = 0)
	custom_coeficient = models.FloatField(default = 0)
	reg_date = models.DateTimeField(default = timezone.now)
	status = models.CharField(default='False', max_length = 10, choices = STATUS_CHOICES)

	def __str__(self):
		return self.login