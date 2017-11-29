from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', view.index, name='index'),
    url(r'^swipes/(?P<netID>[a-zA-Z0-9]+/$)', views.swipe),
    url(r'^users/(?P<netID>[a-zA-Z0-9]+/$)', views.readUser),
    url(r'^users/$', views.createUser)
]
