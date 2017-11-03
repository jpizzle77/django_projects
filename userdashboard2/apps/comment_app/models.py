from __future__ import unicode_literals

from django.db import models
#from app1.models import SomeModel
from ..user_app.models import User

class DescriptionManager(models.Manager):
	def create_description(self,request,data):
		print "-----------inside the create_description() method----------"
		description = Description(description=data['description'],user_id=data['user_id'])
		print description
		description.save()
		return description




class Description(models.Model):
	description = models.CharField(max_length=255)
	user = models.ForeignKey(User, related_name = "descriptions")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = DescriptionManager()
	

	def __repr__(self):
		return "<Description: {} ID:{}>".format(self.description, self.id)




class MessageManager(models.Manager):
	def create_comment(self,request,data):
		print "@"* 50
		print "-----------inside the create_comment() method----------"
		print "@"* 50
		comment = Message(message=data['comment'],user_id=data['comment_user_id'],description_id=data['description_id'])
		#print comment.comment_user_id, "<------------------here is the comment user_id that is being left"
		print comment
		comment.save()
		return comment

class Message(models.Model):
	#username = models.CharField(max_length=255, unique= TRUE)
	message = models.CharField(max_length=255)
	description = models.ForeignKey(Description, related_name = "messages")
	user = models.ForeignKey(User, related_name = "users", default=1)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = MessageManager()
	
	def __repr__(self):
		return "<Message: {}, Description: {}, User: {}, ID: {} >".format(self.message,self.description,self.user, self.id)



class ReplyManager(models.Manager):
	def create_reply(self,request,data):
		print "@"* 50
		print "-----------inside the CREATE_REPLY() method----------"
		print "@"* 50
		reply = Reply(reply=data['reply'],user_id=data['reply_user_id'],comment_id=data['comment_id'])
		print reply.id, "here is the reply id #. OH BOY!!!!!!!!!!!!!!!!!!!!!!!!!!"
		
		print reply.reply,"-----Yo yo, its here"
		reply.save()
		return reply

class Reply(models.Model):
	#username = models.CharField(max_length=255, unique= TRUE)
	reply = models.CharField(max_length=255)
	comment = models.ForeignKey(Message, related_name = "comments", default =1)
	user = models.ForeignKey(User, related_name = "reply_users", default=1)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = ReplyManager()
	
	def __repr__(self):
		return "<Reply: {}, comment: {}, User: {}, Reply ID: {} >".format(self.reply,self.comment,self.user, self.id)






