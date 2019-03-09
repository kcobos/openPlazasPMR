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
data = data[1][6][0][4]+data[1][6][0][12]
data = data[0:140]
for i in range(len(data)):
    print(i)
    print(data[i])
    print("\n\n")
