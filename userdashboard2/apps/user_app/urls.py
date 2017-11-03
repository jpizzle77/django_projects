from django.conf.urls import url
from . import views           # This line is new!

app_name = "user_app"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^sign_in$', views.sign_in, name="sign_in"),
    url(r'^register$', views.register, name="register"),
    url(r'^register_user$', views.register_user, name="register_user"),
    url(r'^login/$', views.login, name="login"),
    url(r'^admin/$', views.admin, name="admin"),
    url(r'^new$', views.new, name="new"),
    url(r'^/$', views.guest, name="guest"),
    #url(r'^show/(?P<number>\d+)$', views.show, name="show"),
    url(r'^edit/(?P<number>\d+)$', views.edit, name="edit"),
    url(r'^edit_info/(?P<number>\d+)$', views.edit_info, name="edit_info"),
    url(r'^edit_password/(?P<number>\d+)$', views.edit_password, name="edit_password"),
    url(r'^edit_level/(?P<number>\d+)$', views.edit_level, name="edit_level"),
    url(r'^remove/(?P<number>\d+)$', views.remove, name="remove"),
    url(r'^confirm_remove/$', views.confirm_remove, name="confirm_remove"),
    url(r'^clear$', views.clear, name="clear"),
  
   

   
    #url(r'^create_user$', views.create_user, name="create_user"),
    #url(r'^register_user$', views.register_user, name="register_user"),
    #url(r'^dashboard$', views.dashboard, name="dashboard"),
    #url(r'^clear$', views.clear, name="clear")
   
    ]