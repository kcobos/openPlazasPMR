
import os, sys, unittest

esto = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, esto + '/../')

from sevilla import sevilla

class TestCiudad( unittest.TestCase ):

    def test_should_create_object_OK(self):
        sevill = sevilla("https://www.google.com/maps/d/u/0/viewer?msa=0&hl=es&ie=UTF8&t=m&ll=37.395937%2C-5.997677000000067&spn=0.047732%2C0.085831&z=13&source=embed&mid=1zZf1zvrl4c9zgM4SejkoADrMhoQ")
        self.assertIsInstance(sevill, sevilla, "Creada correctamente" )
        self.assertIn( "Bécquer", sevill.csv(), "CSV correcto" )
        self.assertIn( "Boteros", sevill.csv(), "CSV correcto" )
        self.assertIn( "Calatrava", sevill.csv(), "CSV correcto" )
