from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.PinsDisplay, name='PinsDisplay'),
	url(r'^(?P<id>[0-9]+)/$', views.PinDescription, name='PinDescription'),
]