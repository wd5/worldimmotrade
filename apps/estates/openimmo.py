# -*- coding: utf-8 -*-
# View file

import fnmatch
import os
import shutil
import hashlib
import time

from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _

from estates.forms import ApartmentForm, PhotoForm, SearchForm, ApartmentViewForm
from estates.models import Apartament, Photo, Bookmarks, Document
from users.models import UserProfile
from annoing.openImmo import OpenImmoParser
from annoing.zipManager import ZipManager
from django.conf import settings

@login_required
def upload(request):
	error = False
	uploaded = False
	errors = []
	if request.POST:
		file = request.FILES['file']	
		if file.name.endswith(".zip"):
		
			extract_path = "%s%s/" % (settings.TEMP_PATH, hashlib.sha1(file.name + str(time.time())).hexdigest())
			os.mkdir(extract_path)
			zip_file_path = "%s%s" % (extract_path, hashlib.sha1(file.name).hexdigest() + ".zip")

			destination = open(zip_file_path, 'wb+')
			for chunk in file.chunks():
				destination.write(chunk)
			destination.close()

			# Read uploaded zip file
			zip = ZipManager()
			zip.read_file(zip_file_path)
			zip.extract(extract_path)

			# Find all xml files
			for xmlfile in os.listdir(extract_path):
				if fnmatch.fnmatch(xmlfile, '*.xml'):
					result = _process_import(request, xmlfile, extract_path)
					if result:
						errors.append(result[0])

			# Clear tmp file
			shutil.rmtree(extract_path)
			uploaded = True


	return direct_to_template(request, "estates/openimmo.html", {
		'error':error,
		'errors': errors,
		'uploaded': uploaded
	})

def _process_import(request, xml_name, extract_path):
	xml_path = "%s%s" % (extract_path, xml_name)
	user = request.user
	params = {}

	parser = OpenImmoParser(xml_path)
	parser.parse()
	geo_result = parser.process_geo()

	if geo_result == False:
		return parser.errors

	xml = parser.result
	
	try:
		name =	xml["freitexte"]["objekttitel"]
	except:
		name = "Object Name"

	params["name_ru"] = name
	params["name_en"] = name
	params["name_de"] = name
	params["type"] = parser.get_type()
	params["city"] =  parser.city_id
	params["region"] = parser.region_id
	params["country"] = parser.country_id
	params["price"] = xml["preise"]["kaufpreis"]
	params["estate_type"] = "villa"
	params["living_space"] = int(float(xml["flaechen"]["wohnflaeche"]))
	params["rooms_count"] = int(float(xml["flaechen"]["anzahl_zimmer"]))
	params["commission"] = parser.get_commision()
	params["land_space"] = parser.get_land_space()
	params["bedrooms_count"] = parser.get_bedrooms_count() 
	params["bathrooms_count"] = parser.get_bathrooms_count() 
	params["separate_toilets_count"] = parser.get_separate_toilets_count() 
	params["parking_count"] = parser.get_parking_count()
	params["possible_redevelopment"] = parser.get_possible_redevelopment() 
	params["bathroom"] = parser.get_wanne()
	params["comfort"] = parser.get_comfort()
	params["furnishings"] = parser.get_furnishings() 
	params["security_systems"] = parser.get_security_systems()
	params["other_facilies"] = parser.get_other_facilies()
	params["built_year"] = parser.get_built_year() 
	params["dist_to_highway"] = parser.get_distance_to("distanzen_AUTOBAHN")
	params["dist_to_station"] = parser.get_distance_to("distanzen_BUS")
	params["dist_to_airport"] = parser.get_distance_to("distanzen_FLUGHAFEN")
	params["dist_to_school"] = parser.get_distance_to("distanzen_REALSCHULE")
	params["dist_to_kindergarten"] = parser.get_distance_to("distanzen_KINDERGAERTEN")
	params["dist_to_centre"] = parser.get_distance_to("distanzen_ZENTRUM")
	params["dist_to_sea"] = parser.get_distance_to("distanzen_sport_MEER")
	params["dist_to_recreation"] = parser.get_distance_to("distanzen_sport_NAHERHOLUNG")
	params["dist_to_slopes"] = parser.get_distance_to("distanzen_sport_SKIGEBIET")
	params["dist_to_sports"] = parser.get_distance_to("distanzen_sport_SPORTANLAGEN")
	params["dist_to_beach"] = parser.get_distance_to("distanzen_sport_STRAND")
	params["object_location_ru"] = parser.get_oject_location()
	params["object_location_en"] = parser.get_oject_location()
	params["object_location_de"] = parser.get_oject_location()
	params["description_ru"] = parser.get_oject_description()
	params["description_en"] = parser.get_oject_description()
	params["description_de"] = parser.get_oject_description()

	#apartment_model = get_object_or_404(Apartament, pk=872, user=request.user)
	#form = ApartmentForm(params, instance=apartment_model)
	form = ApartmentForm(params)
	if form.is_valid():
		form2 = form.save(commit=False)
		form2.user = user
		form2.save()
		form.save_m2m()

		# Apply photos
		for file in parser.get_image_names():
			try:
				file_name = hashlib.sha1(file + str(time.time())).hexdigest() + '.jpg'	
				uploaded_file_path = "%s%s" % (extract_path, file)
				save_path = settings.PATH_TO_UPLOADS + 'uploads/%s/%s/%s' % (request.user.pk, form2.id, file_name) 
				shutil.copyfile(uploaded_file_path, save_path)
				photo = Photo(apartament=form2, photo='uploads/%s/%s/%s' % (request.user.pk, form2.id, file_name))
				photo.save()
			except:
				pass
	else:
		#print "Form Errors"
		#print form.errors	
		pass

