

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect

  
def index(request):
    response = "this is a survey!"
    return HttpResponse(response)
    
def new(request):
	response = "where to create new surveys"
	return HttpResponse(response)