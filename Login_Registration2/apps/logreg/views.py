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

	
	return render(request, 'logreg/index.html')

def register(request, methods='POST'):
	print '------------------------      IN REGISTER ROUTE  (POST)                                ---------------'
	print '*'*50

	if request.method == 'POST':
		response = Login_Reg.objects.check_create(request,request.POST)

		print response, '<----------here is the response'
		if response[0]== False:
			for message in response[1]:
				print "joe mamma"
				messages.error(request, message[1])
			return redirect('logreg_app:index')
		else:
			request.session['message'] = "Successfully Registered!"
			request.session['user']= {
			"id": response[1].id,
			'first_name': response[1].first_name,
			'last_name': response[1].last_name,
			}
			print request.session['user']
			return redirect('logreg_app:home')
		



	return redirect('/')




def login(request, methods='POST'):
	print '------------------------      IN LOGIN ROUTE    (POST)                              ---------------'
	print '*'*50

	if request.method == 'POST':
		response = Login_Reg.objects.check_password(request,request.POST)

		print response, '<----------here is the response'
		if response[0]== False:
			for message in response[1]:
				print "joe mamma"
				messages.error(request, message[1])
			return redirect('logreg_app:index')
		else:
			request.session['message'] = "Successfully Logged In!"
			print request.session['message'] 

			request.session['user']= {
			
			'first_name': response[1].first_name,
			'last_name': response[1].last_name,
			}
			print request.session['user']
			return redirect('logreg_app:home')



	return redirect('/')


def home(request):
	print '----------------            IN THE SHOW.HTML ROUTE          ---------------------'

	print request.session['user']['first_name']





	return render(request,'logreg/home.html')
		

def clear(request):
	print '----------------            CLEARING THE SESSION         ---------------------'

	request.session.clear()

	return redirect('logreg_app:index')

