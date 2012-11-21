# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from estates.models import *

class Country(models.Model):
    name = models.CharField(_(u"Название"), max_length=200)
    h1 = models.TextField(_(u"H1"), blank=True, null=True)
    # Display under h1
    seo_desc = models.TextField(_(u"Seo текст"), blank=True, null=True)
    title = models.CharField(_(u"Seo Title"), blank=True, null=True,  max_length=255)
    otmenok = models.CharField(_(u"Радительский отменак"), blank=True, null=True,  max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _(u"Страна")
        verbose_name_plural = _(u"Страны")

class Region(models.Model):
    country = models.ForeignKey(Country)
    name = models.CharField(_(u"Название"), max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _(u"Регион")
        verbose_name_plural = _(u"Регионы")

class City(models.Model):
    country = models.ForeignKey(Country)
    region = models.ForeignKey(Region)
    name = models.CharField(_(u"Название"), max_length=200, db_index=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = _(u"Город")
        verbose_name_plural = _(u"Города")
