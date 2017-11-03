from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^process$', views.process),
    url(r'^random_word/clear/$', views.clear)
  ]