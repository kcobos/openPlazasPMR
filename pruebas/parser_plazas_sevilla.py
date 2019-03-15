#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
import re
import json
from plaza import plaza

tree = etree.parse("plazas_sevilla.htm", etree.HTMLParser())
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

# print("\"direccion\";\"numero\";\"num_plazas\";\"observacion\";\"latitud\";\"longitud\"")
plazas = []

# latitud = data[i][1][0][0]
# longitud = data[i][1][0][1]
# direccion = data[i][5][0][1].split(",")[0]
# numero = data[i][5][0][1].split(",")[1]
# observacion = data[i][5][1][1]

for i in range(len(data)):
    print(i)
    print(data[i])
    print("\n\n")
