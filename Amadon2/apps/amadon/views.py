from django.shortcuts import render, HttpResponse, redirect
 
def index(request):
	print "-----in the INDEX ROUTE------------"
	try: 
		request.session['total_spent']
		request.session['items_bought']
	except:
		request.session['total_spent'] = 0
		request.session['items_bought'] = 0
	print type(request.session['items_bought'])

	return render(request, 'amadon/index.html')

def process(request, methods='POST'):
	print "-----------in the PROCESS ROUTE-----------"
	request.session['items_bought']=int(request.session['items_bought'])
	print type(request.session['items_bought'])
	product_id = int(request.POST['product_id'])

	if product_id== 1:
		request.session['quantity'] = request.POST['quantity']
		product = "Dojo Cup"
		request.session['total'] =  int(request.session['quantity']) * 4.99
		request.session['total_spent'] += float(request.session['total'])
		request.session['items_bought'] += int(request.session['quantity'])
		print type(request.session['items_bought']), "<----------look at this--------"

	elif product_id == 2:
		request.session['quantity'] = request.POST['quantity']
		product = "Dojo T-Shirt"
		request.session['total'] =  int(request.session['quantity']) * 19.99
		request.session['total_spent'] += float(request.session['total'])
		request.session['items_bought'] += int(request.session['quantity'])

	elif product_id == 3:
		request.session['quantity'] = request.POST['quantity']
		product = "Dojo Sweater"
		request.session['total'] =  int(request.session['quantity']) * 29.99
		request.session['total_spent'] += float(request.session['total'])
		request.session['items_bought'] += int(request.session['quantity'])

	else:
		request.session['quantity'] = request.POST['quantity']
		product = "Algorithm Book"
		request.session['total'] =  int(request.session['quantity']) * 49.99
		request.session['total_spent'] += float(request.session['total'])
		request.session['items_bought'] += int(request.session['quantity'])

	return redirect('/amadon/buy')
	
def buy(request):
	print "---------in the BUY ROUTE--------------"
	return render(request, 'amadon/buy.html')



