from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', include('contact_info.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
