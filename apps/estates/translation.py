# -*- coding: utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions

from estates.models import Apartament, EstateTypeSeoText
from pages.models import StaticPage, News, CountryInfo
from banners.models import Banner
from world.models import Country

class ApartamentTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'object_location')

class StaticPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

class BannerTranslationOptions(TranslationOptions):
    fields = ['code']

class CountryInfoTranslationOptions(TranslationOptions):
    fields = ['content']

class CountryTranslationOptions(TranslationOptions):
    fields = ['name', 'h1', 'title']

class EstateTypeSeoTextTranslationOptions(TranslationOptions):
    fields = ['description']

translator.register(Apartament, ApartamentTranslationOptions)
translator.register(StaticPage, StaticPageTranslationOptions)
translator.register(News, NewsTranslationOptions)
translator.register(Banner, BannerTranslationOptions)
translator.register(CountryInfo, CountryInfoTranslationOptions)
translator.register(Country, CountryTranslationOptions)
translator.register(EstateTypeSeoText, EstateTypeSeoTextTranslationOptions)