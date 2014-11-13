from django.conf.urls import patterns, url
from contact_info import views

urlpatterns = patterns('',
	url(r'^$', views.base, name='Base'),
)
