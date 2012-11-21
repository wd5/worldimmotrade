# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from world.models import Country, Region, City

# Monkeypath
User._meta.get_field_by_name('username')[0].max_length=75

TREATMENT_CHOICES = (
    (u'mr', _(u"Господин")),
    (u'mrs', _(u"Госпожа")),
)

PERSONAL_INFO_DISPLAY = (
    (u"1", _(u"Только Фамилия и номер телефона")),
    (u"2", _(u"Только Фамилия и электронный адрес")),
    (u"3", _(u"Фамилия, номер телефона и E-Mail")),
    (u"full", _(u"Полные контактные данные")),
    (u"nothing", _(u"Ничего")),
    )

class UserProfile(models.Model):
    user               = models.ForeignKey(User)
    # Determinates is user saler or searcher
    is_saler           = models.BooleanField(default=0)
    treatment          = models.CharField(_(u"Обращение"), max_length=3, choices=TREATMENT_CHOICES)
    company_name       = models.CharField(_(u"Название фирмы"), max_length=255, blank=True, null=True)
    first_name         = models.CharField(_(u"Имя"), max_length=255)
    last_name          = models.CharField(_(u"Фамилия"), max_length=255)
    address            = models.CharField(_(u"Улица, номер дома"), max_length=255, blank=False, null=True)
    post_code          = models.CharField(_(u"Почтовый индекс"), max_length=50, blank=False, null=True)
    country            = models.ForeignKey(Country, blank=True, null=True)
    region             = models.ForeignKey(Region,blank=True, null=True)
    city               = models.ForeignKey(City, blank=True, null=True)
    contact_lang       = models.CharField(_(u"Ваш контактный язык"), max_length=100, blank=True, null=True)
    phone              = models.CharField(_(u"Телефон"), max_length=50)
    mobile_phone       = models.CharField(_(u"Мобильный телефон"), max_length=50, blank=True, null=True)
    fax_number         = models.CharField(_(u"Номер факса"), max_length=50, blank=True, null=True)
    email              = models.EmailField(_(u"Электронный адрес"), max_length=255)
    personal_info_show = models.CharField(_(u"Отображение контактных данных"), max_length=8, choices=PERSONAL_INFO_DISPLAY)
    receive_mails      = models.BooleanField(_(u"Получать новости и акции"), default=0)

    def full_name(self):
       return "%s %s" % (self.first_name, self.last_name)

    def apartament_count(self):
        from estates.models import  Apartament
        return Apartament.objects.filter(user=self.user).count()
	
    def display_info(self):
        if self.personal_info_show == u"1":
            return (self.last_name, self.phone)
        elif self.personal_info_show == u"2":
            return (self.last_name, self.email)
        elif self.personal_info_show == u"3":
            return (self.last_name, self.phone, self.email)
        elif self.personal_info_show == u"full":
            return (self.company_name, self.first_name +' '+ self.last_name, self.phone, self.email)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


    class Meta:
        verbose_name = _(u"Профиль пользователя")
        verbose_name_plural = _(u"Профили пользователей")
