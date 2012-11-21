# -*- coding: utf-8 -*-
import urllib
import os

import xml.dom.minidom as dom
from xml.dom.minidom import Node

from django.contrib.sessions.models import Session
from django.core.cache import cache

class currencyManager():
    def __init__(self):
        if not cache.get('currencies_xml'):
            self.load_xml()
            self.parse_xml()
            cache.set('currencies_xml', self.result, 60*60*24)
        else:
            self.result = cache.get('currencies_xml')

    def parse_xml(self):
        ''' Parse xml to dict '''
        result = {}
        xml = dom.parseString(self.xml)
        valutes = xml.getElementsByTagName("Valute")
        for valute in valutes:
            result[valute.attributes["ID"].value] = {}
            for node in valute.childNodes:
                if node.__class__.__name__ == "Element":
                    result[valute.attributes["ID"].value][node.tagName] = node.childNodes[0].data

        result["RUBLES"] = {
            "NumCode": u"1111111",
            "CharCode": u"RUR",
            "Nominal": u"1",
            "Name": u"Рубли",
            "Value": u"1",
        }

        self.result = result

    def load_xml(self):
        ''' Load xml from url '''
        #try:
        #    request = urllib.urlopen("http://www.cbr.ru/scripts/XML_daily.asp")
        #    answer = request.read()
        #    self.xml = str(answer)
        #    request.close()
        #except:
        #    self.xml = open(os.path.dirname(__file__) + "/currencies.xml", "r").read()
        self.xml = open(os.path.dirname(__file__) + "/currencies.xml", "r").read()

    def toSelect(self, request):
        result = ""
        for c in self.getDict():
            try:
                cur_c = request.session['current_currency']
            except:
                cur_c = "R01239"

            if c == cur_c:
                selected = "selected"
            else:
                selected = ""

            result += "<option %s value='%s'>%s</option>" % (selected, c, self.result[c].get("CharCode"))
        return result

    def getDict(self):
        return self.result

    def convert(self, to_c, sum, from_c="R01239"):
        try:
            self.result[to_c]['Name']
        except:
            to_c = "R01239"

        if from_c == to_c:
            return sum

        valute_from = eval(self.result[from_c]['Value'].replace(',','.')) / int(self.result[from_c]['Nominal'])
        valute_to = eval(self.result[to_c]['Value'].replace(',','.')) / int(self.result[to_c]['Nominal'])
        v1_to_v2 = valute_from / valute_to

        if from_c == to_c:
            return 1
        else:
            return float(sum) * float(v1_to_v2)
