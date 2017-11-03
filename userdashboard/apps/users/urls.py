from django.conf.urls import url
from . import views           # This line is new!

app_name = "users"
urlpatterns = [
	url(r'^$', views.index, name="index"),
    url(r'^new$', views.new, name="new"),
    url(r'^edit/(?P<number>\d+)$', views.edit, name="edit"),
    url(r'^edit_info/(?P<number>\d+)$', views.edit_info, name="edit_info"),
    url(r'^user_edit/(?P<number>\d+)$', views.user_edit, name="user_edit"),
    url(r'^show/(?P<number>\d+)$', views.show, name="show"),
    url(r'^clear$', views.clear, name="clear"),
    url(r'^remove/(?P<number>\d+)$', views.remove, name="remove"),
    url(r'^confirm_remove/$', views.confirm_remove, name="confirm_remove"),

    #url(r'^remove$', views.remove, name="remove"),

   
   
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


