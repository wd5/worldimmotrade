# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

# Deprecated
urlpatterns = patterns('',
    url(r'^page/(.+)/$', 'pages.views.show_page'),
    url(r'^news/(\d+)/$', 'pages.views.show_news_page'),
)
