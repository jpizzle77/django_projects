from django.conf.urls import url

from . import views           # This line is new!
  

urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    #url(r'^/', views.blogs),
    url(r'^create/', views.create),
    url(r'^new/', views.new),
    url(r'^(?P<number>\d+)$', views.show_id),
    url(r'^(?P<word>\w+)$', views.show_word),
    url(r'^(?P<number>\d+)/edit$', views.edit_number),
    url(r'^(?P<number>\d+)/delete$', views.destroy)
   
  ]




'''/blogs - display "placeholder to later display all the list of blogs" via HttpResponse. Have this be handled by a method named 'index'.
/blogs/new - display "placeholder to display a new form to create a new blog" via HttpResponse. Have this be handled by a method named 'new'.
/blogs/create - Have this be handled by a method named 'create'.  For now, have this url redirect to /blogs.
/blogs/{{number}} - display 'placeholder to display blog {{number}}.  For example /blogs/15 should display a message 'placeholder to display blog 15'.  Have this be handled by a method named 'show'.
/blogs/{{number}}/edit - display 'placeholder to edit blog {{number}}.  Have this be handled by a method named 'edit'.
/blogs/{{number}}/delete - Have this be handled by a method named 'destroy'. For now, have this url redirect to /blogs. 


 '''