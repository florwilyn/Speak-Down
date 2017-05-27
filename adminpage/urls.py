from django.conf.urls import url
from django.http import HttpResponse
from . import views

urlpatterns = [
	url(r'^admin/home/$', views.homepage, name='admin_page'),
	url(r'^approve/$', views.approve, name='approve'),
	url(r'^delete/$', views.delete, name='delete'),
	url(r'^sign-in/$', views.sign_in, name='sign_in'),
	url(r'^sign-out/$', views.sign_out, name='sign_out')

]