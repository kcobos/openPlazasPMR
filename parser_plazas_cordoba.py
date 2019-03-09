from lxml import etree
from io import BytesIO
import re
import json

archivo = open("cordoba.html", "rb")
tree = etree.parse(archivo, etree.HTMLParser())

scripts = tree.findall(".//script")
jsons_str = []
jsons = []


for s in scripts:
        lista = str(s.text).split('map.addMarker(')
        if len(lista) > 1:
                jsons_str.append(lista[1].split('\',')[0]+'\'\n}')

for j in jsons_str:
    print(j)
    


    
