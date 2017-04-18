from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	uname = models.CharField(max_length=200)
	pwd = models.CharField(max_length=200)
	def __str__(self):
		return self.uname
