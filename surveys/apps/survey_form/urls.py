from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index), 
    url(r'^process$', views.process),
    url(r'^results$', views.results),   # This line has changed!
  ]