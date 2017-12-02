from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^swipes/(?P<netID>[a-zA-Z0-9]+)/$', views.swipe, name='swipe'),
    url(r'^users/(?P<netID>[a-zA-Z0-9]+)/$', views.readUser, name='readUser'),
    url(r'^users/$', views.createUser, name='createUser')
]
