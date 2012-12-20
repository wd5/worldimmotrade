# -*- coding: utf-8 -*-
import time
import datetime

from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django_messages.models import Message

from annoing.currencyManager import currencyManager
from estates.forms import ApartmentForm, PhotoForm, SearchForm, ApartmentViewForm, SearchFormMini
from pages.forms import ContactForm
from pages.models import StaticPage
from estates.models import Apartament, Photo, Bookmarks, Document
from users.models import UserProfile

import random

def xmlse(request):
    pass
    # from estates.xmlse import XMLSe as XMLSe
    # parser = XMLSe('/srv/www/vhosts/worldimmotrade.ru/httpdocs/immotrade/export.xml')
    # parser.parse()

def active_lang():
    return translation.get_language()

def current_language(request):
    lang = ''
    host = request.get_host()
    if host.endswith('.com'):
        lang='en'
    if host.endswith('.de'):
        lang='de'        
    if host.endswith('.ru'):
        
        lang='ru'
        
    return lang

def get_active_title(choices):
    return choices.get(active_lang())

def get_country_from_url(request):
    country_id = 0
    try:
        country_id = request.GET.get('country', 0)
    except:
        pass

    try:
        test = request.META['PATH_INFO'].split('-')
        test2 = test[0].split('/')[-1]
    
        if int(test2) > 0:
            country_id = int(test2)
    except:
        pass

    return country_id

def index(request):
    """ Display site main page """
    form = SearchForm()
   
    form2 = SearchFormMini(request=request)
    objects = Apartament.objects.filter(show_on_start_page=True, is_published=True).all()

    return direct_to_template(request, 'start_page.html', {
        'form': form,
        'form2': form2,
        'objects':objects,
        'data': {'main_page': True},
		'main_text': get_object_or_404(StaticPage, pk=10)
    })

def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    import unicodedata
    import re
    from django.utils.safestring import mark_safe
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    return mark_safe(re.sub('[-\s]+', '-', value))

def redirect_to_country(id):
    try:
        country = Country.objects.get(pk=id)
        return "/search/country/%s-%s/" % (country.id, slugify(country.name_en))
    except:
        return None
     
