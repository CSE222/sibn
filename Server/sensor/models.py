from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Readings(models.Model):
	sensor_type = models.CharField(max_length=200)
	reading = models.IntegerField(default=0)
	time = models.DateTimeField('time recorded')
	def __str__(self):
		return self.sensor_type

