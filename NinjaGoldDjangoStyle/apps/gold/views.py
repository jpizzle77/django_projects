from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
import time
import datetime
import random
 
def index(request):
	try:
		request.session['total']
	except:
		request.session['total']=0
	return render(request, 'gold/index.html')


def process(request):
	print "-------------------------------------Post route-------------------------------------"
	#this code tells you what form they submitted (Farm,Cave,House,Casino). It sets that value to session['earn']
	

	message =''
	ts = time.time()
	print ts
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	print st
	request.session['time'] = st
	
	if request.POST['earn'] == 'farm':
		gold = random.randrange(10, 20)
		request.session['total'] += gold
		request.session['color'] = 'green'
		
	elif request.POST['earn'] == 'cave':
		gold = random.randrange(5,10)
		request.session['total'] += gold
		request.session['color'] = 'green'
		

	elif request.POST['earn'] == 'house':
		gold = random.randrange(2, 5)
		request.session['total'] += gold
		request.session['color'] = 'green'
		

	else:
		gold = random.randrange(-1, 1)
		print gold
		if gold > 0:
			request.session['color'] = 'green'
			request.session['total'] += gold
			
		elif gold < 0:
			request.session['color'] = 'red'
			request.session['total'] += gold
			
		else:
			request.session['color'] = 'blue'
			request.session['total'] += gold
			
	print request.session['total']

	context = {

  	
  	"gold": gold,
  	"color" : request.session['color'],
  	"total": request.session['total'],
  	"place": request.POST['earn'], 
  	"time" : request.session['time']
  	}

  	try: 
		request.session['messages']
	except:
		request.session['messages']=[]

	word_list = request.session['messages']
	word_list.append(context)
	request.session['messages']= word_list

	return redirect('/')

def reset(request):
	del request.session['messages']
	del request.session['total']

	return redirect('/')
