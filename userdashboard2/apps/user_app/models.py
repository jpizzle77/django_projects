from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class User_DB_Manager(models.Manager):

	# this method will validate info forthe first/last names and email. It does not validate the password
	def validate_info(self, request, data):
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

		if errors:
			return [False, errors]

		else: #this will check to see if an email already exists in the DB. If one does it will return a false response
			current_user = User.objects.filter(email = data['email'])
			if current_user:
				errors.append(['first_name','email needs to be unique'])
				return [False, errors]
			else:
				return [True]

	def validate_password(self, request, data):
		print "inside the validate_password() method"
		errors=[]


		if len(data['password']) < 1:
			errors.append(['password',"Password cannot be empty!"])
			
		if data['password'] != data['confirm_password']:
			errors.append(['confirm_password','passwords no match!'])

		if errors:
			return [False, errors]

		else:
			return [True]


	def create_user(self,request,data):
		new_user = User(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], user_level=data['user_level'])
		hashed= bcrypt.hashpw(data['password'].encode(),bcrypt.gensalt())
		new_user.password = hashed

		if data['user_id'] != 1:
			user_level = "Guest"
			new_user.user_level= user_level
			print new_user.user_level
			new_user.save()
			return new_user


	def check_password(self,request, data):

		print "inside the check_password()"
		print data['password']
		errors=[]
		current_user = User.objects.filter(email = data['email'])
		print current_user

		try:
			if current_user[0]:
				print current_user[0]

				print "there is someone in databse"

				return [True, current_user[0]]

		except:
			print "no one in database or password didnt not match"
			errors.append(["login", "please enter a valid email or correct password"])
			return [False, errors]

	def update_info(self,request,data):
		#this will update the user
		print "inside update_info method"
		print request.POST, "look another POST!!!!!!!!!!!!!!!!!!!!!"
		b = request.POST['user_id']
		
		print type(b)
		print b, "<--------------user id"
		a = User.objects.get(id=int(b)) # gets the first record in the blogs table

		a.first_name =request.POST['first_name']
		a.last_name =request.POST['last_name']
		a.email =request.POST['email']
		a.save()
		return request

	def update_password(self,request,data):
		print "inside update_password method"
		print request.POST, "look another POST!!!!!!!!!!!!!!!!!!!!!"
		#the user_id is passed via a hidden POST and stored as user_id. This will let you locate the user's info (including the password for this update)
		user_id = request.POST['user_id']

		#the user (and user's info is found using the get() method and the user_id. The user's info is stored in a variable called user)
		user = User.objects.get(id=int(user_id))
		print user.password #accesing the user password

		hashed= bcrypt.hashpw(data['password'].encode(),bcrypt.gensalt()) #encrypting the new password being sent over
		print hashed, "<------------the new hashed password"
		user.password = hashed #updating the password
		user.save()
		print user.password
		return request

	def update_level(self,request,data):
		print "-------------inside update_level method--------------"
		user_id = request.POST['user_id']
		print user_id
		user = User.objects.get(id=int(user_id))
		print user.user_level #accesing the user level

		user.user_level= request.POST['level']
		print user.user_level
		user.save()
		return request

	def delete_info(self,request,data):
		#this will delete user
		print "inside delete_info method"

		user_id =request.POST['user_id']
		print user_id
		user= User.objects.get(id=int(user_id))
		print user.first_name

		user.delete()

		
		print user.first_name
		print request
		return request
		
		

class User(models.Model):
	#username = models.CharField(max_length=255, unique= TRUE)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password= models.CharField(max_length=255)
	user_level = models.CharField(max_length=10, default="Guest")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = User_DB_Manager()
	

	def __repr__(self):
		return "<First Name: {} Last Name:{} Email:{} ID:{}>".format(self.first_name, self.last_name, self.email, self.id)

