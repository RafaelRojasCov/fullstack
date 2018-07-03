# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
	id = models.IntegerField(primary_key=True)
	category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
	title = models.TextField()
	thumbnail_url = models.URLField()
	price = models.TextField()
	stock = models.BooleanField()
	product_description = models.TextField()
	upc = models.TextField()

	def __str__(self):
		return self.title


class Category(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.TextField()
	url = models.TextField(default=None)

	def __str__(self):
		return self.name
