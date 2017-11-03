from django.shortcuts import render, HttpResponse, redirect
from models import User
  # the index function is called when root is visited

def index(request):
	print "--------inside INDEX route----------"
	#this will grab all the data from the User model. It will be stored inside the dictionary context and passed over via the variable context
	context = {
		'users': User.objects.all()
	}
	
	return render(request, 'friends/index.html', context)



def new(request):
	#directs you to the Create a new user webpage.
	print request
	
	return render(request, 'friends/new_user.html')



def create(request, methods='POST'):
	#inside the CREATE method. Information (first_name,last_name,email) is posted via a form into this method and is first passed into the validate_info() method. If the data is valid it is passed into the create_user methodd
	print '*'*50
	print request
	
	if not User.objects.validate_info(request,request.POST): #basically saying if data is invalid, redirect to the new register page

		return redirect('/users/new')

	else: #if data is valid, data is passed into database using the create_user() method. Then redirects to homepage
		print 'valid data about to be processed'
		User.objects.create_user(request,request.POST)
		return redirect('/users')




def show_id(request,number):
	#this renders the show_user.html, displaying the users first/last names, and email. There will be 2 options on this page. One to edit the user and one to delete the user'
	print request, '<----------path for certain user'
	print number, '<-----id of user--------'
	
	#the context variable here is grabbing 1 user from here. The users id is passed over as a variable called number. This allows you to pass over the users firt/last names and email to be displayed onto the webpage
	context= {

		'user': User.objects.get(id=number)
	
	}

	return render(request, 'friends/show_user.html', context)


def edit_number(request,number):
	#this renders the edit page. This can be from 2 different routes. Index.html or show_user.html.  The users data is passed over via context
	print number
	print request

	context= {

		'user': User.objects.get(id=number)
	
	}
	
	return render(request, 'friends/edit.html', context)

def edited_info(request, number, methods='POST'):
	#inside the edited info method. This will make sure the new updated info is valid first. If the data is valid, it will be passed into the database(updating)
	print request
	print number
	
	if not User.objects.validate_info(request,request.POST):
		return redirect('/users')
	else:
		print 'dis going to to update info'
		print request.POST['first_name']
		User.objects.update_info(request,request.POST)
		return redirect('/users')


def delete(request,number):
	#render delete webpage, and grabs the id that will be deleted via the context dictionary
	print number
	print request


	context= {

		'user': User.objects.get(id=number)
	
	}
	
	return render(request, 'friends/delete.html',context)


def confirm_delete(request,number):
	# uses the delete_info() method to delete user
	print request

	User.objects.delete_info(request,request.POST)

	return redirect('/users')