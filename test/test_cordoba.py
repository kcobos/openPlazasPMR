
import os, sys, unittest

esto = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, esto + '/../')

from cordoba import cordoba

class TestCiudad( unittest.TestCase ):

    def test_should_create_object_OK(self):
        cordob = cordoba("https://movilidad.cordoba.es/informaciontrafico/index.php?minusvalidos=1&fechaInicio=2019-03-08")
        self.assertIsInstance(cordob, cordoba, "Creada correctamente" )

        print(cordob.csv())

        self.assertIn( "DOCTOR GREGORIO MARAÑON", cordob.csv(), "CSV correcto" )
        self.assertIn( "CRUZ DE JUAREZ", cordob.csv(), "CSV correcto" )
        self.assertIn( "DOCTOR BLANCO SOLER", cordob.csv(), "CSV correcto" )
