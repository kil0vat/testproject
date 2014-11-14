from django.conf.urls.defaults import patterns, url
from src.contact_info import views

urlpatterns = patterns('',
	url(r'^$', views.base, name='Base'),
)
