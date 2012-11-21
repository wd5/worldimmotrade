# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from django.utils.translation import  ugettext_lazy as _

from world.models import *

class AdminCountry(admin.ModelAdmin):
    search_fields = ['name']

    class Media:
        js = ['/admin_media/tinymce/jscripts/tiny_mce/tiny_mce.js',
              '/admin_media/tinymce_setup/tinymce_setup.js',]
              	
class AdminRegion(admin.ModelAdmin):
    search_fields = ['name', 'id']

class AdminCity(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Country, AdminCountry)
admin.site.register(Region, AdminRegion)
admin.site.register(City, AdminCity)
