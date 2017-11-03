from django.shortcuts import render, HttpResponse, redirect

  
def index(request):
    
    print request.GET
    print '!'* 50
    return render(request, 'blogs/index.html')



def create(request, methods='POST'):
	print '*'* 50
	print request.POST
	request.session['name'] = request.POST['name']
	request.session['desc'] = request.POST['desc']
	print request.session['name']
	print request.session['desc']
	response = "time to create!"
	return redirect('/')

def new(request):
	response = "placeholder to display a new form to create a new blog"

	return HttpResponse(response)

def show_id(request,number):
	
	response = "The number is...." + number
	return HttpResponse(response)



def show_word(request,word):
	print  request.POST['desc']
	response = "Bird is the...." + word
	return HttpResponse(response)

def edit_number(request,number):
	
	response = "display placeholder to edit blog " + number
	return HttpResponse(response)

def destroy(request,number):
	
	response = "delete blog # " + number + "?"
	return HttpResponse(response)
	#return redirect('/blogs')