from django.conf.urls import url
from . import views           # This line is new!

app_name = "log_reg_app"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register$', views.register, name="register"),
    url(r'^login$', views.login, name="success"),
     url(r'^check_password$', views.check_password, name="check_password"),
    
    ]



'''
    url(r'^destroy/(?P<number>\d+)$', views.delete_page),
    url(r'^confirm_delete/(?P<number>\d+)$', views.confirm_delete)'''