
import os, sys, unittest

esto = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, esto + '/../')

from sevilla import sevilla

class TestCiudad( unittest.TestCase ):

    def test_should_create_object_OK(self):
        sevill = sevilla("plazas_sevilla.htm")
        self.assertIsInstance(sevill, sevilla, "Creada correctamente" )
        print(sevill)
        self.assertIn( "Bécquer", sevill.csv(), "CSV correcto" )
        self.assertIn( "Boteros", sevill.csv(), "CSV correcto" )
        self.assertIn( "Calatrava", sevill.csv(), "CSV correcto" )
