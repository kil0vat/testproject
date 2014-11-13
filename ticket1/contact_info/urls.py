from django.conf.urls.defaults import patterns, url
from ticket1.contact_info import views

urlpatterns = patterns('',
	url(r'^$', views.base, name='Base'),
)
