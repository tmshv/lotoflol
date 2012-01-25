from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from firsttouch.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'inspire.views.home', name='home'),
    # url(r'^inspire/', include('inspire.foo.urls')),
    (r'^lol/first', first_hello),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^inspire/admin/', include(admin.site.urls)),
)
