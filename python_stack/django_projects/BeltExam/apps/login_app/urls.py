from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'login$', views.logins),
    url(r'log$', views.log),
    url(r'create$', views.Registration),
    url(r'new_user$', views.new_user),
    url(r'(?P<id>\d+)/show$',  views.show),
    # url(r'show$',  views.show),
    url(r'(?P<id>\d+)/new_appointments$', views.Newappointments),
    url(r'(?P<id>\d+)/edit$', views.update),
    url(r'(?P<id>\d+)/delete$', views.delete),
    url(r'(?P<id>\d+)/out$', views.out),
    # url(r'(?P<id>\d+)/showTody$', views.showToday),
    # url(r'(?P<id>\d+)/showOthers$', views.showOthers),
]
