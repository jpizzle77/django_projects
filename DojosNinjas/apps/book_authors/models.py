from __future__ import unicode_literals
from django.db import models
  # Create your models here.
class Book(models.Model):
	name = models.CharField(max_length=255)
	desc= models.TextField(default="shit fuck fuck shit")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __repr__(self):
		return "<Name: {} Descr: {}>".format(self.name, self.desc)


class Author(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	books = models.ManyToManyField(Book, related_name = "authors")
	notes= models.TextField(default="bitch")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __repr__(self):
		return "<First Name: {} Last Name:{}>".format(self.first_name, self.last_name)