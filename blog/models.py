# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils import timezone
#definicion de objeto
#Post(models.Model) nombre de modelo, indicamos a Django que Post es un modelo
class Post(models.Model):
	#foreignkey indica que hay un vinculo con otro objeto (equivale a clave ajena realmente?)
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title