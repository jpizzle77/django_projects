'''from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited


def index(request):
	response = "time display!"
	return render(request,'time_display/index.html')
'''
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime


def index(request):
  context = {
  "time": strftime("%b-%d-%Y %H:%M %p", gmtime())
  }
  return render(request,'time_display/index.html', context)