def get_title_by_type_and_model(estate_type, model, request):
    title = ''

    if model.__class__.__name__ == 'Region' or model.__class__.__name__ == 'City':
        model.otmenok = model.name
    else:
        if current_language(request) == 'ru':
            model.otmenok = model.name
        else:
            model.otmenok = model.name

    if estate_type == 'house':
        title = get_active_title({
            'ru': u"Дом в %s. Купить / продажа дома в %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'en': u"House in %s. Buy / Sell House in %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'de': u"Haus in %s. Kaufen / Verkaufen Haus in %s - WorldImmotrade" % (model.otmenok, model.otmenok)
        })
    if estate_type == 'apartment':
        title = get_active_title({
            'ru': u"Квартира в %s. Купить / продажа квартиры / апартаментов в %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'en': u"Apartment in %s. Buy / Sell flats / apartments in %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'de': u"Apartment in %s. Kaufen / Verkaufen Wohnungen / Appartements in %s - WorldImmotrade" % (model.otmenok, model.otmenok)
        })
    if estate_type == 'villa':
        title = get_active_title({
            'ru': u"Вилла / коттедж в %s. Купить / продажа Виллу / коттедж в %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'en': u"Villa / cottage in %s. Buy / Sell a Villa / Cottage in %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'de': u"Villa / Ferienhaus in %s. Kaufen / Verkaufen Villa / Cottage in %s - WorldImmotrade" % (model.otmenok, model.otmenok)
        })
    if estate_type == 'forone':
        title = get_active_title({
            'ru': u"Дом на одного хозяина в %s. Купить / продажа дом на одного хозяина в %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'en': u"House on one host in %s. Buy / sell a house on one host in %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'de': u"Haus auf einem Host in %s. Kauf / Verkauf eines Hauses auf einem Host in %s - WorldImmotrade" % (model.otmenok, model.otmenok)
        })
    if estate_type == 'fortwo':
        title = get_active_title({
            'ru': u"Дом на двух хозяев в %s. Купить / продажа дом на двух хозяев в %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'en': u"House on two hosts in %s. Buy / sell a house on two hosts in %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'de': u"Haus auf zwei Hosts in %s. Kauf / Verkauf eines Hauses auf zwei Hosts in %s - WorldImmotrade" % (model.otmenok, model.otmenok)
        })
    if estate_type == 'personal':
        title = get_active_title({
            'ru': u"Замок / особняк в %s. Купить / продажа замок / особняк в %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'en': u"Burg / Herrenhaus in %s. Buy / Sell Burg / Herrenhaus in %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'de': u"Burg / Herrenhaus in %s. Buy / Sell Burg / Herrenhaus in %s - WorldImmotrade" % (model.otmenok, model.otmenok)
        })
    if estate_type == 'smart':
        title = get_active_title({
            'ru': u"Умный дом в %s. Купить / продажа умный дом в %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'en': u"Smart home in %s. Buy / Sell a smart house in %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'de': u"Smart Home in %s. Buy / Sell ein intelligentes Haus in %s - WorldImmotrade" % (model.otmenok, model.otmenok)
        })
    if estate_type == 'room':
        title = get_active_title({
            'ru': u"Комнаты в %s - WorldImmotrade" % (model.otmenok),
            'en': u"Rooms in %s - WorldImmotrade" % (model.otmenok),
            'de': u"Zimmer in %s - WorldImmotrade" % (model.otmenok)
        })        
    if estate_type == 'sleeping':
        title = get_active_title({
            'ru': u"Подселение в квартире в %s - WorldImmotrade" % (model.otmenok),
            'en': u"Share a room in an apartment in %s - WorldImmotrade" % (model.otmenok),
            'de': u"Teilen sich ein Zimmer in einer Wohnung in %s - WorldImmotrade" % (model.otmenok)
        })
    if estate_type == 'sleeping2':
        title = get_active_title({
            'ru': u"Подселение из 2 комнат в %s - WorldImmotrade" % (model.otmenok),
            'en': u"Of 2 rooms share a room in %s - WorldImmotrade" % (model.otmenok),
            'de': u"Von 2 Zimmer teilen sich ein Zimmer in %s - WorldImmotrade" % (model.otmenok)
        })
    if estate_type == 'sleeping3':
        title = get_active_title({
            'ru': u"Подселение из 3 комнат в %s - WorldImmotrade" % (model.otmenok),
            'en': u"Of 3 rooms share a room in %s - WorldImmotrade" % (model.otmenok),
            'de': u"Von 3 Zimmer teilen sich ein %s in Deutschland - WorldImmotrade" % (model.otmenok)
        })          
    if estate_type == 'sleeping4':
        title = get_active_title({
            'ru': u"Подселение из 4 комнат в %s - WorldImmotrade" % (model.otmenok),
            'en': u"Of 4 rooms share a room in %s - WorldImmotrade" % (model.otmenok),
            'de': u"Von 4 Zimmer teilen sich ein Zimmer in %s - WorldImmotrade" % (model.otmenok)
        }) 
    if estate_type == 'sleeping5m':
        title = get_active_title({
            'ru': u"Подселение из 5 и более комнат в %s - WorldImmotrade" % (model.otmenok),
            'en': u"Share a room of 5 or more rooms in %s - WorldImmotrade" % (model.otmenok),
            'de': u"Share einen Raum von 5 oder mehr Zimmern in %s - WorldImmotrade" % (model.otmenok)
        })         
    if estate_type == 'elite':
        title = get_active_title({
            'ru': u"Элитная недвижимость в %s. Купить / продать элитную недвижимость в %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'en': u"Luxury real estate in %s. Buy / Sell Luxury Real Estate in %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'de': u"Luxus-Immobilien in %s. Buy / Sell Luxury Real Estate in %s - WorldImmotrade" % (model.otmenok, model.otmenok)
        })
    if estate_type == 'commercial':
        title = get_active_title({
            'ru': u"Коммерческая недвижимость в %s. Купить / продажа коммерческой недвижимости в %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'en': u"Commercial real estate in %s. Buy / sell real estate in %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'de': u"Gewerbliche Immobilien in %s. Kauf / Verkauf Immobilien in %s - WorldImmotrade" % (model.otmenok, model.otmenok)
        })
    if estate_type == 'office':
        title = get_active_title({
            'ru': u"Офис в %s. Купить / продажа офиса в %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'en': u"Office in %s. Buy / Sell Office in %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'de': u"Office in %s. Buy / Sell-Buro in %s - WorldImmotrade" % (model.otmenok, model.otmenok)
        })
    if estate_type == 'store':
        title = get_active_title({
            'ru': u"Магазин в %s. Купить / продажа магазина в %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'en': u"Store in %s. Buy / Sell shop in %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'de': u"Store in %s. Buy / Sell-Shop in %s - WorldImmotrade" % (model.otmenok, model.otmenok)
        })
    if estate_type == 'kafe':
        title = get_active_title({
            'ru': u"Кафе / ресторан в %s. Купить / продажа кафе / ресторана в %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'en': u"Cafe / restaurant in %s. Buy / Sell a cafe / restaurant in %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'de': u"Cafe / Restaurant in %s. Buy / Sell ein Cafe / Restaurant in %s - WorldImmotrade" % (model.otmenok, model.otmenok)
        })         
    if estate_type == 'hotel':
        title = get_active_title({
            'ru': u"Гостиница / отель в %s - WorldImmotrade" % (model.otmenok),
            'en': u"Hotel in %s - WorldImmotrade" % (model.otmenok),
            'de': u"Hotel in %s - WorldImmotrade" % (model.otmenok)
        })      
    if estate_type == 'warehouse':
        title = get_active_title({
            'ru': u"Склад в %s. Купить / продажа склада в %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'en': u"Warehouse in %s. Buy / sell stock in %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'de': u"Warehouse in %s. Kaufen / Verkauf von Aktien in %s - WorldImmotrade" % (model.otmenok, model.otmenok)
        })
    if estate_type == 'production':
        title = get_active_title({
            'ru': u"Производство в %s - WorldImmotrade" % (model.otmenok),
            'en': u"Production in %s - WorldImmotrade" % (model.otmenok),
            'de': u"Produktion in %s - WorldImmotrade" % (model.otmenok)
        })
    if estate_type == 'plot':
        title = get_active_title({
            'ru': u"Участок в %s. Купить / продажа участка в %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'en': u"A plot of land in %s. Buy / sell a piece of land in %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'de': u"Ein Grundstuck in %s. Kauf / Verkauf eines Grundstucks in %s - WorldImmotrade" % (model.otmenok, model.otmenok)
        })
    if estate_type == 'rest_house':
        title = get_active_title({
            'ru': u"Жилье для отдыха в %s - WorldImmotrade" % (model.otmenok),
            'en': u"Accommodation for holidays in %s - WorldImmotrade" % (model.otmenok),
            'de': u"Unterkunft fur den Urlaub in %s - WorldImmotrade" % (model.otmenok)
        })
    return title
        
def filterByRegionEndType(request, region, estate_type):
    '''
     Process urls like /region-158/type-house
    '''
    regionModel = get_object_or_404(Region, pk = region)
    country = regionModel.country.id
    
    return search(request, {
        'region':region,
        'estate_type':estate_type,
        'filterByRegionEndType': True,
        'country':country,
        'title':get_title_by_type_and_model(estate_type, regionModel, request)
    })

def filterByEstateType(request, estate_type):
    return search(request, {
        'estate_type':estate_type,
    })

def filterByCountryEndType(request, country, estate_type):
    '''
     Process urls like /house-in-<ID>-<SLUG>
    '''
    model = get_object_or_404(Country, pk = country)

    return search(request, {
        'country':model.id,
        'estate_type':estate_type,
        'showEstateTypeSeoText': True,
        'filterByCountryEndType': True,
        'type': 1,
        'title':get_title_by_type_and_model(estate_type, model, request)
    })

