# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^load_json/$', 'world.views.load_json'),
    (r'^autocomplete/$', 'world.views.autocomplete'),
)
