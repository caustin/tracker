from django.conf.urls import patterns, include, url
from django.contrib import admin

import thirdparty.urls
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^thirdparty/', include(thirdparty.urls)),
)