def filterRentByCountryEndType(request, country, estate_type):
    '''
     Process urls like /rent-*-in-<ID>-<SLUG>
    '''
    title = ''
    model = get_object_or_404(Country, pk = country)

    if estate_type == 'house':
        title = get_active_title({
            'ru': u"Аренда Дома в %s. Снять дом в %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'en': u"Rent Houses in %s. Rent a house in %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'de': u"Hauser mieten in %s. Mieten Sie ein Haus in %s - WorldImmotrade" % (model.otmenok, model.otmenok)
        })
    if estate_type == 'apartment':
        title = get_active_title({
            'ru': u"Аренда апартаментов в %s. Снять квартиру / жилье в %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'en': u"Rent apartments in %s. Rent an apartment in %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'de': u"Mieten Sie sich Appartments in %s. Mieten Sie eine Wohnung in %s - WorldImmotrade" % (model.otmenok, model.otmenok)
        })
    if estate_type == 'villa':
        title = get_active_title({
            'ru': u"Аренда Виллы / коттеджа в %s. снять Виллу / коттедж в %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'en': u"Rent Villas / cottages in %s - WorldImmotrade" % (model.otmenok),
            'de': u"Villas zu mieten / Ferienhauser in %s. Mieten Sie eine Villa / Ferienhaus in %s - WorldImmotrade" % (model.otmenok, model.otmenok)
        })
    if estate_type == 'apartment':
        title = get_active_title({
            'ru': u"Аренда апартаментов в %s. Снять квартиру / жилье в %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'en': u"Rent apartments in %s. Rent an apartment in %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'de': u"Mieten Sie sich Appartments in %s. Mieten Sie eine Wohnung in %s - WorldImmotrade" % (model.otmenok, model.otmenok)
        })
    if estate_type == 'forone':
        title = get_active_title({
            'ru': u"Аренда / снять дом на одного хозяина в %s - WorldImmotrade" % (model.otmenok),
            'en': u"Renting a house on one host in %s - WorldImmotrade" % (model.otmenok),
            'de': u"Vermietung eines Hauses auf einem Host in %s - WorldImmotrade" % (model.otmenok)
        })
    if estate_type == 'room':
        title = get_active_title({
            'ru': u"Аренда комнаты в %s. Снять / сдать комнату в %s - WorldImmotrade" % (model.otmenok),
            'en': u"Rent a room in %s. To rent a room in %s - WorldImmotrade" % (model.otmenok),
            'de': u"Mieten Sie ein Zimmer in %s. Um ein Zimmer in %s mieten - WorldImmotrade" % (model.otmenok)
        })
    if estate_type == 'elite':
        title = get_active_title({
            'ru': u"Аренда элитной недвижимость в %s - WorldImmotrade" % (model.otmenok),
            'en': u"Rental of luxury real estate in %s - WorldImmotrade" % (model.otmenok),
            'de': u"Vermietung von Luxus-Immobilien in %s - WorldImmotrade" % (model.otmenok)
        })
    if estate_type == 'elite':
        title = get_active_title({
            'ru': u"Аренда элитной недвижимость в %s - WorldImmotrade" % (model.otmenok),
            'en': u"Rental of luxury real estate in %s - WorldImmotrade" % (model.otmenok),
            'de': u"Vermietung von Luxus-Immobilien in %s - WorldImmotrade" % (model.otmenok)
        })
    if estate_type == 'commercial':
        title = get_active_title({
            'ru': u"Аренда коммерческой недвижимости в %s. Сдам коммерческую недвижимость в %s - WorldImmotrade" % (model.otmenok, model.otmenok),
            'en': u"Rent commercial property in %s - WorldImmotrade" % (model.otmenok),
            'de': u"Rent Gewerbeimmobilien in %s - WorldImmotrade" % (model.otmenok)
        })
    if estate_type == 'office':
        title = get_active_title({
            'ru': u"Аренда офиса в %s - WorldImmotrade" % (model.otmenok),
            'en': u"Rental office in %s - WorldImmotrade" % (model.otmenok),
            'de': u"Vermietung Buro in %s - WorldImmotrade" % (model.otmenok)
        })
    if estate_type == 'store':
        title = get_active_title({
            'ru': u"Аренда магазина в %s - WorldImmotrade" % (model.otmenok),
            'en': u"Rent a shop in %s - WorldImmotrade" % (model.otmenok),
            'de': u"Rent a shop in %s - WorldImmotrade" % (model.otmenok)
        })
    if estate_type == 'kafe':
        title = get_active_title({
            'ru': u"Аренда кафе / ресторана в %s - WorldImmotrade" % (model.otmenok),
            'en': u"Rent a cafe / restaurant in %s - WorldImmotrade" % (model.otmenok),
            'de': u"Rent a Cafe / Restaurant in %s - WorldImmotrade" % (model.otmenok)
        })
    if estate_type == 'warehouse':
        title = get_active_title({
            'ru': u"Аренда склада в %s - WorldImmotrade" % (model.otmenok),
            'en': u"Rent warehouse in %s - WorldImmotrade" % (model.otmenok),
            'de': u"Rent-Lager in %s - WorldImmotrade" % (model.otmenok)
        })
    if estate_type == 'plot':
        title = get_active_title({
            'ru': u"Аренда участка в %s - WorldImmotrade" % (model.otmenok),
            'en': u"Rental station in %s - WorldImmotrade" % (model.otmenok),
            'de': u"Mietstation in %s - WorldImmotrade" % (model.otmenok)
        })
    if estate_type == 'rest_house':
        title = get_active_title({
            'ru': u"Аренда жилья для отдыха в %s - WorldImmotrade" % (model.otmenok),
            'en': u"Rent holiday home in %s - WorldImmotrade" % (model.otmenok),
            'de': u"Rent Ferienhaus in %s - WorldImmotrade" % (model.otmenok)
        })             

    return search(request, {
        'country':model.id,
        'estate_type':estate_type,
        'type': 2,
        'title':title
    })

def searchByCountry(request, country, slug):
    '''
    Process url: search/country/<country>-*/
    '''
    country_model = Country.objects.get(pk=country)
    
    if slug != slugify(country_model.name_en):
        get_object_or_404(Country, pk = 0)

    if translation.get_language() == 'ru':
        text = country_model.otmenok
    else:
        text = country_model.name

    title = get_active_title({
        'ru': u"Недвижимость в %s. Купить / продажа недвижимости в %s - WorldImmotrade" % (text, text),
        'en': u"Real estate in %s. Buy / sell real estate in %s - WorldImmotrade" % (text, text),
        'de': u"Immobilien in %s. Kauf / Verkauf Immobilien in %s - WorldImmotrade" % (text, text)
    })

    return search(request, {
        'country': country,
        'countryOnly':True,
        'title': title,
        'searchByCountry': True,
    })

