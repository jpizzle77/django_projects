from django.conf.urls import url
from . import views           # This line is new!

app_name = "userdash"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^signin$', views.signin, name="signin"),
    url(r'^login/$', views.login, name="login"),
    url(r'^register$', views.register, name="register"),
    url(r'^create_user$', views.create_user, name="create_user"),
    url(r'^register_user$', views.register_user, name="register_user"),
    #url(r'^dashboard$', views.dashboard, name="dashboard"),
    #url(r'^clear$', views.clear, name="clear"),
   
    ]

'''     userdash:index    
    	userdash:signin
    	userdash:login
    	userdash:register
    	userdash:register_user'''

'''     dashboard:index
        dashboard:admin '''


'''     users:index 
        users:new 
        users:edit 
        users:edit_info
        users:user_edit
        users:show
        users:clear
        users:remove
        users:confirm_remove'''
