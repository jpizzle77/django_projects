from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class Login_Reg_Manager(models.Manager):

	def validate_info(self, request, data):
		print "inside the validate_info() method"

		def number(string):
			return re.search('\d', string)
		errors=[]
	

		if len(data['first_name']) < 1: 
			errors.append("First name cannot be empty or contain numbers!")
		if number(data['first_name']):
			errors.append('No numbers are allowed for first name')
			
		if len(data['last_name']) < 1:
			errors.append("Last name cannot be empty or contain numbers!")
		if number(data['last_name']):
			errors.append('No numbers are allowed for last name')
			
		if len(data['email']) < 1:
			errors.append("Email name cannot be empty and must be a valid email!") 
		if not EMAIL_REGEX.match(data['email']):
			errors.append("Invalid Email Address!")
		if len(self.filter(email = data['email']))> 0:
			errors.append('email needs to be unique')
			
			
		if len(data['password']) < 1:
			errors.append("Password cannot be empty!")
			
		if data['password'] != data['confirm_password']:
			errors.append('passwords no match!')
			
		print errors, "$" *25
		return errors

	def create_user(self,request, valid_data):
		print "inside create_user() inside the Class Login_Reg Manager "
		hashed= bcrypt.hashpw(valid_data['password'].encode(),bcrypt.gensalt())
		
		return self.create(
				first_name = valid_data['first_name'],
				last_name = valid_data['last_name'],
				email = valid_data['email'],
				password = hashed,
				
				)

	def check_password(self,request, data):
		print "inside the check_password()"
		print data['password']

		#first check to see if email already exists
		if len(self.filter(email = data['email']))>0:
			messages.error(request,'email needs to be unique')

		hashed= bcrypt.hashpw(data['password'].encode(),bcrypt.gensalt())

		if  not bcrypt.checkpw(data['password'].encode(), hashed):
			print "please try again with password"
			return request
		else:
			print "please try again with password"
			return request


class Login_Reg(models.Model):
	#username = models.CharField(max_length=255, unique= TRUE)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password= models.CharField(max_length=255)
	confirm_password= models.CharField(max_length=255)
	objects = Login_Reg_Manager()
	

	def __repr__(self):
		return "<First Name: {} Last Name:{} Email:{} >".format(self.first_name, self.last_name, self.email)


