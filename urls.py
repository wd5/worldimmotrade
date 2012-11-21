# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import  settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^$', 'estates.views.index'),
    url(r'^migrate/$', 'estates.views.migrate'),
    url(r'^search/$', 'estates.views.search', {'students':False}, name='search'),
    url(r'^search/students/$', 'estates.views.search', {'students':True}, name='search-students'),
    (r'^user/', include('users.urls')),
    (r'^tarifs/', include('tarifs.urls')),
    (r'^pricing/', 'pages.views.pricing'),
    (r'^estates/', include('estates.urls')),
    (r'^world/', include('world.urls')),
    (r'^admin/', include(admin.site.urls)),
    #Converter
    url(r'^ajax_converter/$', 'pages.views.convert',name='ajax-converter'),
    # Pages app
    url(r'^page/organisation/$', 'pages.views.organisation', name='page-organisation'),
    url(r'^page/(.+)/$', 'pages.views.show_page', name='view-page'),
    url(r'^news/$', 'pages.views.show_all_news', name='view-all-news'),
    url(r'^news/(\d+)/$', 'pages.views.show_news_page', name='view-news'),
    url(r'^country/(\d+)/$', 'pages.views.show_country_info', name='country-info'),
    url(r'^contacts/$', 'pages.views.contacts', name='view-contacts'),
    url(r'^services/(.+)/$', 'pages.views.iframe_page'),
    (r'^messages/', include('django_messages.urls')),
    (r'^grappelli/', include('grappelli.urls')),

    (r'^password/reset/$', 'django.contrib.auth.views.password_reset',
    {'post_reset_redirect' : '/password/reset/done/'}),
    (r'^password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    (r'password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm',
    {'post_reset_redirect' : '/password/done/'}),
    (r'^password/done/$', 'django.contrib.auth.views.password_reset_complete'),

    (r'^companies/$', 'users.views.companiesList'),

    ##################################

    (r'^search/country/(?P<country>\d+)-(?P<slug>.+)/$', 'estates.views.searchByCountry'),
    url(r'^(?P<estate_type>.*)-in-region-(?P<region>\d+)/$', 'estates.views.filterByRegionEndType', name='filterByRegionEndType'),
    # Created in second box in search sidebar
    url(r'^(?P<estate_type>\w+)-in-(?P<country>\d+)-(.+)/$', 'estates.views.filterByCountryEndType', name='filterByCountryEndType'),
    url(r'^rent-(?P<estate_type>\w+)-in-(?P<country>\d+)-(.+)/$', 'estates.views.filterRentByCountryEndType', name='filterRentByCountryEndType'),
    url(r'^country-(?P<country_id>\d+)-(.+)/city-(?P<city_id>\d+)$', 'estates.views.filterByCity', name='filterByCity'),
    url(r'^country-(?P<country_id>\d+)-(.+)/region-(?P<region_id>\d+)$', 'estates.views.filterByRegion', name='filterByRegion'),
    url(r'^estate-type-(?P<estate_type>\w+)$', 'estates.views.filterByEstateType', name='filterByEstateType'),

    (r'^robots.txt$', 'estates.views.robots'),
    (r'^googled5314acba1fdabf8.html$', 'django.views.static.serve', {'path':"/googled5314acba1fdabf8.html",'document_root': settings.MEDIA_ROOT,'show_indexes': False }),
    (r'^cmsmagazine5dbde1f1d2f07da9d8519fcfe2f0e8b5.txt$', 'django.views.static.serve', {'path':"/cmsmagazine5dbde1f1d2f07da9d8519fcfe2f0e8b5.txt",'document_root': 
settings.MEDIA_ROOT,'show_indexes': False }),

)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

# rosetta
#from django.conf import settings
#if 'rosetta' in settings.INSTALLED_APPS:
#    urlpatterns += patterns('',
#        url(r'^rosetta/', include('rosetta.urls')),
#    )
