from django.shortcuts import render, HttpResponse, redirect
from models import Course
  # the index function is called when root is visited

def index(request):
	print "--------inside INDEX route----------"
	#this will grab all the data from the User model. It will be stored inside the dictionary context and passed over via the variable context
	context = {
		'users': Course.objects.all()
	}

	
	return render(request, 'coding_languages/index.html', context)


def create(request, methods='POST'):
	#inside the CREATE method. Information (first_name,last_name,email) is posted via a form into this method and is first passed into the validate_info() method. If the data is valid it is passed into the create_user methodd
	print '*'*50
	print request
	Course.objects.create_user(request,request.POST)
	return redirect('/courses')



def delete_page(request,number):
	print "--------inside delete.html route----------"
	#this will grab all the data from the User model. It will be stored inside the dictionary context and passed over via the variable context
	print number
	context = {
		'user': Course.objects.get(id=int(number))
	}
	
	return render(request, 'coding_languages/destroy.html', context)

def confirm_delete(request,number):
	# uses the delete_info() method to delete user
	print request

	Course.objects.delete_info(request,request.POST)

	return redirect('/courses')

