from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'textapp.views.home', name='url'),
    #home(r'^$', 'textapp.views.send',name='send'),

   # url(r'^applicationsProject/', include('applicationsProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
