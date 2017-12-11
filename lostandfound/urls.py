from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^swipes/(?P<netID>[a-zA-Z0-9]+)/$', views.swipe, name='swipe'),
    url(r'^reportLost/$', views.reportLost, name='reportLost'),
]
