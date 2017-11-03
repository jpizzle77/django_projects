from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^destroy/(?P<number>\d+)$', views.delete_page),
     url(r'^confirm_delete/(?P<number>\d+)$', views.confirm_delete)
    ]
'''
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<number>\d+)$', views.show_id),
    url(r'^(?P<number>\d+)/edit$', views.edit_number),
    url(r'^(?P<number>\d+)/edited_info$', views.edited_info),
    url(r'^(?P<number>\d+)/delete$', views.delete),
    url(r'^(?P<number>\d+)/confirm_delete$', views.confirm_delete)
'''