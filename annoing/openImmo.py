# -*- coding: utf-8 -*-

import os
import re
import pprint
import xml.dom.minidom as dom

from xml.dom.minidom import Node
from world.models import Region, City, Country
from django.utils.translation import ugettext_lazy as _


class OpenImmoParser():

	def __init__(self, xml_file_path):
		self.result = {}
		self.errors = []
		self.region_id = 0
		self.city_id = 0
		self.country_id = 0
		self.load_xml(xml_file_path)

	def is_bool(self, v):
	  return v.lower() in ("yes", "true", "t", "1")

	def load_xml(self, path):
		self.xml = open(path, "r").read()

	def parse(self):
		xml = dom.parseString(self.xml)
		estates = xml.getElementsByTagName("immobilie")
		for e in estates:
			for node in e.childNodes:
				if node.__class__.__name__ == "Element":
					params = self.get_node_params(node)

	def get_node_params(self, node):
		self.result[node.tagName] = {}
		for params in node.childNodes:
			# Here goes values
			if params.__class__.__name__ == "Element":
				for param in params.childNodes:
					if param.__class__.__name__ == "Text":
						param_name = params.tagName 
						if node.tagName == "infrastruktur":
							param_name = "%s_%s" % (param_name, params.attributes.values()[0].value)
	
						self.result[node.tagName][param_name] = param.data
					else:
						#Get sub childs
						sub_childs = param.childNodes

	# Process geo params
	def process_geo(self):
		region_name = ""
		city_name = ""
		country_iso = ""

		try:
			city_name = self.result["geo"]["ort"]
		except:
			city_name = ""

		try:
			region_name = self.result["geo"]["bundesland"]
		except:
			region_name = ""

		if city_name == "":
			self.errors.append(_(u"Укажите название города"))
			return False

		try:
			xml = dom.parseString(self.xml)
			node = xml.getElementsByTagName("land")
			country_iso = node[0].attributes["iso_land"].value
		except:
			country_iso = ""

		# Search country by iso code
		code = ""
		f = open('iso.txt', 'r')
		for line in f.readlines():
			line = re.sub("\s+" , " ", line)
			try:
				test = line.split(" ")[-3:][0]
				if test == country_iso:
					code = line.split(" ")[0]
			except:
				pass
		
		# Search country
		country_model = None
		countries = Country.objects.all()
		for c in countries:
			code = code.lower()
			if code.find(c.name_en.lower()[:5]) >= 0:
				country_model = c

		try:
			city_model = City.objects.get(name=city_name)
			self.city_id = city_model.pk
			self.region_id = city_model.region.pk
			self.country_id = city_model.country.pk
			return True
		except:
			pass

		region_model = None
		if region_name == "": 
			self.errors.append(_(u"Укажите название региона"))
			return False
		
		if country_model:
			try:
				region_model = Region.objects.get(name=region_name)
			except:
				region_model = Region(name=region_name, country=country_model)
				region_model.save()

				# Search city
				try:
					city_model = City.objects.get(name=city_name)
				except:
					# City not found
					city_model = City(region=region_model,country=country_model,name=city_name)
					city_model.save()

			try:
				self.country_id = country_model.pk
				self.region_id = region_model.pk
				self.city_id = city_model.pk
			except:
				return False

			return True

		return False


	def get_type(self):
		try:
			xml = dom.parseString(self.xml)
			node = xml.getElementsByTagName("vermarktungsart")
			result = node[0].attributes["KAUF"].value
		except:
			result = "false"

		if result == "true":
			return 1
		else:
			return 2

	def get_commision(self):
		try:
			test = self.result["preise"]["aussen_courtage"]
			test = test.replace(",", ".")
			result = float(test)
		except:
			result = 0

		return float(result)

	def get_land_space(self):
		try:
			test = self.result["flaechen"]["grundstuecksflaeche"]
			test = test.replace(",", ".")
			result = int(float(test))
		except:
			result = 0

		return result

	def get_bedrooms_count(self):
		try:
			test = self.result["flaechen"]["anzahl_schlafzimmer"]
			result = int(float(test))
		except:
			result = 0

		return result

	def get_bathrooms_count(self):
		try:
			test = self.result["flaechen"]["anzahl_badezimmer"]
			result = int(float(test))
		except:
			result = 0

		return result

	def get_separate_toilets_count(self):
		try:
			test = self.result["flaechen"]["anzahl_sep_wc"]
			result = int(float(test))
		except:
			result = 0

		return result

	def get_parking_count(self):
		try:
			test = self.result["flaechen"]["anzahl_stellplaetze"]
			result = int(float(test))
		except:
			result = 0

		return result	

	def get_possible_redevelopment(self):
		try:
			test = self.result["ausstattung"]["raeume_veraenderbar"]
			result = self.is_bool(test)
		except:
			result = False

		return result	

	def get_wanne(self):
		try:
			xml = dom.parseString(self.xml)	
			test = xml.getElementsByTagName("bad")
			if self.is_bool(test[0].attributes["WANNE"].value) == True:
				return [1]
		except:
			return []

	def get_kamin(self):
		try:
			test = self.result["ausstattung"]["kamin"]
			result = self.is_bool(test)
		except:
			result = False

		return result	

	def get_sauna(self):
		try:
			test = self.result["ausstattung"]["sauna"]
			result = self.is_bool(test)
		except:
			result = False

		return result	


	def get_lift(self):
		try:
			xml = dom.parseString(self.xml)	
			test = xml.getElementsByTagName("fahrstuhl")
			if self.is_bool(test[0].attributes["PERSONEN"].value) == True:
				return True
		except:
			return False

	def get_condicioner(self):
		try:
			test = self.result["ausstattung"]["klimatisiert"]
			result = self.is_bool(test)
		except:
			result = False

		return result	

	def get_balkon(self):
		try:
			xml = dom.parseString(self.xml)	
			test = xml.getElementsByTagName("ausricht_balkon_terrasse")
			if self.is_bool(test[0].attributes["OST"].value) == True:
				return True
		except:
			return False		

	def get_garden(self):
		try:
			test = self.result["ausstattung"]["gartennutzung"]
			result = self.is_bool(test)
		except:
			result = False

		return result			

	def get_comfort(self):
		result = []
		try:
			# Kamin
			if self.get_kamin() == True:
				result.append(6)
			if self.get_lift() == True:
				result.append(1)
			if self.get_condicioner() == True:
				result.append(5)
			if self.get_balkon() == True:
				result.append(4)
			if self.get_sauna() == True:
				result.append(7)
			if self.get_garden() == True:
				result.append(2)
		except:
			return result

		return result

	def get_furnishings(self):
		result = []
		try:
			xml = dom.parseString(self.xml)	
			test = xml.getElementsByTagName("moebliert")
			if test[0].attributes["moeb"].value == "VOLL":
				result.append(1)
		except:
			pass

		return result

	def get_security_systems(self):
		result = []
		try:
			xml = dom.parseString(self.xml)	
			test = xml.getElementsByTagName("sicherheitstechnik")
			if test[0].attributes["ALARMANLAGE"].value == "true":
				result.append(1)
			if test[0].attributes["KAMERA"].value == "true":
				result.append(2)
			if test[0].attributes["POLIZEIRUF"].value == "true":
				result.append(4)				
		except:
			pass

		return result

	def get_other_facilies(self):
		result = []
		try:
			xml = dom.parseString(self.xml)	
			test = xml.getElementsByTagName("unterkellert")
			if test[0].attributes["keller"].value == "JA":
				result.append(6)
		except:
			pass

		return result

	
	def get_built_year(self):
		try:
			test = self.result["zustand_angaben"]["baujahr"]
			result = int(float(test))
		except:
			result = 0

		return result

	def get_distance_to(self, value):
		try:
			test = self.result["infrastruktur"][value]
			result = int(float(test))
		except:
			result = float(0)

		return result

	def get_oject_location(self):
		try:
			test = self.result["freitexte"]["lage"]
		except:
			test = ""

		return test
	
	def get_oject_description(self):
		try:
			test = self.result["freitexte"]["objektbeschreibung"]
		except:
			test = ""

		return test	

	def get_image_names(self):
		result = []
		xml = dom.parseString(self.xml)
		test = xml.getElementsByTagName("pfad")
		for image in test:
			image_name = image.childNodes[0].data 
			if image_name.endswith(".jpg") == True:
				result.append(image_name)
		return result
