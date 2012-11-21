from django.utils import translation
#from django.http import HttpResponseRedirect,HttpResponse
#from django.conf import settings

class LocaleMiddleware(object):
	def process_request(self, request):
		host = request.META['HTTP_HOST']
		if host == "en.worldimmotrade.ru":
			translation.activate("en")
		if host == "de.worldimmotrade.ru":
			translation.activate("de")
		if host == "worldimmotrade.ru":
			translation.activate("ru")
		if host == "worldimmotrade.com":
			translation.activate("en")
                if host == "worldimmotrade.de":
                        translation.activate("de")
                if host == "worldimmotrade.ru":
                        translation.activate("ru")
		if host == "www.worldimmotrade.com":
			translation.activate("en")
                if host == "www.worldimmotrade.de":
                        translation.activate("de")
                if host == "www.worldimmotrade.ru":
                        translation.activate("ru")
						


