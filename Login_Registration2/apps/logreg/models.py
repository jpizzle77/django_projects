from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class Login_Reg_Manager(models.Manager):

	def check_create(self, request, data):
		print "inside the validate_info() method"

		def number(string):
			return re.search('\d', string)

		errors=[]
	

		if len(data['first_name']) < 1: 
			errors.append(['first_name',"First name cannot be empty or contain numbers!"])
		if number(data['first_name']):
			errors.append(['first_name','No numbers are allowed for first name'])
			
		if len(data['last_name']) < 1:
			errors.append(['last_name',"Last name cannot be empty or contain numbers!"])
		if number(data['last_name']):
			errors.append(['last_name','No numbers are allowed for last name'])
			
		if len(data['email']) < 1:
			errors.append(['email','email',"Email name cannot be empty and must be a valid email!"]) 
		if not EMAIL_REGEX.match(data['email']):
			errors.append(['email',"Invalid Email Address!"])

		if len(data['password']) < 1:
			errors.append(['password',"Password cannot be empty!"])
			
		if data['password'] != data['confirm_password']:
			errors.append(['confirm_password','passwords no match!'])

		if errors:
			return [False, errors]

		else:
			current_user = Login_Reg.objects.filter(email = data['email'])
			if current_user:
				errors.append(['first_name','email needs to be unique'])
				return [False, errors]

			else:
				new_user = Login_Reg(first_name=data['first_name'], last_name=data['last_name'], email=data['email'])
				hashed= bcrypt.hashpw(data['password'].encode(),bcrypt.gensalt())
				new_user.password = hashed
				new_user.save()
				return [True, new_user]

	def check_password(self,request, data):
		print "inside the check_password()"
		print data['password']
		errors=[]
		current_user = Login_Reg.objects.filter(email = data['email'])
		print current_user

		if current_user[0]:
			print "there is someone in databse"

		if bcrypt.checkpw(data['password'].encode(), current_user[0].password.encode()):
			print "passwords match"

			return [True, current_user[0]]

		else:
			print "There is a  fucking problem dipshit"
			errors.append(["login", "please enter a valid email or correct password"])
			return [False, errors]

		
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
