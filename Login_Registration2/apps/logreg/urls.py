from django.conf.urls import url
from . import views           # This line is new!

app_name = "logreg_app"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register$', views.register, name="register"),
    url(r'^login$', views.login, name="login"),
    url(r'^home$', views.home, name="home"),
     url(r'^clear$', views.clear, name="clear"),
   
    ]