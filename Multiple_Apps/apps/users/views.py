from django.shortcuts import render, HttpResponse, redirect

  
def index(request):
    response = "I am a user"
    return HttpResponse(response)


def new(request):
	response = "dis is where news users are created"
	return HttpResponse(response)


def register(request):
	response = "this is where you register"
	return HttpResponse(response)



def login(request):
	response = "where 2 log in at"
	return HttpResponse(response)