# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^register/type/$', 'users.views.choose_type', name='users-register-select'),
    url(r'^register/$', 'users.views.register', {'saler': True}, name='users-register'),
    url(r'^register/user/$', 'users.views.register', {'saler': False}, name='users-register'),
    url(r'^login/$', 'users.views.login', name='users-login'),
    url(r'^logout/$', 'users.views.logout', name='users-logout'),
    url(r'^thanks/$', 'users.views.thanks', name='users-thanks'),
    url(r'^edit_profile/$', 'users.views.edit_profile', name='users-edit-profile'),
    url(r'^change-currency/$', 'users.views.change_currency', name='users-change-currency'),
)