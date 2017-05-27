from django.conf.urls import url
from django.http import HttpResponse
from . import views

urlpatterns = [
	url(r'^homepage/$', views.homepage),
	url(r'^send_forum/$', views.send),
]