def filterByCity(request, country_id, city_id):
    city = get_object_or_404(City, pk = city_id, country = country_id)

    title = get_active_title({
        'ru': u"Недвижимость в %s. Купить / продажа недвижимости в %s - WorldImmotrade" % (city.name, city.name),
        'en': u"Real estate in %s. Buy / sell real estate in %s - WorldImmotrade" % (city.name, city.name),
        'de': u"Immobilien in %s. Kauf / Verkauf Immobilien in %s - WorldImmotrade" % (city.name, city.name)
    })

    return search(request, {
        'country': city.country.id,
        'city':city.id,
        'filterByCity': True,
        'title': title,
    })

def filterByRegion(request, country_id, region_id):
    region = get_object_or_404(Region, pk = region_id, country = country_id)

    return search(request, {
        'country': region.country.id,
        'region':region.id,
        'filterByRegion': True,
    })

def search(request, data = {}, students = False):
    '''
    Process search requests
    
    students - determinate is search for students
    '''
    estates_list = Apartament.objects.filter(is_published=True).order_by("-created")

    # If not data - use request.GET
    if (len(data) == 0):
        data = request.GET.copy()
    
    if len(request.GET) == 1 and request.GET.get('country', 0) > 0:
        test_redirect = redirect_to_country(request.GET.get('country', 0))
        if test_redirect:
            from django.http import HttpResponsePermanentRedirect
            return HttpResponsePermanentRedirect(test_redirect)

    try:
        if request.GET.get('id'):
            estates_list = estates_list.filter(id=request.GET.get('id'))
    except:
        pass

    try:
        # Process search for students
        if students == False:
            estates_list = estates_list.filter(students__in=[0,1])
        elif students == True:
            estates_list = estates_list.filter(students__in=[1,2])
            # Process additional rent_for option
            if data.getlist('rent_for'):
                estates_list = estates_list.filter(rent_for__in=data.getlist('rent_for'))
    except:
        pass

    try:
        # Filter by country
        if data.get('country'):
            country_from_url = data.get('country')
            estates_list = estates_list.filter(country=country_from_url)
            if data.get('region'):
                estates_list = estates_list.filter(region=data.get('region'))
            if data.get('city'):
                estates_list = estates_list.filter(city=data.get('city'))
    except:
        pass

    # Estate type
    try:
        if data.getlist('estate_type') and data.getlist('estate_type','0') != '0':
            estates_list = estates_list.filter(estate_type__in=data.getlist('estate_type'))
    except:
        if data.get('estate_type') and data.get('estate_type','0') != '0':
            estates_list = estates_list.filter(estate_type=data.get('estate_type'))        
    
    # Prices
    try:
        if data.get('price_min') and int(data.get('price_min')) > 0:
            price_min = float(data.get('price_min'))

            price_min = currency_manager.convert(
                from_c = request.session.get('current_currency',"R01239"),
                to_c = "R01239",
                sum = price_min,
            )

            estates_list = estates_list.filter(price__gte=price_min)
    except:
        pass
    try:
        if data.get('price_max') and int(data.get('price_max')) > 0:
            price_max = float(data.get('price_max'))

            price_max_c = currency_manager.convert(
                from_c = request.session.get('current_currency',"R01239"),
                to_c = "R01239",
                sum = price_max,
            )

            estates_list = estates_list.filter(price__lte=price_max_c)
    except:
        pass

    try:
        # By type
        if data.get('type'):
            estates_list = estates_list.filter(type=data.get('type'))
    except:
        pass

    try:
        # Aviable from/to
        if data.get('aviable_start'):
            estates_list = estates_list.filter(
                aviable_from__lte=time.strftime("%Y-%m-%d", time.strptime(data.get('aviable_start'),"%d.%m.%Y"))
            )
        if data.get('aviable_end'):
            estates_list = estates_list.filter(
                aviable_to__gte=time.strftime("%Y-%m-%d", time.strptime(data.get('aviable_end'),"%d.%m.%Y"))
            )
    except:
        pass

    try:
        # Total space from/to
        if data.get('total_space_start'):
            estates_list = estates_list.filter(total_space__gte=data.get('total_space_start'))
        if data.get('total_space_end'):
            estates_list = estates_list.filter(total_space__lte=data.get('total_space_end'))
    except:
        pass

    try:
        # Floor from/to
        if data.get('floor_start'):
            estates_list = estates_list.filter(floor__gte=data.get('floor_start'))
        if data.get('floor_end'):
            estates_list = estates_list.filter(floor__lte=data.get('floor_end'))
    except:
        pass

    try:
        # Rooms count from/to
        if data.get('rooms_start'):
            estates_list = estates_list.filter(rooms_count__gte=data.get('rooms_start'))
        if data.get('rooms_end'):
            estates_list = estates_list.filter(rooms_count__lte=data.get('rooms_end'))
    except:
        pass

    try:
        # Sleeping rooms from/to
        if data.get('sleep_rooms_start'):
            estates_list = estates_list.filter(bedrooms_count__gte=data.get('sleep_rooms_start'))
        if data.get('sleep_rooms_end'):
            estates_list = estates_list.filter(bedrooms_count__lte=data.get('sleep_rooms_end'))
    except:
        pass

    try:
        # Build year from/to
        if data.get('year_start'):
            estates_list = estates_list.filter(built_year__gte=data.get('year_start'))
        if data.get('year_end'):
            estates_list = estates_list.filter(built_year__lte=data.get('year_end'))
    except:
        pass

    try:
        # Window view
        if data.getlist('window_view'):
            estates_list = estates_list.filter(window_view__in=data.getlist('window_view'))
    except:
        pass

    try:
        # Object location
        if data.getlist('location'):
            estates_list = estates_list.filter(location__in=data.getlist('location'))
    except:
        pass

    try:
        # Furnishings
        if data.getlist('furnishings'):
            estates_list = estates_list.filter(furnishings__in=data.getlist('furnishings'))
    except:
        pass

    try:
        # Comfort
        if data.getlist('comfort'):
            estates_list = estates_list.filter(comfort__in=data.getlist('comfort'))
    except:
        pass

    try:
        # Additional equipment
        if data.getlist('additional_equipment'):
            estates_list = estates_list.filter(additional_equipment__in=data.getlist('additional_equipment'))
    except:
        pass

    try:
        # Floor type
        if data.getlist('floor_type'):
            estates_list = estates_list.filter(floor_type__in=data.getlist('floor_type'))
    except:
        pass

    try:
        # Process order_by
        if request.GET.get('order', False):
            if request.GET.get('order', False) == 'country':
                estates_list = estates_list.order_by('country')
            if request.GET.get('order', False) == 'city':
                estates_list = estates_list.order_by('city')
            if request.GET.get('order', False) == 'price_asc':
                estates_list = estates_list.order_by('price')
            if request.GET.get('order', False) == 'price_desc':
                estates_list = estates_list.order_by('-price')
            if request.GET.get('order', False) == 'space_asc':
                estates_list = estates_list.order_by('living_space')
            if request.GET.get('order', False) == 'space_desc':
                estates_list = estates_list.order_by('-living_space')
            if request.GET.get('order', False) == 'created_asc':
                estates_list = estates_list.order_by('created')
            if request.GET.get('order', False) == 'created_desc':
                estates_list = estates_list.order_by('-created')
        else:
            estates_list = estates_list.order_by('-created')

        if data.get('id'):
            estates_list = estates_list.filter(id=data.get('id'))
    except:
        estates_list = estates_list.order_by('-created')

    # Select only unique objects
    estates_list = estates_list.distinct()

    # Check if we need to open "Additional" slider in search sidebar
    open_additional_slider = False
    additional_items = ['floor_start', 'floor_end', 'rooms_start','rooms_end',
                        'sleep_rooms_start','sleep_rooms_end',
    ]

    for k in additional_items:
        if data.get(k, False):
            open_additional_slider = True
            break

    try:
        countryModel = Country.objects.get(id=data.get('country'))
    except:
        countryModel = None

    # Set seo title
    if not data.get('title'):
        title = ''
        try:
            if countryModel.title:
                title = countryModel.title
            else:
                title = u"Недвижимость в %s купить/продать -" % (countryModel.otmenok or countryModel.name)
        except:
            title = ''
    else:
        title = data.get('title')

    if students:
        title = _(u"Жилье для студентов - WorldImmotrade")

    if int(request.GET.get('page', 0)) >= 2:
        title = "%s %s" % (request.GET.get('page', 0), title)

    try:
        data['page'] = int(request.GET.get('page', 0))
    except:
        data['page'] = 0

    boxCountries = []
    if countryModel:
        needCPos = 0
        i=0
        if countryModel:
            country_id = countryModel.id
        boxCountries = Country.objects.order_by('name_ru').all()
        for c in boxCountries:
            if c.id == country_id:
                needCPos = i
            i += 1

        if needCPos - 5 < 0:
            needCPos = 5
        if needCPos + 6 > len(boxCountries):
            needCPos = len(boxCountries)
        boxCountries = boxCountries[needCPos-5:needCPos+6]
        
    canonical = ''

    if request.GET.get('country', 0):
        try:
            if request.GET.get('country', 0) and request.GET.get('region') == u"" and not request.GET.get('city') and not request.GET.get('region'):
                country = Country.objects.get(pk=data.get('country'))
                canonical = "<link rel=\"canonical\" href=\"http://%s/search/country/%s-%s/\" />" % (request.get_host(), country.id, slugify(countryModel.name_en))
            if request.GET.get('country', 0) > 0 and request.GET.get('region', 0) > 0 and not request.GET.get('city'):
                country = Country.objects.get(pk=data.get('country'))
                region = Region.objects.get(pk=data.get('region'))
                canonical = "<link rel=\"canonical\" href=\"http://%s/country-%s-%s/region-%s\" />" % (request.get_host(), country.id, slugify(countryModel.name_en), region.id)
            if request.GET.get('country', 0) > 0 and request.GET.get('region', 0) > 0 and request.GET.get('city'):
                city = City.objects.get(pk=data.get('city'))
                canonical = "<link rel=\"canonical\" href=\"http://%s/country-%s-%s/city-%s\" />" % (request.get_host(), countryModel.id, slugify(countryModel.name_en), city.id)
        except:
            pass

    return direct_to_template(request, 'estates/search_list.html', {
        'estates_list': estates_list,
        'open_additional_slider': open_additional_slider,
        'students':students,
        'title':title,
        'boxCountries':boxCountries,
        'datetime': datetime,
        'country':data.get('country'),
        'data':data,
        'canonical':canonical
        #'country_only':country_only
    })

