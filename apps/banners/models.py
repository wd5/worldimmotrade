# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

class Banner(models.Model):
    ''' Model to manage banners '''
    name = models.CharField(_(u"Название"), max_length=100)
    position = models.CharField(_(u"Позиция"), max_length=100)
    code = models.TextField(_(u"Код"), blank=True, null=True, default="")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u"Баннер")
        verbose_name_plural = _(u"Баннеры")


class BannerAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']

admin.site.register(Banner, BannerAdmin)