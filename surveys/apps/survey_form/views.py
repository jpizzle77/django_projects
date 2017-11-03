from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
	try:
		request.session['count']+=1

	except:
		request.session['count']=1
    
    	return render(request, 'survey_form/index.html')



def process(request, methods='POST'):
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']
	print request.session['name']
	print request.session['location']
	print request.session['language']
	print request.session['comment']
	return redirect('/results')
	

def results(request):
	 return render(request, 'survey_form/results.html')