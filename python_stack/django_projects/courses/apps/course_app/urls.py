from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^/$', views.index),
    url(r'^add$', views.add),
    url(r'^show$', views.show),
    url(r'^(?P<id>\d+)/delete$', views.delete),
    
    # url(r'create$', views.Registration),
    # url(r'out$', views.out),
]