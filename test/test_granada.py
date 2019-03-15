
import os, sys, unittest

esto = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, esto + '/../')

from granada import granada

class TestCiudad( unittest.TestCase ):

    def test_should_create_object_OK(self):
        grana = granada("http://www.movilidadgranada.com/kml/pmr201705.kmz")
        self.assertIsInstance(grana, granada, "Creada correctamente" )
        print(grana)
        self.assertIn( "SAN", grana.csv(), "CSV correcto" )
        self.assertIn( "GORA", grana.csv(), "CSV correcto" )
        self.assertIn( "ANTONIO", grana.csv(), "CSV correcto" )
