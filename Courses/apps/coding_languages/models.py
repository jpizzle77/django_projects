from __future__ import unicode_literals
from django.db import models
from django.contrib import messages

class CourseManager(models.Manager):

	def create_user(self,request,data):
		#this is the method that will create the user
		print "inside create_user method"

		if request:
			self.create(
				name = data['name'],
				description = data['description'],
				created_at = data['created_at']
				)
		return request

	def delete_info(self,request,data):
		#this will delete user
		print "inside delete_info method"

		b =request.POST['user_id']
		print b
		a= Course.objects.get(id=int(b))
		print a.name

		a.delete()

		
		print a.name
		print request
		return request

class Course(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = CourseManager()
	

	def __repr__(self):
		return "<name: {} Description:{} Created at:{} >".format(self.name, self.description, self.created_at)

