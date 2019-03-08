#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
tree = ET.parse('plazas_granada.kml')
root = tree.getroot()

print("\"id\";\"direccion\";\"numero\";\"num_plazas\";\"observacion\";\"latitud\";\"longitud\"")
id = 0
for node in tree.findall("{http://www.opengis.net/kml/2.2}Document/{http://www.opengis.net/kml/2.2}Folder/{http://www.opengis.net/kml/2.2}Placemark"):
    # print(node.tag, node.attrib,)# node.text)
    for des in node.iter("{http://www.opengis.net/kml/2.2}description"):
        text = des.text
        via_ini = text.find("VÍA") + 14
        via_fin = text.find("</", via_ini)
        via_arr = text[via_ini:via_fin].split(",")
        via = via_arr[1:]+[via_arr[0]]
        via = " ".join(via)
        via = via.replace("  ", " ").strip()
        print(id,";\"",via,"\"", sep="", end="")
        num_ini = text.find("NÚMERO") + 17
        num_fin = text.find("</", num_ini)
        print(";\"", text[num_ini:num_fin].strip(), "\"", sep="", end="")
        pla_ini = text.find("PLAZAS") + 17
        pla_fin = text.find("</", pla_ini)
        print(";", text[pla_ini:pla_fin].strip(), sep="", end="")
        obs_ini = text.find("OBSERVACIÓN") + 22
        obs_fin = text.find("</", obs_ini)
        print(";\"", text[obs_ini:obs_fin], "\"", sep="", end="")
    for coor in node.iter("{http://www.opengis.net/kml/2.2}Point"):
        for c in coor.iter("{http://www.opengis.net/kml/2.2}coordinates"):
            spl = c.text.split(",")
            print(";", spl[1].strip(), sep="", end="")
            print(";", spl[0].strip(), sep="")
    id+=1