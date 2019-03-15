import os, sys, unittest

esto = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, esto + '/../')

from plaza import plaza

class TestPlaza( unittest.TestCase ):

    def test_should_create_object_OK(self):
        una_plaza = plaza( "C/ Pez", None, 1, None, None, None )
        self.assertIsInstance(una_plaza, plaza, "Creada correctamente" )
