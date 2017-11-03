from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from ..user_app.models import User
from models import Description, Message, Reply


# Create your views her


def home(request):
	response = "Hello, I am your first request!"
	return HttpResponse(response)


def edit(request):  
	print "INSIDE DASHBOARD EDIT ROUTE"
	try:
		request.session['user']['user_id']
	except:
		request.session['user']['user_id']=1

	user_id = request.session['user']['user_id']


	
	
	context = {
		'user': User.objects.get(id=int(user_id))
	}

	return render(request,'comment_app/edit.html',context)



def edit_info(request, methods ='POST'): 

	print "<--------------inside the EDIT_INFO ROUTE" 
	
	print request.POST
	
	response = User.objects.validate_info(request,request.POST)
	print response, '<---------this response will validate the first/last names and email input  ---------------'

	if response[0] == False:
		for message in response[1]:
				print "joe mamma"
				messages.error(request, message[1])
		return redirect('user_dashboard:edit')

	else:
			print 'dis going to to update info'
			print request.POST['first_name']
			User.objects.update_info(request,request.POST)
			return redirect('user_dashboard:guest')

def edit_password(request, methods ='POST'): 
		response = User.objects.validate_password(request,request.POST)
		print response, '<----------this response will make sure the password/confirm password match----------------'

		if response[0] == False:
			for message in response[1]:
				print "joe mamma"
				messages.error(request, message[1])
				return redirect('user_dashboard:edit')


		else:
			User.objects.update_password(request,request.POST)
			return redirect('user_dashboard:guest')


def guest(request):
	print "------------   INSIDE GUEST ROUTE  -----------"

	context = {
		'users': User.objects.all()
	}
	

	return render(request,'comment_app/guest.html',context)

def show(request, number):
	print "--------------inside the show method() in views "
	print number, "this will show the persons profile you are clicking on. It will show there name, id, email and a description"
	try:
		request.session['user']['user_id']
		print request.session['user']['user_id'],"this is the user that is signed in. They can leave a comment on the user's description"
	except:
		request.session['user']['user_id']=1

	
	user_id =int(number)
	print user_id
	print type(user_id)
	


	
	description = User.objects.get(id=user_id).descriptions.last()
	print description.id

	

	#replies = Message.objects.get(id=comment_id).comments.all()
	#print comment

	try:
		description_id = description.id

	except:
		description_id=1

	print description_id,"----------description_id"

	try:
		comment_id =request.session['comment']['id']

	except:
		comment_id=1

	print comment_id, "<------this is the comment id-------->"

	try:
		comment_on_comment_id =request.session['reply']['id']


	except:
		comment_on_comment_id=1

	print comment_on_comment_id, "<------this is the comment on comment id-------->"



	replies= Message.objects.get(id=comment_id).comments.all()
	print replies, "<------------here are the replies for 1 message"

	
	

	#create a dictionary that grabs info from the User and Description models. The user and desripition id's are used to filter the desired info
	#the info is passed over to the show.html webpage where it can be displayed
	context = {
		'user': User.objects.get(id=int(number)),
		'description': description,
		'comments': Description.objects.get(id=description_id).messages.all(),
		'replies': replies
		}
	print "^"*50
	#print comments.user, "<--------------FUCKING AROUND W ORM----------------"
	print "^"*50
	#print context, "<--------------CONTEXT BEING PASSED OVER"

	return render(request,'user_app/show.html',context)



def description(request, methods ='POST'): 

	print "<--------------POSTING the DESCRIPTION " 
	number = request.POST
	number = request.POST['user_id']
	print number, "<-------ID OF USER CREATING DESCRIPTION"
	description_id = Description.objects.last()

	print description_id.id, "this will be last id of known 'description' "

	description = Description.objects.create_description(request,request.POST)
	print description.description, description.user_id
	print description.id, "<-------------dis is the description id"

	request.session['description']= {
				"id": description.id,
				"user_id":description.user_id,
				
				}

	print request.session['description'], " <-----------------here is the session description"
	
	return redirect('comment_app:show', number= number)


def comment(request, methods ='POST'): 
	print "@"* 50
	print "<--------------inside the comment ROUTE" 
	print "@"* 50
	print request.POST, "<--------------here is the post"
	number = request.POST['user_id']
	
	print number,"$$$$$$$$------------ user id-----$$$$$$$$$$$"
	comment_id = Message.objects.last()
	
	print comment_id.id, "this will be last id of known 'comment "

	comment = Message.objects.create_comment(request,request.POST)
	print comment.message, comment.user_id
	print comment.user_id, "<-------------dis is the comment user_id"

	request.session['comment']= {
				"id": comment.id,
				"user_id":comment.user_id,
				"description_id": comment.description_id,
				'comment': comment.message,
				
				}

	print comment.user_id, "<@-------------------------------comment user_id"

	print request.session['comment'], " <-----------------here is the session comment"


	return redirect('comment_app:show', number= number)

def reply(request, methods ='POST'): 
	print "@"* 50
	print "<--------------inside the reply ROUTE" 
	print "@"* 50
	print request.POST, "<--------------here is the post"
	number = request.POST['user_id']
	comment_id=request.POST['comment_id']
	print comment_id, "<-----------comment Id--------------------"

	
	

	reply = Reply.objects.create_reply(request,request.POST)
	print reply.reply, reply.user_id
	print reply.id, "<-------------dis is the reply user_id"

	request.session['reply']= {
				"id": reply.id,
				"comment_id": reply.comment_id,
				'reply': reply.reply,
				'user': reply.user_id
				
				}

	print reply.user_id, "<@-------------------------------reply user_id"

	print request.session['reply'], " <-----------------here is the session reply"


	return redirect('comment_app:show', number=number) # think of this as /show/users/85  'number=number gives u the 85'




