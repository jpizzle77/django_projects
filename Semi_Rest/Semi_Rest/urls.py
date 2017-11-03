"""Semi_Rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include # Notice we added include
from django.contrib import admin
urlpatterns = [
      url(r'^', include('apps.friends.urls')),
       url(r'^users/', include('apps.friends.urls')),
      
  ]

'''
@app.route('/')
@app.route('/friends', methods=['POST'])
@app.route('/friends/<id>/edit')
@app.route('/friends/<id>', methods=['POST'])
@app.route('/friends/<id>/delete', methods=['POST'])'''