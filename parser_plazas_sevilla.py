#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from plaza import plaza

tree = ET.parse('plazas_sevilla.htm')
root = tree.getroot()
