# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django import forms

from pages.models import News, StaticPage, CountryInfo

class StaticPageAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StaticPageAdminForm, self).__init__(*args, **kwargs)
        self.fields['title_ru'].required = True
        self.fields['content_ru'].required = True

    class Meta:
        exclude = ['title', 'content']

class CountryInfoAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CountryInfoAdminForm, self).__init__(*args, **kwargs)
        self.fields['content_ru'].required = True
        self.fields['country'].label = _(u"Страна")

    class Meta:
        exclude = ['content']


class AdminNews(admin.ModelAdmin):
    list_display = ['title', 'created','updated']
    form = StaticPageAdminForm

class AdminStaticPage(admin.ModelAdmin):
    form = StaticPageAdminForm

    class Media:
        js = ['/admin_media/tinymce/jscripts/tiny_mce/tiny_mce.js',
              '/admin_media/tinymce_setup/tinymce_setup.js',]

class AdminCountryInfo(admin.ModelAdmin):
    list_display = ['country']
    form = CountryInfoAdminForm

    class Media:
        js = ['/admin_media/tinymce/jscripts/tiny_mce/tiny_mce.js',
              '/admin_media/tinymce_setup/tinymce_setup.js',]


admin.site.register(News,AdminNews)
admin.site.register(StaticPage, AdminStaticPage)
admin.site.register(CountryInfo, AdminCountryInfo)
