# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'tarifs.views.index', name='choose-tarif'),
    url(r'^select/$', 'tarifs.views.select_tarif', name='tarif-select'),
    url(r'^confirmed/$', 'tarifs.views.confimed', name='tarif-confirmed'),
    url(r'^pay/$', 'tarifs.views.show_pay_page', name='tarif-paypage'),
    url(r'^cancel/$', 'tarifs.views.cancel_request', name='tarif-cancel'),
)