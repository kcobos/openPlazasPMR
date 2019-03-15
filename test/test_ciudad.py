
import os, sys, unittest

esto = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, esto + '/../')

from plaza import plaza
from ciudad import ciudad

class TestCiudad( unittest.TestCase ):

    def test_should_create_object_OK(self):
        una_plaza = plaza( "C/ Pez", None, 1, None, None, None )
        otra_plaza = plaza( "Rue del Percebe", 13, 1, None, None, None )
        una_ciudad = ciudad("da igual")
        self.assertIsInstance(una_ciudad, ciudad, "Creada correctamente" )
        una_ciudad.add( una_plaza )
        una_ciudad.add( otra_plaza )
        self.assertEqual( len(una_ciudad.pmrs), 2, "Plazas añadidas" )
        print(una_ciudad)
        self.assertIn( "Percebe", una_ciudad.csv(), "CSV correcto" )
