<<<<<<< HEAD
from django.conf.urls import url
from django.http import HttpResponse
from . import views

urlpatterns = [
	url(r'^$', views.homepage),
	url(r'^send_forum/$', views.send),
=======
from django.conf.urls import url
from django.http import HttpResponse
from . import views

urlpatterns = [
	url(r'^homepage/$', views.homepage),
>>>>>>> 6f8334cd8230b93795afd270e036cf1a5c373ed9
]