# -*- coding: utf-8 -*-

import os
import re
import pprint
import xml.dom.minidom as dom
import urllib2, hashlib, os, time

from urllib2 import Request
from xml.dom.minidom import Node
from world.models import Region, City, Country
from estates.models import Apartament, Photo
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str, smart_unicode
from django.contrib.auth.models import User
from estates.forms import ApartmentForm
from annoing.currencyManager import currencyManager

class XMLSe():

	def __init__(self, file_path):
		self.file_path = file_path
		self.xml = open(file_path, "r").read()
		self.crossData = []

	def parse(self):
		xml = dom.parseString(self.xml)
		estates = xml.getElementsByTagName("offer")
		for e in estates:
			data = {}
			for node in e.childNodes:
				if node.__class__.__name__ == "Element":
					tagName = node.tagName

					try:
						tagValue = node.childNodes[0].nodeValue
						if(tagName == 'prices'):
							tagValue = node.childNodes[0].firstChild.nodeValue
							# tagValue = node.childNodes[1].firstChild.nodeValue
						if(tagName == 'description'):
							tagValue = node.childNodes[0].data
						if(tagName == 'areas'):
							#tagValue = [node.childNodes[1].childNodes[0].nodeValue, node.childNodes[3].childNodes[0].nodeValue]
							tagValue = node.childNodes[0].firstChild.nodeValue
						if(tagName == 'images'):
							tagValue = self.get_node_images(node)
					except:
						tagValue = ''

					data[tagName] = tagValue
			self.crossData.append(data)
		self.migrate()

	def get_node_images(self, node):
		result = []
		for e in node.childNodes:
			if(e.__class__.__name__ == 'Element'):
				result.append(e.firstChild.nodeValue)
		return result 

	def migrate(self):
		user = User.objects.get(pk=286)
		converter = currencyManager()
		n = 0
		for data in self.crossData:
			country =Country.objects.get(name=data.get('country'))

			try:
				region = Region.objects.get(name=data.get('state'))
			except:
				region = Region()
				region.name = data.get('state')
				region.country = country
				region.save()
				#print 'Created Region: %s' % region.name

			try:
				city = City.objects.get(region=region, name=data.get('town'))
			except:
				city = City()
				city.region = region
				city.country = country
				city.name = data.get('town')
				city.save()
				#print 'Created City: %s' % city.name

			name = self.get_title(data.get('description'))
			params = {
				'name': name,
				'name_ru': name,
				'name_en': name,
				'name_de': name,
				#'price': int(converter.convert('R01239', data['prices'], 'RUBLES')),
				'price': float(data['prices']),
				'description': data.get('description'),
				'description_ru': data.get('description'),
				'user': user,
				'type': 1, # Sale
				'rooms_count': 1,
				'total_space': int(float(data.get('areas'))),
				'living_space': int(float(data.get('areas'))),
				'estate_type': "apartment",
				'country': country.id,
				'region': region.id,
				'city': city.id
			}
			form = ApartmentForm(params)
			if form.is_valid():
				form.instance.is_published = True
				form2 = form.save(commit=False)
				form2.user = user
				form2.save()
				form.save_m2m()

				if len(data.get('images')) > 0:
					for photo in data.get('images'):
						try:
							pass
							file_name = hashlib.sha1(photo + str(time.time())).hexdigest() + '.jpg'
							print "Downloading photo..."
							request = Request(photo,
								headers={ 'User-Agent': 'Mozilla/5.0', 'Accept-Charset': 'utf-8' }
							)
							res = urllib2.urlopen(request)

							try:
								import os
								os.makedirs('/srv/www/vhosts/worldimmotrade.ru/httpdocs/immotrade/media/uploads/%s/%s' % (user.id, form2.id))
								# os.makedirs('/var/www/immotrade/media/uploads/%s/%s' % (user.id, form2.id))
							except:
								pass

							# f = open('/var/www/immotrade/media/uploads/%s/%s/%s' % (user.id, form2.id, file_name), 'w')
							f = open('/srv/www/vhosts/worldimmotrade.ru/httpdocs/immotrade/media/uploads/%s/%s/%s' % (user.id, form2.id, file_name), 'w')
							f.write(res.read())
							f.close()
							res.close() 

							# Create new DB object
							photo = Photo(apartament=form2, photo='uploads/%s/%s/%s' % (user.id, form2.id, file_name))
							photo.save()
						except:
							print "Error downloading photo %s" % photo
			else:
				print form.errors
			n=n+1
			print "Processing object %s" % (n)

	def get_city(self, name):
		country = Country.objects.get(pk=23)
		region = Region.objects.get(pk=5453)
		try:
			city = City.objects.get(region=region, name=name)
		except:
			city = City()
			city.name = name
			city.region = region
			city.country = country
			city.save()
		return city


	def get_title(self, data):
		return data.split('.')[0][:200]

