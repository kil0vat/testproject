from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', include('ticket1.contact_info.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
