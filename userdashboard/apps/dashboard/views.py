from django.shortcuts import render, HttpResponse, redirect

from ..userdash.models import Login_Reg

#from apps.userdash.models import Login_Reg
#from userdashboard.apps.userdash.models import Log
from django.contrib import messages

def index(request):
	print "------------   INDEX FOR DASHBOARD APP  -----------"
	print request.session['user']
	
	
	context = {
		'users': Login_Reg.objects.all()
	}
	




	return render(request,'dashboard/index.html',context)

def admin(request):
	print "------------   INSIDE ADMIN ROUTE  -----------"

	context = {
		'users': Login_Reg.objects.all()
	}
	

	return render(request,'dashboard/admin.html', context)


def edit(request):  
	print "INSIDE DASHBOARD EDIT ROUTE"
	print request.session['user']['user_id']
	user_id= request.session['user']['user_id']


	
	
	context = {
		'user': Login_Reg.objects.get(id=int(user_id))
	}

	return render(request,'dashboard/edit.html',context)


def edit_info(request, methods ='POST'): 

	print "<--------------inside the EDIT_INFO ROUTE" 
	
	print request.POST
	
	response = Login_Reg.objects.validate_info(request,request.POST)
	print response, '<----------here is the response----------------'

	if response[0] == False:
		return redirect('dashboard:index')
	else:
		print 'dis going to to update info'
		print request.POST['first_name']
		Login_Reg.objects.update_info(request,request.POST)
		return redirect('dashboard:index')

def show(request, number):


	context = {
		'user': Login_Reg.objects.get(id=int(number))
	}

	return render(request,'dashboard/show.html', context)



def description(request, methods="POST"):
	print "inside the description route"
	print request.POST

	return redirect('dashboard:index')