def robots(request):
    '''
    Robots.txt for subdomains
    '''
    html=""
    host = request.get_host()
    if host.startswith('en.'):
        html = "User-agent: * \nDisallow: /"
    if host.startswith('de.'):
        html = "User-agent: * \nDisallow: /"
    if host.startswith('ru.'):
        html = "User-agent: * \nDisallow: /"

    if html == "":
        if host.endswith('.com'):
            html = open('/srv/www/vhosts/worldimmotrade.ru/httpdocs/immotrade/media/robots_com.txt').read()
        if host.endswith('.ru'):
            html = open('/srv/www/vhosts/worldimmotrade.ru/httpdocs/immotrade/media//robots_ru.txt').read()
        if host.endswith('.de'):
            html = open('/srv/www/vhosts/worldimmotrade.ru/httpdocs/immotrade/media//robots_de.txt').read()                        

    return HttpResponse(html)

@login_required()
def create(request):
    ''' Create new apartment '''
    get_object_or_404(UserProfile, user=request.user, is_saler=True)

    form = ApartmentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form2 = form.save(commit=False)
        form2.user = request.user
        form2.save()
        form.save_m2m()

        allowed_extensions = ['gif', 'jpg', 'png']
        allowed_extensions_docs = ['pdf', 'doc', 'docx', 'xls']
        import hashlib, os, time 

        # Process photos
        for f in request.FILES.getlist('photo'):
            #f.name = str(random.random())
            if f.name.lower().split(".")[-1] in allowed_extensions:  
                new_file_name = "%s%s" % (hashlib.sha1("%s%s" % (random.random(),time.time())).hexdigest(), '.jpg')
                path = os.path.realpath(settings.MEDIA_ROOT + 'uploads/%s/%s/%s' % (request.user.id, form2.id, new_file_name))
                
		try:
		    os.mkdirs('/srv/www/vhosts/worldimmotrade.ru/httpdocs/immotrade/media/uploads/%s/%s' % (request.user.id, form2.id))
                    p2 = '/srv/www/vhosts/worldimmotrade.ru/httpdocs/immotrade/media/uploads/%s/%s' % (request.user.id, form2.id)
                    import commands
                    commands.getstatusoutput('chmod -R 0777 %s' % (p2))
                except:
                    pass

                destination = open(path, 'wb+')
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()
     
                #new_file_name = hashlib.sha1(f.name).hexdigest()

                # Assign photo to apartment
                photo = Photo(apartament=form2, photo='uploads/%s/%s/%s' % (request.user.id, form2.id, new_file_name))
                photo.save()

        # Process documents
        for d in request.FILES.getlist('document'): 
            f.name = str(random.random())
            if d.name.split(".")[-1] in allowed_extensions_docs: 
                new_file_name = hashlib.sha1("%s%s" % (random.random(),time.time())).hexdigest() + '.' + d.name.split(".")[-1] 
                path = os.path.realpath(settings.MEDIA_ROOT + 'uploads/%s/%s/%s' % (request.user.id, form2.id, new_file_name))
                
                destination = open(path, 'wb+')
                for chunk in d.chunks():
                    destination.write(chunk)
                destination.close()

                # Assign photo to apartment
                document = Document(apartament=form2, file_name='uploads/%s/%s/%s' % (request.user.id, form2.id, new_file_name))
                document.save()

        messages.success(request, _(u"Объект успешно создан."))

        from tarifs.models import TarifRequests
        user_profile = get_object_or_404(UserProfile, user=request.user, is_saler=True) 
        is_tarif_selected = TarifRequests.objects.filter(user=user_profile, paid=True).count()
        if is_tarif_selected == 0:
            return redirect('/tarifs')
        else:
            return redirect('cart')

    return direct_to_template(request, 'estates/form.html', {
        'form': form,
    })

