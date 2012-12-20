# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^create/$', 'estates.views.create', name='apartment-create'),
    url(r'^create_xml/$', 'estates.views.create_xml_objects', name='create-appartments-via-xml'),
    url(r'^list/$', 'estates.views.estates_list', name='apartment-list'),
    url(r'^edit/(\d+)/$', 'estates.views.edit', name='apartment-edit'),
    url(r'^view/(\d+)/$', 'estates.views.view', name='apartment-view'),
    url(r'^bookmark/(\d+)/$', 'estates.views.add_to_bookmarks', name='apartment-bookmark'),
    url(r'^bookmark_delete/(\d+)/$', 'estates.views.remove_from_bookmarks', name='apartment-bookmark-remove'),
    url(r'^bookmarks/$', 'estates.views.bookmarks', name='bookmarks'),
    url(r'^cart/$', 'estates.views.cart', name='cart'),
    url(r'^publish/$', 'estates.views.publish', name='publish'),
    url(r'^unpublish/$', 'estates.views.unpublish', name='unpublish'),
    url(r'^delete/$', 'estates.views.delete', name='delete-apartment'),
	# openimmo
    url(r'^openimmo/$', 'estates.openimmo.upload', name='openimmo-page'),
    url(r'^xmlse/$', 'estates.views.xmlse', name='xmlse-s'),
)

