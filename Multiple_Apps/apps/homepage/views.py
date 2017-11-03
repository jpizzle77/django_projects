from django.shortcuts import render, HttpResponse, redirect

  
def index(request):

	try:
		request.session['name']
	except:
		request.session['name']=""

	return render(request, 'homepage/index.html')