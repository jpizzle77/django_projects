from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
	return render(request, 'session_words/index.html')

def process(request, methods='POST'):

	try: 
		font_size = request.POST['big_font']
	except:
		font_size ='small'

	text = request.POST['text']

	if font_size =='small':
		text=request.POST['text']
	else:
		text= text.upper()
		
	if request.POST['color']== 'red':
		color= 'red'
	elif request.POST['color']== 'blue':
		color= 'blue'
	else:
		color= 'green'
	
	context = {

  	"time": strftime("%b-%d-%Y %H:%M %p", gmtime()),
  	"text" : text,
  	"size": font_size,
  	"color": color
  	}
	
	try: 
		request.session['words']
	except:
		request.session['words']=[]

	word_list = request.session['words']
	word_list.append(context)
	request.session['words']= word_list
	
	return redirect('/')


def clear(request):
	print 'in the clear', "!"* 50
	del request.session['words']
	
	return redirect('/')