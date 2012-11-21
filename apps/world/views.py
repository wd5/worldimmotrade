# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.utils import simplejson
from django.utils import translation

from world.models import *

def load_json(request):
    """
    Load regions or cities and returns it in JSON format
    """
    if 'country' in request.GET and 'region' not in request.GET:
        # Get regions
		if translation.get_language() == 'ru':
			objects = Region.objects.filter(country=request.GET['country']).order_by('name').all().distinct()
		if translation.get_language() == 'en':
			objects = Region.objects.filter(country=request.GET['country']).order_by('name').all().distinct()
		if translation.get_language() == 'de':
			objects = Region.objects.filter(country=request.GET['country']).order_by('name').all().distinct()			
    elif 'region' in request.GET and 'country' in request.GET:
        # Get city
		if translation.get_language() == 'ru':
			objects = City.objects.filter(country=request.GET['country'], region=request.GET['region']).order_by('name').all().distinct()
		if translation.get_language() == 'en':
			objects = City.objects.filter(country=request.GET['country'], region=request.GET['region']).order_by('name').all().distinct()
		if translation.get_language() == 'de':
			objects = City.objects.filter(country=request.GET['country'], region=request.GET['region']).order_by('name').all().distinct()
    else:
        objects = {}

    result = ''
    for obj in objects:
        result += "<option value='%s'>%s</option>" % (obj.id, obj.name)

    return HttpResponse(result, mimetype='text/html')


def autocomplete(request):
    result = ""

    objects = City.objects.filter(
            country=request.GET['country'], region=request.GET['region'], name__startswith=request.GET['term']
    ).distinct().order_by('name')

    pos = 0
    for c in objects:
        if pos < len(objects)-1:
            comma = ','
        else:
            comma = ''
        result += '{ "id": "%s", "label": "%s", "value": "%s" }%s ' % (c.id,c.name,c.name, comma)
        pos += 1

    #return HttpResponse(simplejson.dumps(result), mimetype='application/json')
    return HttpResponse('[ ' + result + ' ]')
