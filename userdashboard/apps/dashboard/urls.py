from django.conf.urls import url
from . import views           # This line is new!

app_name = "dashboard"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^admin$', views.admin, name="admin"),
    url(r'^edit/$', views.edit, name="edit"),
    url(r'^edit_info/$', views.edit_info, name="edit_info"),
    url(r'^show/(?P<number>\d+)$', views.show, name="show"),
    url(r'^description/$', views.description, name="description"),
    
    
   
    ]
''' userdash:index    
    	userdash:signin
    	userdash:login
    	userdash:register
    	userdash:register_user'''

''' dashboard:index
    	dashboard:admin '''



''' users:index 
        users:new 
        users:edit 
        users:edit_info
        users:user_edit
        users:show
        users:clear
        users:remove
        users:confirm_remove'''
