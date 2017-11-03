from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import re

  # Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
MIN_LENGTH=3

class UserManager(models.Manager):
	
	def validate_info(self, request, data):
		print "inside validate_info method"

		valid_data = True

		#check names for empty
		if len(data['first_name']) < 1 or len(data['last_name']) < 1 or len(data['email']) < 1:
			messages.error(request,'no empty field for first, last names or email')
			valid_data = False

		# check names for min length
		if len(data['first_name']) < MIN_LENGTH or len(data['last_name']) < MIN_LENGTH or len(data['email']) < MIN_LENGTH:
			messages.error(request,'fields must be at least 3 characters')
			valid_data = False

		#check email unique
		if not EMAIL_REGEX.match(data['email']):
			messages.error(request,'email needs correct format "ex: abc@abc.com"')
			valid_data = False

		'''if len(self.filter(email = data['email']))>0:
			messages.error(request,'email needs to be unique')
			valid_data = False'''

		return valid_data

	def create_user(self,request,data):
		#this is the method that will create the user
		print "inside create_user method"

		if request:
			self.create(
				first_name = data['first_name'],
				last_name = data['last_name'],
				email = data['email']
				)

		return request

	def update_info(self,request,data):
		#this will update the user
		print "inside update_info method"

		b =request.POST['user_id']

		a= User.objects.get(id=int(b))
		print a
		a.first_name =request.POST['first_name']
		a.last_name =request.POST['last_name']
		a.email =request.POST['email']
		a.save()
		return request

	def delete_info(self,request,data):
		#this will delete user
		print "inside delete_info method"

		b =request.POST['user_id']
		print b
		a= User.objects.get(id=int(b))
		print a
		print a.id, "-----------this is the user id #"

		a.delete()
		a.save()
		print a, ' printing the variable "a", after doing a.delete() and a.save()'

		return request
		
	
		


class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=2)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()

	def __repr__(self):
		return "<First name: {} Last Name:{} Email:{} ID:{}>".format(self.first_name, self.last_name, self.email,self.id)

