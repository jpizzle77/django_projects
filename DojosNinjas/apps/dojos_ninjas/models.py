from __future__ import unicode_literals
from django.db import models
  # Create your models here.
class Dojo(models.Model):
	name = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=2)
	desc= models.TextField(default="Joe momma")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __repr__(self):
		return "<Name: {} City:{} State:{} Desc: {}>".format(self.name, self.city, self.state, self.desc)


class Ninja(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	dojo = models.ForeignKey(Dojo, related_name = "ninjas")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __repr__(self):
		return "<First Name: {} Last Name:{}>".format(self.first_name, self.last_name)