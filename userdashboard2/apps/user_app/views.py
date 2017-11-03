from django.shortcuts import render, HttpResponse, redirect
from models import User
from ..comment_app.models import Description
from django.contrib import messages

def index(request):
	print "--------inside INDEX route----------"

	return render(request, 'user_app/index.html')#,context)



def sign_in(request):
	print "--------Signin html webpage---------"

	return render(request, 'user_app/sign_in.html')

def register(request):
	print " ----------    NEW USER REGISTERS ON THIS PAGE  ------------------"

	print '*'*50

	return render(request,'user_app/register.html')

def new(request):
	print " ----------    ADMIN NEW USER REGISTERS ON THIS PAGE  ------------------"

	print '*'*50

	return render(request,'user_app/new.html')


def register_user(request, methods='POST'):
	print " ----------    ROUTE TO REGISTER A USER (POST)  ------------------"

	if request.method == 'POST':
		print request.POST
		user_id = User.objects.last() #grabs the last id in DB to be used for the new user to be created
		print user_id

		# calling the custom validate_info() method to validate the incoming data (first name, last name, email) is valid before being passed into DB. Will return either a True or False(with errors) response
		response = User.objects.validate_info(request,request.POST)

		print response, '<----------here is the response (True or False (w a list of the errors returned as well))----------------'

		if response[0] == False: #this means the validations failed. Return back to the register page with the errors posted

			# returns the list of errors. 
			for message in response[1]:
				messages.error(request, message[1])
			return redirect('user_app:register')


		else:  #this will first validate the passwords, then create a new user if input is correct

			response = User.objects.validate_password(request,request.POST)
			print response, '<----------here is the response (True or False (w a list of the errors returned as well))----------------'

			if response[0]== False: #this means the validations failed. Return back to the register page with the errors posted

			# returns the list of errors
				for message in response[1]:
					messages.error(request, message[1])
				return redirect('user_app:register')

			else:
				new_user = User.objects.create_user(request,request.POST) # a new user is created via the custom create_user() method
				print new_user, "<----------------what up new user !!!!!!!!!"
				print new_user.id, new_user.first_name, new_user.last_name, new_user.user_level
			
				#store the new user info into a session dictionary
				request.session['user']= {
				"id": new_user.id,
				'first_name': new_user.first_name,
				'last_name': new_user.last_name,
				}

				print request.session['user']

				if new_user.id == 56:
					return redirect('dashboard:admin')
				else:
					return redirect('dashboard:guest')


	

def login(request, methods='POST'):
	print " ----------    SIGN-IN info is POSTED for validations.     ------------------"
	print '*'*50
	
	if request.method == 'POST':
		print request.POST['email']
		response = User.objects.check_password(request,request.POST)


		print response, '<----------here is the response'
		if response[0]== False:
			for message in response[1]:
				print "joe mamma"
				messages.error(request, message[1])
				return redirect('user_app:sign_in')
		else:
			request.session['user']= {

			'user_id': response[1].id,
			'first_name': response[1].first_name,
			'last_name': response[1].last_name,
			'email': response[1].email,
			}

			print request.session['user']['user_id'], "<--------------here is the user id to sign in!!!!!!!!!!!"

			if request.session['user']['user_id'] ==2:
				return redirect('dashboard:admin')
			else:
				print "is it coming in this route????????????"
				return redirect('user_dashboard:guest')

	return redirect('user_app:sign_in')


def admin(request):
	print "------------   INSIDE ADMIN ROUTE  -----------"

	context = {
		'users': User.objects.all()
	}
	

	return render(request,'user_app/admin.html',context)
	
def guest(request):
	print "------------   INSIDE GUEST ROUTE  -----------"

	context = {
		'users': User.objects.all()
	}
	

	return render(request,'user_app/guest.html',context)

def show(request, number):
	print "--------------inside the show method() in views "
	print number, "this will show the person's id"
	description_id = int(request.session['description_id']), "<-----the description id"
	print type(description_id)
	

	try:
		comment_id = (request.session['comment']['id']),"<------the comment id"
	except:
		comment_id=1

	print comment_id
	try:
		request.session['comment']
	except:
		request.session['comment']=''

	#create a dictionary that grabs info from the User and Description models. The user and desripition id's are used to filter the desired info
	#the info is passed over to the show.html webpage where it can be displayed
	context = {
		'user': User.objects.get(id=int(number)),
		'description': Description.objects.get(id=description_id),
		'comment': Message.objects.get(id=comment_id)
	}

	print context

	return render(request,'user_app/show.html',context)

def edit(request,number):  
	print number, "this is the id to be edited"
	print type(number)
	x = int(number)
	print type(x)
	request.session['id'] = x
	print request.session['id']
	print type(request.session['id'])
	context= {
		'user': User.objects.get(id=int(number)),

	}
	print context


	return render(request,'user_app/edit.html', context)

def user_edit(request,number):  
	print number, "route for user to edit info"

	return render(request,'user_app/user_edit.html')



def edit_info(request,number, methods ='POST'): 

	print "<--------------inside the EDIT_INFO ROUTE" 
	
	print request.POST
	
	response = User.objects.validate_info(request,request.POST)
	print response, '<---------this response will validate the first/last names and email input  ---------------'

	if response[0] == False:
		for message in response[1]:
				print "joe mamma"
				messages.error(request, message[1])
		return redirect('users:edit', number = number)

	else:
			print 'dis going to to update info'
			print request.POST['first_name']
			User.objects.update_info(request,request.POST)
			return redirect('dashboard:admin')


def edit_password(request,number, methods ='POST'): 
		response = User.objects.validate_password(request,request.POST)
		print response, '<----------this response will make sure the password/confirm password match----------------'

		if response[0] == False:
			for message in response[1]:
				print "joe mamma"
				messages.error(request, message[1])
				return redirect('users:edit', number = number)


		else:
			User.objects.update_password(request,request.POST)
			return redirect('dashboard:admin')

def edit_level(request,number, methods ='POST'):
	print "------------------this will let you edit user to be an ADMIN OR GUEST----------------"
	print request.POST

	response = User.objects.update_level(request,request.POST)

	return redirect('dashboard:admin')

def remove(request,number):
	print "--------inside delete.html route----------"
	#this will grab all the data from the User model. It will be stored inside the dictionary context and passed over via the variable context
	print number

	context = {
		'user': User.objects.get(id=int(number))
	}
	
	return render(request,'user_app/remove.html', context)

def confirm_remove(request, methods='POST'):
	# uses the delete_info() method to delete user
	print request


	User.objects.delete_info(request,request.POST) # in the userdash app models.py

	return redirect('dashboard:admin')
	
def clear(request):
	print " -------------clearing the session!!!!!!!!!!!!!!"
	request.session.clear()
	return redirect('user_app:sign_in')




	
