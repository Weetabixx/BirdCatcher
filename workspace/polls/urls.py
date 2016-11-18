from django.conf.urls import patterns, include, url
 
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
 
urlpatterns = patterns('',
    # Add the following line to link the root URL to the function myblog.views.index()
    url(r'^$', 'polls.views.index', name='index'),
    # url(r'^myblog/', include('myblog.foo.urls')),
 
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
 
    # Uncomment the next line to enable the admina
    url(r'^admin/', include(admin.site.urls)),
)