from django.conf.urls import url
from . import views

urlpatterns = [
    #/reportLost/
    url(r'^$', views.reportLost, name='reportLost'),
]
