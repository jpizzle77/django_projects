from django.shortcuts import render, HttpResponse, redirect
from models import Login_Reg
from django.contrib import messages

  # the index function is called when root is visited

def index(request):
	print "--------inside INDEX route----------"

	
	#this will grab all the data from the User model. It will be stored inside the dictionary context and passed over via the variable context
	'''context = {
		'users': Course.objects.all()
	}'''

	
	return render(request, 'log_reg/index.html')

def success(request):
	return render(request, 'log_reg/success.html')


def register(request, methods='POST'):
	print '------------------------      IN PROCESS ROUTE                                   ---------------'
	print '*'*50
	print request

	errs= Login_Reg.objects.validate_info(request,request.POST)
	print errs

	if errs: 
		for err in errs:
			messages.error(request, err)
			# return "here" will only show 1 message
		return redirect('/')
	else:
		new_user = Login_Reg.objects.create_user(request,request.POST)
		request.session['id'] = new_user.id
		request.session['first_name'] = new_user.first_name
		messages.success(request, "Thank you {} for registering".format(new_user.first_name))
		return render(request, 'log_reg/success.html')

	


def login(request, methods='POST'):
	print '-------------CHECK PASSWORD ROUTE--------------'

	password = request.POST['password']
	print password
	
	check_hashed_pw = Login_Reg.objects.check_password(request,request.POST)

	if check_hashed_pw:
		return redirect('/success')
	else:
		return redirect('/')
	
