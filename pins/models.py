from __future__ import unicode_literals

from django.db import models

# Create your models here.

PRIVACY_CHOICES = (
	('PR', 'Private'),
	('PB', 'Public'),
)

class Pins(models.Model):
	name		= models.CharField(max_length=200)
	slug		= models.SlugField(unique=True)
	category	= models.ForeignKey('Category')
	privacy		= models.CharField(max_length=2,choices=PRIVACY_CHOICES)
	description	= models.TextField(blank=True)

	def __unicode__(self):
		return self.name

class Category(models.Model):
	name		= models.CharField(max_length=200)
	slug 		= models.SlugField(unique=True)
	description	= models.TextField(blank=True)

	def __unicode__(self):
		return self.name