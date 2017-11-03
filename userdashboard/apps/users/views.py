from django.shortcuts import render, HttpResponse, redirect
#from models import Login_Reg
from django.contrib import messages
from ..userdash.models import Login_Reg

def index(request):
	return redirect('users:new')

def new(request):
	print "------------   USERS APP INDEX  -----------"



	return render(request,'users/index.html')



def edit(request,number):  
	print number, "this is the id to be edited"
	print type(number)
	x = int(number)
	print type(x)
	request.session['id'] = x
	print request.session['id']
	print type(request.session['id'])
	context= {
		'user': Login_Reg.objects.get(id=int(number)),

	}
	print context


	return render(request,'users/edit.html',context)



def edit_info(request, number, methods ='POST'): 

	print "<--------------inside the EDIT_INFO ROUTE" 
	print number
	print request.POST
	print request.POST['user_id']
	print type(request.POST['user_id'])

	request.session['user_id']=request.POST['user_id']
	print request.session['user_id'],  "the request session id"
	

	response = Login_Reg.objects.validate_info(request,request.POST)
	print response, '<----------here is the response----------------'

	if response[0] == False:
		return redirect('dashboard:admin')
	else:
		print 'dis going to to update info'
		print request.POST['first_name']
		Login_Reg.objects.update_info(request,request.POST)
		return redirect('dashboard:admin')


def user_edit(request,number):  
	print "inside the user edit route"
	
	
	




	return render(request,'users/user_edit.html')

def show(request, number):
	print id, "this will show the person's id"
	context = {
		'user': Login_Reg.objects.get(id=int(number))
	}

	return render(request,'users/show.html',context)

def remove(request,number):
	print "--------inside delete.html route----------"
	#this will grab all the data from the User model. It will be stored inside the dictionary context and passed over via the variable context
	print number

	context = {
		'user': Login_Reg.objects.get(id=int(number))
	}
	
	return render(request,'users/remove.html', context)

def confirm_remove(request, methods='POST'):
	# uses the delete_info() method to delete user
	print request


	Login_Reg.objects.delete_info(request,request.POST) # in the userdash app models.py

	return redirect('dashboard:admin')
	


def clear(request):

	print " -------------clearing the session!!!!!!!!!!!!!!"
	request.session.clear()


	return redirect('userdash:login')



