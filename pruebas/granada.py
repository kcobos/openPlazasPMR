# -*- coding: utf-8 -*-

import requests, zipfile, io, os
r = requests.get("http://www.movilidadgranada.com/kml/pmr201705.kmz")
z = zipfile.ZipFile(io.BytesIO(r.content))
try:
    os.mkdir("./granada")
except OSError as e:
    if (e.errno != 17):
        print("ERROR en la creación del directorio granada: {0}".format(e))
        exit(-1)

z.extractall("./granada")

for f in os.listdir("./granada"):
    os.remove("./granada/"+f)
os.rmdir("./granada")