@login_required()
def edit(request, id):
    ''' Edit existing apartment '''
    apartment_model = get_object_or_404(Apartament, pk=id, user=request.user)
    form = ApartmentForm(request.POST or None, instance=apartment_model)

    if form.is_valid():
        apartment = form.save()
        from django.db import connection, transaction
        cursor = connection.cursor()
        cursor.execute("UPDATE estates_apartament SET name_ru = %s, name_en=%s, name_de=%s WHERE id = %s", [request.POST.get('name_ru'),request.POST.get('name_en'),request.POST.get('name_de'),id])
        cursor.execute("UPDATE estates_apartament SET description_ru = %s, description_en=%s, description_de=%s WHERE id = %s", [request.POST.get('description_ru'),request.POST.get('description_en'),request.POST.get('description_de'),id])
        cursor.execute("UPDATE estates_apartament SET object_location_ru = %s, object_location_en=%s, object_location_de=%s WHERE id = %s", [request.POST.get('object_location_ru'),request.POST.get('object_location_en'),request.POST.get('object_location_de'),id])

        allowed_extensions = ['gif', 'jpg', 'png', 'jpeg']
        allowed_extensions_docs = ['pdf', 'doc', 'docx', 'xls']
        import hashlib, os, time 

        # Process photos
        for f in request.FILES.getlist('photo'):  
            if f.name.lower().split(".")[-1] in allowed_extensions: 
                new_file_name = hashlib.sha1("%s%s" % (random.random(),time.time())).hexdigest() + '.jpg'
                path = os.path.realpath(settings.MEDIA_ROOT + 'uploads/%s/%s/%s' % (request.user.id, apartment.id, new_file_name))
                
                destination = open(path, 'wb+')
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()

                # Assign photo to apartment
                photo = Photo(apartament=apartment, photo='uploads/%s/%s/%s' % (request.user.id, apartment.id, new_file_name))
                photo.save()

        # Process documents
        for d in request.FILES.getlist('document'):  
            if d.name.split(".")[-1] in allowed_extensions_docs: 
                new_file_name = hashlib.sha1("%s%s" % (random.random(),time.time())).hexdigest() + '.' + d.name.split(".")[-1] 
                path = os.path.realpath(settings.MEDIA_ROOT + 'uploads/%s/%s/%s' % (request.user.id, apartment.id, new_file_name))
                
                destination = open(path, 'wb+')
                for chunk in d.chunks():
                    destination.write(chunk)
                destination.close()

                # Assign photo to apartment
                document = Document(apartament=apartment, file_name='uploads/%s/%s/%s' % (request.user.id, apartment.id, new_file_name))
                document.save()

        # Process deleted photos
        if request.POST.getlist('delete_image'):
            for i in request.POST.getlist('delete_image'):
                # Get end delete image
                Photo.objects.filter(pk__in=request.POST.getlist('delete_image'), apartament=apartment_model).delete()

        # Process deleted docs
        if request.POST.getlist('delete_doc'):
            for i in request.POST.getlist('delete_doc'):
                # Get end delete image
                Document.objects.filter(pk__in=request.POST.getlist('delete_doc'), apartament=apartment_model).delete()

        messages.success(request, _(u"Изменения сохранены"))
        if apartment_model.is_published:
            return redirect('apartment-list')
        else:
            return redirect('cart')

    return direct_to_template(request, 'estates/form.html', {
        'form': form,
    })

@login_required()
def estates_list(request):
    ''' Display list of user objects '''
    estates_list = Apartament.objects.filter(user=request.user, is_published=True).order_by('-created')

    return direct_to_template(request, 'estates/list.html', {
        'estates_list': estates_list,
        'per_page': settings.OBJECTS_PER_PAGE,
    })

@login_required()
def add_to_bookmarks(request, id):
    ''' Add apartment to user bookmars '''
    model = get_object_or_404(Apartament, pk=id)
    # Add to bookmarks
    bookmark = Bookmarks(apartment=model, user=request.user)
    bookmark.save()
    return redirect('apartment-view', model.id)

