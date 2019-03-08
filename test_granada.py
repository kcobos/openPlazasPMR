
import os, sys, unittest

esto = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, esto + '/../')

from granada import granada

class TestCiudad( unittest.TestCase ):

    def test_should_create_object_OK(self):
        grana = granada("plazas_granada.kml")
        self.assertIsInstance(grana, granada, "Creada correctamente" )
        print(grana)
        self.assertIn( "Percebe", grana.csv(), "CSV correcto" )
        
