# -*- coding: utf-8 -*-
# File for task http://dev.imagecms.net/issues/1316

from django.utils import translation
from django import template
from world.models import Country, City, Region

register = template.Library()

def to_estate_type(type_str):
    from estates.choices import ESTATE_TYPE_CHOICES as etype
    dic = dict(etype)
    result = dic[type_str]
    if result.startswith('--'):
        return result[2:]
    else:
        return result

@register.filter(name='renderMetaDescription')
def renderMetaDescription(data):
	result = {}
	try:
		if data.get('searchByCountry'):
			country = Country.objects.get(pk=data.get('country'))
			result = {
				'ru':u'Недвижимость в %s - на портале зарубежной недвижимости WorldImmotrade.ru. Купить / продажа недвижимости в %s.' % (country.otmenok, country.otmenok),
				'en':u'Real estate in %s - for overseas property portal WorldImmotrade.com. Buy / sell real estate in %s.' % (country.name, country.name),
				'de':u'Immobilien in %s - für ausländische Immobilien-Portal WorldImmotrade.de. Kauf / Verkauf Immobilien in %s.' % (country.name, country.name),			
			}
		if data.get('filterByCity'):
			city = City.objects.get(pk=data.get('city'))
			result = {
				'ru':u'Недвижимость в %s - на портале зарубежной недвижимости WorldImmotrade.ru. Купить / продажа недвижимости в %s.' % (city.name, city.name),
				'en':u'Real estate in %s - for overseas property portal WorldImmotrade.com. Buy / sell real estate in %s.' % (city.name, city.name),
				'de':u'Immobilien in %s - für ausländische Immobilien-Portal WorldImmotrade.de. Kauf / Verkauf Immobilien in %s.' % (city.name, city.name),			
			}
		if data.get('filterByRegion'):
			region = Region.objects.get(pk=data.get('region'))
			result = {
				'ru':u'Недвижимость в %s - на портале зарубежной недвижимости WorldImmotrade.ru. Купить / продажа недвижимости в %s.' % (region.name, region.name),
				'en':u'Real estate in %s - for overseas property portal WorldImmotrade.com. Buy / sell real estate in %s.' % (region.name, region.name),
				'de':u'Immobilien in %s - für ausländische Immobilien-Portal WorldImmotrade.de. Kauf / Verkauf Immobilien in %s.' % (region.name, region.name),			
			}
		if data.get('filterByCountryEndType'):
			country = Country.objects.get(pk=data.get('country'))
			result = {
				'ru':u'%s в %s - на портале зарубежной недвижимости WorldImmotrade.ru. Купить / продажа %s в %s.' % (to_estate_type(data.get('estate_type')), country.otmenok, to_estate_type(data.get('estate_type')).lower(), country.otmenok),
				'en':u'%s in %s - for overseas property portal WorldImmotrade.com. Buy / sell %s in %s.' % (to_estate_type(data.get('estate_type')), country.name, to_estate_type(data.get('estate_type')).lower(), country.name),
				'de':u'%s in %s - für ausländische Immobilien-Portal WorldImmotrade.de. Kauf / Verkauf %s in %s.' % (to_estate_type(data.get('estate_type')), country.name, to_estate_type(data.get('estate_type')).lower(), country.name),
			}
		if data.get('filterByRegionEndType'):
			region = Region.objects.get(pk=data.get('region'))
			result = {
				'ru':u'%s в %s - на портале зарубежной недвижимости WorldImmotrade.ru. Купить / продажа %s в %s.' % (to_estate_type(data.get('estate_type')), region.name, to_estate_type(data.get('estate_type')).lower(), region.name),
				'en':u'%s in %s - for overseas property portal WorldImmotrade.com. Buy / sell %s in %s.' % (to_estate_type(data.get('estate_type')), region.name, to_estate_type(data.get('estate_type')).lower(), region.name),
				'de':u'%s in %s - für ausländische Immobilien-Portal WorldImmotrade.de. Kauf / Verkauf %s in %s.' % (to_estate_type(data.get('estate_type')), region.name, to_estate_type(data.get('estate_type')).lower(), region.name),
			}
		return result.get(translation.get_language(), '')
	except:
		return ''


