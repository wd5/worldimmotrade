# -*- coding: utf-8 -*-
# Tariff model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from users.models import UserProfile

class Tarif(models.Model):
    ''' Manages site tarifs '''
    name = models.CharField(_(u"Название"), max_length=50)
    price = models.FloatField(_(u"Цена"))
    price_per_ad = models.FloatField(_(u"Цена за объявление"))
    ad_count = models.PositiveIntegerField(_(u"Количество объектов"))
    unlimited = models.BooleanField(_(u"Количество объектов неограничено"), default=False)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['ad_count']
        verbose_name = _(u"Тариф")
        verbose_name_plural = _(u"Тарифы")

class TarifRequests(models.Model):
    ''' Saves users selected tarifs.
        Row must be deleted after time exceeded.
    '''
    user = models.ForeignKey(UserProfile)
    tarif = models.ForeignKey(Tarif)
    months_count = models.PositiveIntegerField(_(u"Количество месяцев"), max_length=2)
    paid = models.BooleanField(_(u"Оплачен"), default=False)
    start_date = models.DateField(_(u"Дата начала"), blank=True, null=True)
    end_date = models.DateField(_(u"Дата окончания"), blank=True, null=True)

    class Meta:
        verbose_name = _(u"Запрос тарифа")
        verbose_name_plural = _(u"Запросы тарифов")
