from django.conf.urls import url
from . import views           # This line is new!

app_name = "comment_app"

urlpatterns = [
    url(r'^/$', views.guest, name="guest"), #NOTE:  DON'T FORGET A '/' before the '$' symbol. Kept redirecting me to the index page, instead of here
    url(r'^edit/$', views.edit, name="edit"),
    url(r'^edit_info/$', views.edit_info, name="edit_info"),
    url(r'^edit_password/$', views.edit_password, name="edit_password"),
    url(r'^show/(?P<number>\d+)$', views.show, name="show"),
    url(r'^description/$', views.description, name="description"),
    url(r'^comment/$', views.comment, name="comment"),
    url(r'^reply/$', views.reply, name="reply"),
   
    ]