@register.filter(name='renderFooterLink')
def renderFooter(data):
	try:
		if data.get('main_page'):
			return '<img src="/media/siteimage_mini.png" alt="Создание сайта"><a href="http://www.siteimage.com.ua/" title="Создание сайта" target="_blank">Создание сайта</a> и продвижение сайта.'
		if data.get('show_country_info'):
			return '<img src="/media/siteimage_mini.png" alt="Создание сайтов"><a href="http://www.siteimage.com.ua/" title="Создание сайтов" target="_blank">Создание сайтов</a>, реклама сайта.'
		# Greece objects
		if (data.get('country') == 88 or data.get('country') == '88') and data.get('on_object_view') :
			return '<img src="/media/siteimage_mini.png" alt="Разработка сайтов"><a href="http://www.siteimage.com.ua/" title="Разработка сайтов" target="_blank">Разработка сайтов</a>, аналитика сайта.'
		# Bolgaria
		if data.get('country') == 23 or data.get('country') == '23':
			return '<img src="/media/siteimage_mini.png" alt="интернет агентство"><a href="http://www.siteimage.com.ua/" title="интернет агентство" target="_blank">Интернет агентство</a>, реклама в интернете.'
		# Vengria
		if data.get('country') == 99 or data.get('country') == '99':
			return '<img src="/media/siteimage_mini.png" alt="раскрутка сайтов"><a href="http://www.siteimage.com.ua/raskrutka-sajtov-main" title="раскрутка сайтов" target="_blank">Раскрутка сайтов</a>, создание сайта.'
		# Germany
		if data.get('country') == 56 or data.get('country') == '56':
			return '<img src="/media/siteimage_mini.png" alt="продвижение сайтов"><a href="http://www.siteimage.com.ua/raskrutka-sajtov-main" title="продвижение сайтов" target="_blank">Продвижение сайтов</a>, разработка сайта.'
		# Greece		
		if data.get('country') == 88 or data.get('country') == '88':
			return '<img src="/media/siteimage_mini.png" alt="раскрутка сайта"><a href="http://www.siteimage.com.ua/raskrutka-sajtov-main" title="раскрутка сайта" target="_blank">Раскрутка сайта</a>, SEO компания "Сайт Имидж".'		
		# Spain
		if data.get('country') == 67 or data.get('country') == '67':
			return '<img src="/media/siteimage_mini.png" alt="продвижение сайта"><a href="http://www.siteimage.com.ua/raskrutka-sajtov-main" title="продвижение сайта" target="_blank">Продвижение сайта</a>, SEO оптимизация сайта.'
		# Kipr		
		if data.get('country') == 54 or data.get('country') == '54':
			return '<img src="/media/siteimage_mini.png" alt="интернет реклама"><a href="http://www.siteimage.com.ua/raskrutka-sajtov/kompleksnoe-prodvizhenie" title="интернет реклама" target="_blank">Интернет реклама</a>, www.siteimage.com.ua.'
		# Россия
		if data.get('country') == 191 or data.get('country') == '191':
			return '<img src="/media/siteimage_mini.png" alt="реклама в интернет"><a href="http://www.siteimage.com.ua/raskrutka-sajtov/kompleksnoe-prodvizhenie" title="реклама в интернет" target="_blank">Реклама в интернет</a>, поисковый аудит сайта.'
		# Чешская республика
		if data.get('country') == 55 or data.get('country') == '55':
			return '<img src="/media/siteimage_mini.png" alt="оптимизация сайта"><a href="http://www.siteimage.com.ua/raskrutka-sajtov/optimizacija-sajta" title="оптимизация сайта" target="_blank">Оптимизация сайта</a>, реклама в интернете.'
		# Словакия		
		if data.get('country') == 202 or data.get('country') == '202':
			return '<img src="/media/siteimage_mini.png" alt="поисковая оптимизация сайта"><a href="http://www.siteimage.com.ua/raskrutka-sajtov/optimizacija-sajta" title="поисковая оптимизация сайта" target="_blank">Поисковая оптимизация сайта</a> от "Сайт Имидж".'
	except:
		pass

	return '<img src="/media/siteimage_mini.png" alt="Разработка сайта"><a href="http://www.siteimage.com.ua/" title="Разработка сайта" target="_blank">Разработка сайта</a> и раскрутка сайта.'