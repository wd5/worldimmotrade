# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from django.utils.translation import  ugettext_lazy as _

from users.models import UserProfile
from world.models import *

class UserProfileAdminForm(forms.ModelForm):
    """ Saler register form """
    def __init__(self, *args, **kwargs):
        super(UserProfileAdminForm, self).__init__(*args, **kwargs)
        if self.instance is None and len(self.data) == 0:
            self.fields['region'].queryset = Region.objects.filter(country=0)
            self.fields['city'].queryset = City.objects.filter(region=0)
        if self.instance.id and len(self.data) == 0:
            self.fields['region'].queryset = Region.objects.filter(country=self.instance.country)
            self.fields['city'].queryset = City.objects.filter(region=self.instance.region)
        if len(self.data) > 0:
            self.fields['region'].queryset = Region.objects.filter(country=self.data.get('country') or 0)
            self.fields['city'].queryset = City.objects.filter(region=self.data.get('region') or 0)

    region = forms.ModelChoiceField(queryset=Region.objects.filter(id=0))
    city = forms.ModelChoiceField(queryset=Region.objects.filter(id=0))

    class Media:
        js = ('/media/jquery/js/jquery-1.4.4.min.js',
              '/media/scripts/jquery.relatedselects.min.js',
              '/media/adminScripts/usersForm.js',
        )

class AdminUserProfile(admin.ModelAdmin):
    list_filter = ['is_saler']
    list_display = ['full_name','apartament_count', 'is_saler']
    form = UserProfileAdminForm


admin.site.register(UserProfile, AdminUserProfile)
