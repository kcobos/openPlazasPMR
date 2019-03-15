#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
import re, json
import requests

from plaza import plaza
from ciudad import ciudad

class sevilla(ciudad):
    """
       Parseo de los datos de Sevilla, a partir de los datos de la web del ayuntamiento
    """

    def __init__(self,url):

        r = requests.get(url)

        self.pmrs = []
        tree = etree.fromstring(r.text, etree.HTMLParser())
        scripts = tree.findall(".//script")
        data_script = None

        for s in scripts:

            if str(s.text).find("_pageData") != -1:
                data_script = str(s.text)
                break

        data_script = data_script.split("var _pageData = \"")[1]
        data = data_script[0:len(data_script)-4].replace("\\\\n","").replace("\\n","").replace("\\\"","\"")
        data = json.loads(data)
        data = data[1][6][0][12][0][13][0]

        for p in data:
            latitud = p[1][0][0][0]
            longitud = p[1][0][0][1]
            if p[5][0][1][0].find("Apartamiento") != -1:
                continue
            if p[5][0][1][0].find(",") != -1:
                partes = p[5][0][1][0].split(",")
                direccion = partes[0]
                if len(partes) == 2:
                    numero = partes[1]
                else:
                    numero = None
            nota = p[5][1][1][0]
            plazas = None
            self.pmrs.append(plaza(direccion, numero, plazas, nota, latitud, longitud))
