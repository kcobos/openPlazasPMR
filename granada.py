#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

from plaza import plaza
from ciudad import ciudad

class granada(ciudad):
    """
       Parseo de los datos de Granada a partir de los datos de CGIM Granada
    """
    
    def __init__(self,file ):
        self.pmrs = []
        tree = ET.parse(file)
        root = tree.getroot()

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
                direccion = via
                num_ini = text.find("NÚMERO") + 17
                num_fin = text.find("</", num_ini)
                numero = text[num_ini:num_fin].strip()
                pla_ini = text.find("PLAZAS") + 17
                pla_fin = text.find("</", pla_ini)
                plazas =   text[pla_ini:pla_fin].strip()
                obs_ini = text.find("OBSERVACIÓN") + 22
                obs_fin = text.find("</", obs_ini)
                nota = text[obs_ini:obs_fin]

            for coor in node.iter("{http://www.opengis.net/kml/2.2}Point"):
                for c in coor.iter("{http://www.opengis.net/kml/2.2}coordinates"):
                    spl = c.text.split(",")
                    latitud  =  spl[1].strip()
                    longitud = spl[0].strip()

            self.pmrs.append(plaza(direccion, numero, plazas, nota, latitud, longitud))
