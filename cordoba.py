#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
import re
import json

from plaza import plaza
from ciudad import ciudad

class cordoba(ciudad):
    def __init__(self,file ):
        self.pmrs = []
        tree = etree.parse(file, etree.HTMLParser())
        scripts = tree.findall(".//script")

        jsons_str = []

        # En cada script del html hay una parte a partir de map.addMarker() que es la que nos interesa
        for s in scripts:
            lista = str(s.text).split('map.addMarker(')
            if len(lista) > 1:
                    jsons_str.append(lista[1].split('\',')[0]+'\',')

        # El primer elemento no es una plaza, lo descartamos
        jsons_str.pop(0)

        for j in jsons_str:
            datos_del_titulo = self.json_title(j)
            direccion = datos_del_titulo['direccion']
            numero = datos_del_titulo['numero']
            num_plazas = datos_del_titulo['num_plazas']
            observacion = datos_del_titulo['observacion']
            lat = self.json_attr(j, "lat")
            lng = self.json_attr(j, "lng")

            self.pmrs.append(plaza(direccion, numero, num_plazas, observacion, lat, lng))


    def json_attr(self, str, attr):
            to_return = str.split(attr+":")[1]
            to_return = to_return.split(",")[0]
            return to_return.lstrip().rstrip()

    def json_title(self, str):
            to_return = {}
            #Nos quedamos con title: para abajo
            str = str.split("title:")[1]
            elementos = str.split(',')

            # No se me ocurre nada más para quitar todos los caracteres del principio
            to_return['direccion'] = elementos[0].lstrip().lstrip('\'\\').lstrip().rstrip()

            observacion = elementos[1].split('\\')[0].lstrip().rstrip()
            to_return['observacion'] = observacion

            numero = re.findall(r"Nº \d+", str)
            if (len(numero)):
                    to_return ['numero'] = re.sub("[^0-9]", "", numero[0])
            else:
                    to_return['numero'] = ""

            num_plazas = re.findall(r"\d+ PLAZA/S", str)
            if (len(num_plazas)):
                    to_return ['num_plazas'] = re.sub("[^0-9]", "", num_plazas[0])
            else:
                    to_return['num_plazas'] = ""

            return to_return
