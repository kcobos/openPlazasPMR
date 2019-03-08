#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
import re
from plaza import plaza

tree = etree.parse("plazas_sevilla.htm", etree.HTMLParser())
scripts = tree.findall(".//script")
data_script = None

for s in scripts:

    if str(s.text).find("_pageData") != -1:
        data_script = str(s.text)
        break

regex = '"\[\[(.+)\]\\n\]\\n";'
x = re.findall(regex, data_script)
print(x)
