# -*- coding: utf-8 -*-
import os
import Image
import re

from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_unicode
from django import template
from django.utils import translation
from django.forms import ChoiceField, FileField
from django.conf import settings

from estates.models import Apartament
from pages.models import News
from urlgen import urlGen

register = template.Library()


from django import template

class AssignNode(template.Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
    def render(self, context):
        context[self.name] = self.value.resolve(context, True)
        return ''

def do_assign(parser, token):
    """
    Assign an expression to a variable in the current context.
    
    Syntax::
        {% assign [name] [value] %}
    Example::
        {% assign list entry.get_related %}
        
    """
    bits = token.contents.split()
    if len(bits) != 3:
        raise template.TemplateSyntaxError("'%s' tag takes two arguments" % bits[0])
    value = parser.compile_filter(bits[2])
    return AssignNode(bits[1], value)

register = template.Library()
register.tag('assign', do_assign)



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

@register.filter(name='toEstateType')
def _to_estate_type(type_str):
    from estates.choices import ESTATE_TYPE_CHOICES as etype
    dic = dict(etype)
    result = dic[type_str]
    if result.startswith('--'):
        return result[2:]
    else:
        return result


@register.filter(name='count_objects')
def _count_objects_by_country(country_model):
    ''' Count total estates for country model '''
    return Apartament.objects.filter(country=country_model, is_published=True).count()

@register.filter(name="truncate")
def truncate_(value, arg):
    try:
        bits = []
        for x in arg.split(u':'):
            if len(x) == 0:
                bits.append(None)
            else:
                bits.append(int(x))
        result = value[slice(*bits)]
        if len(value) > len(result):
            result = result + '...'
        return result

    except (ValueError, TypeError):
        return value # Fail silently.

@register.filter(name='field_value')
def field_value(field):
	"""
	Returns the value for this BoundField, as rendered in widgets.
	"""
	if field.form.is_bound:
		if isinstance(field.field, FileField) and field.data is None:
			val = field.form.initial.get(field.name, field.field.initial)
		else:
			val = field.data
	else:
		val = field.form.initial.get(field.name, field.field.initial)
		if callable(val):
			val = val()
	if val is None:
		val = ''
	return val

@register.filter(name='display_value')
def display_value(field):
    """
    Returns the displayed value for this BoundField, as rendered in widgets.
    """
    values=[]
    value = field_value(field)
    try:
		if field.name.startswith("dist_to") and float(value) > 0:
			return value
    except:
		pass

    if field.name == "views":
        return value

    if isinstance(field.field, ChoiceField):
        for (val, desc) in field.field.choices:
            # For many to many fields
            if type(value) == list:
                for v in value:
                    if v == val:
                        values.append(unicode(field.field.choices[int(val)-1][1]))
            # For normal select
            if val == value:
                return unicode(desc)

    if value == '' or value == []:
        return u'Не указано'
    if value == True:
        return _(u'Да')
    if value == False:
        return u'Нет'
    if values:
        return ", ".join(values)

    return value


r_lightbox = re.compile('<a (?=[^>]*\.(jpg|gif|png))(?![^>]*lightbox)')
s_lightbox = '<a rel="lightbox" '

@register.filter
def lightbox(content):
    return r_lightbox.sub(s_lightbox, smart_unicode(content))

@register.filter(name='thumbnail')
def thumbnail_(file, size='200x200'):
    """
    Example:
    <img src="object.get_image_url" alt="original image" />
    <img src="object.image|thumbnail" alt="image resized to default 200x200 format" />
    <img src="object.image|thumbnail:"200x300" alt="image resized to 200x300" />

    The filter is applied to a image field (not the image url get from
    get_image_url method of the model), supposing the image filename is
    "image.jpg", it checks if there is a file called "image_200x200.jpg" or
    "image_200x300.jpg" on the second case, if the file isn't there, it resizes
    the original image, finally it returns the proper url to the resized image.
    """

    if file:
        # defining the size
        x, y = [int(x) for x in size.split('x')]
        # defining the filename and the miniature filename
        basename, format = file.path.rsplit('.', 1)
        baseurl, _format = file.url.rsplit('.', 1)

        #miniature = basename + '_' + size + '.' +  format
        #miniature_filename = os.path.join(settings.MEDIA_ROOT, miniature)
        #miniature_url = os.path.join(settings.MEDIA_URL, miniature)

        miniature_filename = basename + '_' + size + '.' +  format
        miniature_url = baseurl + '_' + size + '.' +  format

        # if the image wasn't already resized, resize it
        if not os.path.exists(miniature_filename) and os.path.exists(file.path):
            #print '>>> debug: resizing the image to the format %s!' % size
            img = Image.open(file.path)
            if img.mode != "RGB":
                img = img.convert("RGB")

            # image.thumbnail([x, y], Image.ANTIALIAS) # generate a 200x200 thumbnail
            src_width, src_height = img.size

            src_ratio = float(src_width) / float(src_height)
            dst_width, dst_height = x, y
            dst_ratio = float(dst_width) / float(dst_height)

            if dst_ratio < src_ratio:
                crop_height = src_height
                crop_width = crop_height * dst_ratio
                x_offset = float(src_width - crop_width) / 8
                y_offset = 0
            else:
                crop_width = src_width
                crop_height = crop_width / dst_ratio
                x_offset = 0
                y_offset = float(src_height - crop_height) / 15
            img = img.crop((int(x_offset), int(y_offset), int(x_offset)+int(crop_width), int(y_offset+int(crop_height))))
            img = img.resize((dst_width, dst_height), Image.ANTIALIAS)
            img.save(miniature_filename, img.format, quality=settings.UPLOAD_IMAGE_QUALITY)

        return settings.MEDIA_URL + miniature_url

    return ''

@register.filter(name='latest_news')
def _get_latest_news(limit = 3):
    return News.objects.all()[:limit]

@register.filter(name='addurlparam')
def _add_url_param(request, param_name):
    uri = urlGen()
    return uri.generate(str(param_name), request)

@register.filter('break')
def break_(loop):
    raise StopLoopException(loop, False)


@register.filter('continue')
def continue_(loop):
    raise StopLoopException(loop, True)


# monkeypatch NodeList to handle break/continue
def render(self, context):
    return template.mark_safe(''.join(map(template.force_unicode,
                                          _render_nodelist_items(self,context))))
template.NodeList.render = render


# monkeypatch ForNode to handle break/continue
def render(self, context):
    try:
        values = self.sequence.resolve(context, True)
    except template.VariableDoesNotExist:
        values = []
    if values is None:
        values = []
    if not hasattr(values, '__len__'):
        values = list(values)
    len_values = len(values)
    if len_values < 1:
        return self.nodelist_empty.render(context)
    if self.is_reversed:
        values = reversed(values)
    unpack = len(self.loopvars) > 1
    # push a forloop value onto the context
    loop = BoundedLoop('forloop', context, self.nodelist_loop, len_values)
    for value in values:
        if unpack:
            # if there are multiple loop variables, unpack the value into them
            context.update(dict(zip(self.loopvars, value)))
        else:
            context[self.loopvars[0]] = value
        status = loop.next()
        if unpack and status is loop.PASS:
            context.pop()
        if status is loop.BREAK:
            break
    return loop.render(close=True)
template.defaulttags.ForNode.render = render


class StopLoopException(Exception):
    def __init__(self, loop, continue_, nodelist=None):
        if not isinstance(loop, Loop):
            raise TypeError('Loop instance expected, %s given' % loop.__class__.__name__)
        super(StopLoopException, self).__init__(loop, continue_, nodelist)
        self.loop, self.continue_, self.nodelist = self.args


class Loop(dict):
    PASS = object()
    BREAK = object()
    CONTINUE = object()

    def __init__(self, name, context, nodelist):
        self._name = name
        self._context = context
        self._nodelist = nodelist
        self._rendered_nodelist = template.NodeList()
        self['parentloop'] = context.get(name)
        context.push()
        context[name] = self

    def render(self, close=False):
        if close:
            self.close()
        return self._rendered_nodelist.render(self._context)
    render.alters_data = True

    def next(self):
        if self._nodelist is None:
            raise RuntimeError('This loop is inactive')
        try: # update the exposed attributes
            counter = self['counter']
            self.update(counter0=counter, counter=counter+1, first=False)
        except KeyError:
            # initialize the exposed attributes the first time this is called
            self.update(counter0=0, counter=1, first=True)
        try:
            _render_nodelist_items(self._nodelist, self._context, self._rendered_nodelist)
            status = self.PASS
        except StopLoopException, ex:
            # if this is not the target loop, keep bubbling up the exception
            if ex.loop is not self:
                raise
            # pop context until (but excluding) the dict that contains this loop
            self._pop_context_until_self(inclusive=False)
            status = ex.continue_ and self.CONTINUE or self.BREAK
        return status
    next.alters_data = True

    def close(self):
        if self._nodelist:
            self._pop_context_until_self(inclusive=True)
            self._nodelist = None
    close.alters_data = True

    def _pop_context_until_self(self, inclusive):
        name = self._name
        dicts = self._context.dicts
        while len(dicts) > 1:
            if dicts[-1].get(name) is self:
                if inclusive:
                    del dicts[-1]
                break
            del dicts[-1]


class BoundedLoop(Loop):
    def __init__(self, name, context, nodelist, length):
        if length < 1:
            raise ValueError('Length must be at least 1')
        self._length = length
        super(BoundedLoop, self).__init__(name, context, nodelist)

    def next(self):
        try: # update the exposed attributes
            revcounter0 = self['revcounter0']
            if revcounter0 <= 0:
                raise RuntimeError('Attempted to call `next()` more than %d times' % self._length)
            self.update(revcounter0=revcounter0-1, revcounter=revcounter0, last=revcounter0==1)
        except KeyError:
            # initialize the exposed attributes the first time this is called
            length = self._length
            self.update(revcounter0=length-1, revcounter=length, last=length==1)
        return super(BoundedLoop, self).next()
    next.alters_data = True


def _render_nodelist_items(nodelist, context, result=None):
    if result is None:
        result = []
    for node in nodelist:
        if not isinstance(node, template.Node):
            result.append(node)
        else:
            try:
                result.append(nodelist.render_node(node, context))
            except Exception, ex:
                # get the wrapped exception if settings.DEBUG is True
                if hasattr(ex, 'exc_info'):
                    ex = ex.exc_info[1]
                # let every exception other than StopLoopException propagate
                if not isinstance(ex, StopLoopException):
                    raise
                # reraise the StopLoopException with the updated nodelist
                if ex.nodelist:
                    result.extend(ex.nodelist)
                ex.nodelist = result
                raise ex
    return result

@register.filter(name='toCurrency')
def toCurrency(price, request):
    from annoing.currencyManager import currencyManager
    from babel.numbers import format_number, format_decimal, format_percent
    
    current_currency = request.session.get('current_currency')
    currency_manager = currencyManager()

    try:
        znak = currency_manager.result[current_currency]['CharCode']
    except :
        znak = "EUR"

    if not current_currency:
        new_price = price
    else:
        new_price = currency_manager.convert(current_currency, price)

    new_price = str(format_decimal(new_price, locale='de_DE'))

    if len(new_price[new_price.find(","):len(new_price)]) > 2:
        new_price = new_price[0:new_price.find(",")+3]

    return str(new_price) + " " + znak

@register.filter(name='getEstateTypeName')
def getEstateTypeName(key):
    from estates.choices import ESTATE_TYPE_CHOICES

    choices = list(ESTATE_TYPE_CHOICES)
    for c in choices:
        k = list(c)
        if k[0] == key:
            return k[1]
    return None

def getEstateTypeSuffix(data):
    from world.models import Country, Region, City

    try:
        country = Country.objects.get(id=data.get('country'))
    except:
        return ''
    
    # Display region title
    if data.get("country", 0) and data.get('region',0) and not data.get('city', 0):
        try:
            r = Region.objects.get(id=data.get('region', 0)).name
            return r
        except:
            return ''
        
    # Display city title
    if data.get("country", 0) and data.get('city',0):
        try:
            return City.objects.get(id=data.get('city', 0)).name
        except:
            return ''

    if country:
        if translation.get_language() == 'ru':
            return country.otmenok
        else:
            return country.name

@register.filter(name="countryH1")
def countryH1(data):
    from world.models import Country, Region, City
    
    try:
        country = Country.objects.get(pk=data.get('country'))
    except:
        return ''
    
    # Display estate type
    if data.get("estate_type", 0) and data.get("estate_type", 0) != '0':
        try:
            typeLabel = getEstateTypeName(data.get("estate_type", 0))
            inStr = _(u"в")
            #result = "<h1>" + unicode(typeLabel) + " " + inStr + " " + getEstateTypeSuffix(data) + "</h1>"
            result = "<h1>%s %s %s</h1>" % (unicode(typeLabel), inStr, getEstateTypeSuffix(data))
            return result.replace('-','')
        except:
            return ''

    estate_in_str = _(u"Недвижимость в") + ''

    # Display region title
    if data.get("country", 0) and data.get('region',0) and not data.get('city',0):
        try:
            region = Region.objects.get(id=data.get('region', 0))
            return "%s%s %s%s" % ('<h1>',estate_in_str,region,'</h1>')
        except:
            return ''
        
    # Display city title
    if data.get("country", 0) and data.get('city',0):
        try:
            city = City.objects.get(id=data.get('city', 0))
            return "%s%s %s%s " % ('<h1>', estate_in_str,city,'</h1>')
        except:
            return ''

    if country:
        if country.h1:
            return u'<h1>%s %s</h1>' % (estate_in_str, country.h1)
        else:
            try:
                if translation.get_language() == 'ru':
                    return u'<h1>%s %s</h1>' % (estate_in_str, country.otmenok)
                else:
                    return u'<h1>%s %s</h1>' % (estate_in_str, country.name)
            except:
                return ''

@register.filter(name="countrySeoText")
def countrySeoText(data):
    from world.models import Country, Region, City

    if data.get('countryOnly', False) == False:
        return ''

    try:
        country = Country.objects.get(id=data.get('country', 0))
    except:
        return ''

    if country.seo_desc:
        return country.seo_desc
    else:
        return ''

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

@register.filter(name="citiesBox")
def citiesBox(data):    
    from world.models import Country
    from estates.choices import ESTATE_TYPE_CHOICES as etype
    from django.template.defaultfilters import capfirst

    try:
        country = Country.objects.get(id=data.get('country'))
    except:
        return ''

    result = ''

    for type in dict(etype):
        count = Apartament.objects.filter(estate_type=type, country=country, is_published=True).count()
        if count > 0:
            if translation.get_language() == 'ru':
                country_text = country.otmenok
            else:
                country_text = country.name
            result += u"<a href='/%s-in-%s-%s'>%s %s %s</a> (%s)<br/>" % (type, country.id, slugify(country.name_en), capfirst(_to_estate_type(type)), _(u"в"), country_text, count)

    return result


@register.filter(name="regionCities")
def regionCities(data):    
    from world.models import Country, City
    from django.db import connection
    from django.template.defaultfilters import capfirst

    try:
        country = Country.objects.get(id=data.get('country'))
        #cities = City.objects.filter(country = country)
        cursor=connection.cursor()
        cursor.execute("SELECT id, city_id FROM estates_apartament WHERE country_id=%s GROUP BY city_id LIMIT 20" % country.id)
        cities2 = cursor.fetchall()
        cities_list=[]
        for city_id in cities2:
            cities_list.append(city_id[1])
        cities = City.objects.filter(id__in=cities_list)
    except:
        return ''

    result = ''
    for city in cities:
        count = Apartament.objects.filter(country=country, city=city,is_published=True).count()
        if count > 0:
            result += u"<a href='/country-%s-%s/city-%s'>%s</a> (%s)<br/>" % (country.id, slugify(country.name_en), city.id, city.name, count)

    return result    


@register.filter(name="estateTypeSeoText")
def estateTypeSeoText(data):
    from estates.models import EstateTypeSeoText
    try:
        text = EstateTypeSeoText.objects.get(type_id = data.get('estate_type'), country = data.get('country'))
    except:
        return ''
    
    if translation.get_language() == 'ru':
        result = text.description_ru
    if translation.get_language() == 'en':
        result = text.description_en
    if translation.get_language() == 'de':
        result = text.description_de

    if result:
        return result
    return ''