@login_required()
def remove_from_bookmarks(request, id):
    ''' Remove apartment from bookmarks '''
    model = get_object_or_404(Apartament, pk=id)
    # Delete bookmarked object
    Bookmarks.objects.filter(apartment=model, user=request.user).delete()
    return redirect('apartment-view', model.id)

@login_required()
def bookmarks(request):
    ''' Display user bookmarks '''
    bookmarks = Bookmarks.objects.filter(user=request.user)
    paginator = Paginator(bookmarks, settings.OBJECTS_PER_PAGE)

    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        bookmarks = paginator.page(page)
    except (EmptyPage, InvalidPage):
        bookmarks = paginator.page(paginator.num_pages)

    return direct_to_template(request, 'estates/bookmarks.html', {
        'bookmarks': bookmarks,
        'per_page': settings.OBJECTS_PER_PAGE,
    })

def view(request, id):
    ''' View estate '''
    model = get_object_or_404(Apartament, pk = id, is_published=True)
    form = ApartmentViewForm(instance=model)
    contact_form = ContactForm(request.POST or None)

    model.views = model.views + 1
    model.save()

    model.user.profile = UserProfile.objects.filter(user=model.user).get()

    # Check if user added this apartment to bookmarks
    if request.user.is_authenticated():
        try:
            bookmarked = Bookmarks.objects.filter(apartment=model, user=request.user).get()
        except:
            bookmarked = False
    else:
        bookmarked = False

    if request.POST.has_key('send_contact'):
        # Send user request to saler
        if contact_form.is_valid():
            current_page = Site.objects.get_current().domain +"/estates/view/" + str(model.id) + '/'
            if request.user.is_authenticated():
                # Send private message
                msg = Message(
                    subject = unicode(_(u"Запрос")),
                    body = "%s\n----------\n%s" % (contact_form.cleaned_data['message'],
                                         _(u"Сообщение отправлено со страницы:") + "\n" + current_page),
                    sender = request.user,
                    recipient = model.user,
                )
                msg.save()
            else:
                # User is not authenticated,
                # so recipient can't reply to this user from
                # inner messages system.
                message_data= {
                    'recipient': model.user.profile.first_name,
                    'sender': u"%s %s" % (contact_form.cleaned_data['first_name'], contact_form.cleaned_data['last_name']),
                    'message': contact_form.cleaned_data['message'],
                    'current_page': current_page,
                }
                message = render_to_string('emails/notify.html', message_data)
                email = EmailMessage(_(u"Сообщение от ") + contact_form.cleaned_data['first_name'],
                                     message,
                                     contact_form.cleaned_data['email'],
                                     [model.user.profile.email])
                email.send()
            messages.success(request, _(u"Спасибо. Ваше сообщение отправлено."))
            return redirect('apartment-view', model.id)
    else:
        if request.user.is_authenticated():
            profile = UserProfile.objects.get(user=request.user)
            if profile:
                # Pre-populate user form
                contact_form.fields['first_name'].initial = profile.first_name
                contact_form.fields['last_name'].initial = profile.last_name
                contact_form.fields['email'].initial = profile.email
                contact_form.fields['phone'].initial = profile.phone

    # Check for print action
    if request.GET.get("print"):
        tpl_name = 'estates/view_print.html'
    else:
        tpl_name = 'estates/view.html'

    boxCountries = []
    countryModel = model.country
    if countryModel:
        needCPos = 0
        i=0
        if countryModel:
            country_id = countryModel.id
        boxCountries = Country.objects.order_by('name_ru').all()
        for c in boxCountries:
            if c.id == country_id:
                needCPos = i
            i += 1

        if needCPos - 5 < 0:
            needCPos = 5
        if needCPos + 6 > len(boxCountries):
            needCPos = len(boxCountries)
        boxCountries = boxCountries[needCPos-5:needCPos+6]

    data = {
        'country': model.country.id,
        'region': model.region.id,
    }

    data['on_object_view'] = True

    return direct_to_template(request, tpl_name, {
        'model': model,
        'form': form,
        'contact_form': contact_form,
        'bookmarked': bookmarked,
        'data':data,
        'country': model.country.id,
        'boxCountries': boxCountries,
    })

@login_required()
def cart(request):
    ''' Display user cart '''
    estates_list = Apartament.objects.filter(user=request.user, is_published=False).order_by('-created')
    paginator = Paginator(estates_list, settings.OBJECTS_PER_PAGE)

    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        estates_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        estates_list = paginator.page(paginator.num_pages)

    from tarifs.models import TarifRequests
    profile = UserProfile.objects.get(user=request.user)

    try:
        current_tarif = TarifRequests.objects.get(user=profile)
    except:
        current_tarif = None

    return direct_to_template(request, 'estates/cart.html', {
        'estates_list': estates_list,
        'per_page': settings.OBJECTS_PER_PAGE,
        'current_tarif': current_tarif 
    })


@login_required()
def publish(request):
    ''' Move objects from cart to site '''
    from tarifs.models import TarifRequests
    import datetime

    try:
        test = TarifRequests.objects.get(
            user=UserProfile.objects.get(user=request.user), paid=True, end_date__gt=datetime.datetime.today()
        )

        # Get count of user objects in cart
        published = len(Apartament.objects.filter(user=request.user, is_published=True)) + 1
        max_in_tarif = test.tarif.ad_count

        if test.tarif.ad_count > 0:
            if published > max_in_tarif:
                raise StandardError

        model = get_object_or_404(Apartament, pk=request.GET.get('id'), user=request.user)
        model.is_published = True
        model.save()

    except:
        # Not paid
        pass

    return redirect("cart")

@login_required()
def unpublish(request):
    ''' Move objects from cart to site '''
    model = get_object_or_404(Apartament, pk=request.GET.get('id'), user=request.user)
    model.is_published = False
    model.save()
    return redirect("apartment-list")

@login_required()
def delete(request):
    ''' Delete objects '''
    model = get_object_or_404(Apartament, pk=request.GET.get('id'), user=request.user)
    model.delete()
    return redirect("cart")


#########################################################
# MIGRATION
#########################################################

from itertools import *
from django.db import connection

from users.models import UserProfile
from django.contrib.auth.models import User
from world.models import Region, City, Country
from estates.forms import ApartmentForm
import urllib2
from urllib2 import Request
import hashlib, os, time

