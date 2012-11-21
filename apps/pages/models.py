# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from world.models import Country

class StaticPage(models.Model):
    ''' Model for manage static pages '''
    title = models.CharField(_(u"Название"), max_length=500)
    url = models.SlugField(_(u"URL"))
    content = models.TextField(_(u"Содержание"))
    created = models.DateTimeField(_(u"Создано"), auto_now_add=True)
    updated = models.DateTimeField(_(u"Обновлено"), auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u"Статическая страница")
        verbose_name_plural = _(u"Статические страницы")

class News(models.Model):
    ''' News model '''
    title = models.CharField(_(u"Название"), max_length=500)
    content = models.TextField(_(u"Содержание"), )
    created = models.DateTimeField(_(u"Создано"), auto_now_add=True)
    updated = models.DateTimeField(_(u"Обновлено"), auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u"Новость")
        verbose_name_plural = _(u"Новости")
        ordering = ['-created']


class CountryInfo(models.Model):
    ''' Holds info about cocuntry '''
    country = models.ForeignKey(Country)
    content = models.TextField(_(u"Содержание"), blank=True, null=True, default="")

    class Meta:
        verbose_name = _(u"Информация о стране")
        verbose_name_plural = _(u"Информация о странах")
