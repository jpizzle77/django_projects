from django.shortcuts import render, HttpResponse, redirect
from models import Login_Reg
from django.contrib import messages

  # the index function is called when root is visited

def index(request):
	print "--------inside INDEX route----------"

	
	#this will grab all the data from the User model. It will be stored inside the dictionary context and passed over via the variable context
	context = {
		'users': Login_Reg.objects.all()
	}

	

	
	return render(request, 'userdash/index.html',context)



def signin(request):
	print "--------Signin html webpage---------"

	
	#this will grab all the data from the User model. It will be stored inside the dictionary context and passed over via the variable context
	'''context = {
		'users': Course.objects.all()
	}'''

	
	return render(request, 'userdash/login.html')

def login(request, methods='POST'):
	print " ----------    Signin info is POSTED.     ------------------"
	print '*'*50
	
	if request.method == 'POST':
		print request.POST['email']
		response = Login_Reg.objects.check_password(request,request.POST)


		print response, '<----------here is the response'
		if response[0]== False:
			for message in response[1]:
				print "joe mamma"
				messages.error(request, message[1])
			return redirect('userdash:signin')
		else:
			request.session['user']= {

			'user_id': response[1].id,
			'first_name': response[1].first_name,
			'last_name': response[1].last_name,
			'email': response[1].email,
			}

			print request.session['user']['user_id'], "<--------------here is the user id to sign in!!!!!!!!!!!"
			if request.session['user']['user_id'] == 1:
				request.session['user_level'] = 9
				print request.session['user_level'], "<---------user_level = ADMIN -----"
				return redirect('dashboard:admin')
			else:
				request.session['user_level'] = 1
				print request.session['user']['user_id'], "<---------user id--->"
				print request.session['user_level'], "<---------user_level guest......-----"
				return redirect('dashboard:index')



	

	return redirect('userdash:index')
	


def register(request):
	print " ----------    NEW USER REGISTERS ON THIS PAGE  ------------------"

	print '*'*50

	return render(request,'userdash/register.html')

def create_user(request):
	print " ----------    ADMIN CREATES A NEW USER PAGE  ------------------"

	print '*'*50

	return render(request,'userdash/create_new.html')
	



def register_user(request, methods='POST'):
	print " ----------    ROUTE TO REGISTER A USER (POST)  ------------------"

	if request.method == 'POST':
		print request.POST
		user_id = Login_Reg.objects.last()
		print user_id
		response = Login_Reg.objects.check_create(request,request.POST)

		print response, '<----------here is the response----------------'
		if response[0]== False: #this means the validations failed
			for message in response[1]:
				print "joe mamma"
				messages.error(request, message[1])
			return redirect('userdash:register')
		else: # the response returns a True, and returns the new user that was created
			
			request.session['user']= {
			"id": response[1].id,
			'first_name': response[1].first_name,
			'last_name': response[1].last_name,
			}
			if request.session['user']['id'] == 1: #this will make the first person to register the ADMIN
				request.session['user_level'] = 9
				print request.session['user_level'], "<---------user_level = ADMIN-----"
				return redirect('dashboard:admin')
			else:
				try:
					if request.session['user_level'] == 9: # this line will check to see if the ADMIN is creating a new user, or if someone is registering
						print request.session['user_level'], "<---------user_level  Still an Admin......-----"
						return redirect('dashboard:admin')
				except:
					return redirect('dashboard:index')

			


	'''return redirect('userdash:index')'''



'''def dashboard(request, methods='POST'):
	print "------------   user dashboard html page    -----------"



	return render(request, 'dashboard/index.html')'''