def query_to_dicts(query_string, *query_args):
    cursor = connection.cursor()
    cursor.execute(query_string, query_args)
    col_names = [desc[0] for desc in cursor.description]
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        row_dict = dict(izip(col_names, row))
        yield row_dict
    return


def run_query(query):
    return query_to_dicts(query)

def old_country_to_new(key):
    #OLD:NEW
    countries_list = {
        '3':14,	    #Australia
        '70':13,	#Austria
        '5':36,	    #Belarus
        '6':21,	    #Belgium
        '8':31,	    #Brazil
        '7':23,	    #Bulgaria
        '23':38,	#Canada
        '24':248,	#Caribbean Islands
        '61':46,	#Chile
        '26':48,	#China
        '28':50,	#Costa Rica
        '59':97,	#Croatia
        '29':51,	#Cuba
        '27':54,	#Cyprus
        '60':55,	#Czech
        '14':58,	#Denmark
        '15':60,	#Dominican Republic
        '71':64,	#Egypt
        '65':63,	#Estonia
        '56':69,	#Finland
        '58':74,	#France
        '12':56,	#Germany
        '9':76,	    #Great Britain
        '13':88,	#Greece
        '10':99,    #Hungary
        '18':104,	#India
        '19':100,	#Indonesia
        '68':101,	#Ireland
        '17':102,	#Israel
        '21':109,	#Italy
        '67':113,	#Japan
        '22':125,	#Kazakhstan
        '25':114,	#Kenya
        '30':135,	#Latvia
        '31':133,	#Lithuania
        '32':134,	#Luxembourg
        '33':153,	#Malta
        '35':157,	#Mexico
        '36':249,	#Monaco
        '62':250,	#Montenegro
        '34':137,	#Morocco
        '37':166,	#Netherlands
        '38':171,	#New Zealand
        '39':167,	#Norway
        '41':173,	#Panama
        '42':186,	#Paraguay
        '57':177,	#Philippines
        '44':179,	#Poland
        '43':184,	#Portugal
        '46':189,	#Romania
        '45':191,	#Russia
        '47':195,	#Seychelles
        '48':198,	#Singapore
        '49':202,	#Slovakia
        '50':200,	#Slovenia
        '66':245,	#Southern Africa
        '20':67,	#Spain
        '64':197,	#Sweden
        '63':43,	#Switzerland
        '52':216,	#Thailand
        '69':221,	#Tunisia
        '53':223,	#Turkey
        '54':228,	#Ukraine
        '40':2,  #United Arab Emirates
        '55':232,	#Uruguay
        '51':231,	#USA
        '11':236,	#Venezuela
    }

    return countries_list.get(key)

def old_type_to_new(key1):
    params = {
        '1':"apartment",
        '2':"house",
        '3':"elite",
        '4':"commercial",
        '5':"plot",
        '6':"other",
    }

    return params.get(key1, "house")


def old_category_to_new(key):
    if key == '0' or key == 0:
        return 1
    else:
        return key

def migrate(request): 
    user = User.objects.get(pk=1)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM estates_apartament")
    cursor.execute("DELETE FROM estates_photo")
    old_apartments = run_query("SELECT * FROM old_catalog")
    pos = 0

    rfile = open('/srv/www/vhosts/worldimmotrade.ru/httpdocs/immotrade/relations.txt', 'w')
    #rfile = open('/var/www/immotrade/relations.txt', 'w')

    for apartment in old_apartments:
        try:
            country = Country.objects.get(pk=old_country_to_new(str(apartment['country_id'])))

            regions = list(Region.objects.filter(country=country))
            cities = list(City.objects.filter(region=regions[1]))
            region = regions[1]
            city = cities[1]
        except :
            continue

        params = {
            'type': old_category_to_new(apartment['category_id']),
            'estate_type': old_type_to_new(str(apartment['type_id'])),
            'name_ru': apartment['title_ru'],
            'name_en': apartment['title_en'] or apartment['title_ru'],
            'name_de': apartment['title_de'] or apartment['title_ru'],
            'price': float(apartment["price"]) or float("0.00"),

            'description_ru': apartment['text_ru'],
            'description_en': apartment['text_en'],
            'description_de': apartment['text_de'],

            'country': int(country.pk),
            'region': int(region.pk),
            'city': int(city.pk),
        }

        try:
            params['living_space'] = int(apartment['area'])
        except :
            pass


        try:
            params['rooms_count'] = int(apartment['count_room'])
        except :
            pass

        try:
            params['built_year'] = int(apartment['year'])
        except :
            pass

        try:
            params['bathrooms_count'] = int(apartment['count_badroom'])
        except :
            pass

        try:
            params['floors_count'] = int(apartment['count_floor'])
        except :
            pass

        form = ApartmentForm(params)
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.user = user
            form2.save()
            form.save_m2m()

            # old/new
            rfile.write("%s - %s\n" % (apartment['id'], form2.id))

            # Process photos
            photos = apartment['photos']
            if len(photos) > 0:
                photo_list = photos.split(',')

                for photo in photo_list:
                    try:
                        file_name = hashlib.sha1(photo + str(time.time())).hexdigest() + '.jpg'
                        print "Downloading photo..."
                        page_url = 'http://worldimmotrade.com/public/upload/catalog/%s' % (photo)
                        request = Request(page_url,
                                                headers={ 'User-Agent': 'Mozilla/5.0', 'Accept-Charset': 'utf-8' }
                        )
                        res = urllib2.urlopen(request)

                        #f = open('/var/www/immotrade/media/uploads/%s/%s/%s' % (1,form2.id,file_name), 'w')
                        f = open('/srv/www/vhosts/worldimmotrade.ru/httpdocs/immotrade/media/uploads/%s/%s/%s' % (1,form2.id,file_name), 'w')
                        f.write(res.read())
                        f.close()
                        res.close()

                        # Create new DB object
                        photo = Photo(apartament=form2, photo='uploads/%s/%s/%s' % (1, form2.id, file_name))
                        photo.save()
                    except:
                        pass

        else:
            print apartment['category_id']
            print "error in " + str(apartment['id'])
            print form.errors
            print '------------------------'

        pos += 1
        print "Position " + str(pos)

    rfile.close()    
    return HttpResponse("Done")
