from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
from django.utils.crypto import get_random_string

def index(request):
	print "<======= inside the INDEX==========>"
	try:
		request.session['attempt']+=1
	except:
		request.session['attempt']=1

	print request.session['attempt']
	
	return render(request, 'random_word/index.html')



def process(request, methods='POST'):
	print "<======= inside the PROCESS==========>"
	unique_id = get_random_string(length=14)
	request.session['random']= unique_id
	print request.session['random'], "<--------------------session['random']"
	
	return redirect('/')



def clear(request, methods='POST'):
	print "<======= inside the CLEAR ROUTE==========>"
	del request.session['random']
	del request.session['attempt']
	
	return redirect('/')