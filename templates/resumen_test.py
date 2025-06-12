import unittest

# Importamos el codigo a testear.
from resumen import Resumen

####################################################################

class TestResumen(unittest.TestCase):

    def test_creacion(self):
        r = Resumen(100, 8.5, 5.1, 7.45, 0.3, 0.7)
        self.assertEqual(r.cantidad, 100)
        self.assertAlmostEqual(r.promedio_matematica, 8.5)
        self.assertAlmostEqual(r.promedio_lengua, 5.1)
        self.assertAlmostEqual(r.promedio_nse, 7.45)
        self.assertAlmostEqual(r.proporcion_ambito_rural, 0.3)
        self.assertAlmostEqual(r.proporcion_sector_estatal, 0.7)

    def test_repr(self):
        r = Resumen(2663, 8.967, 3.544, 4.369, 0.21, 0.69)
        esperado = "<Mat:8.97, Len:3.54, NSE:4.37, Rural:0.21, Estado:0.69, N:2663>"
        self.assertEqual(repr(r), esperado)

    def test_eq_true(self):
        r1 = Resumen(1000, 8.001, 7.002, 4.3009, 0.3004, 0.6996)
        r2 = Resumen(1000, 8.0005, 7.0024, 4.3001, 0.3005, 0.6995)
        self.assertTrue(Resumen.__eq__(r1, r2))

    def test_eq_false_por_cantidad(self):
        r1 = Resumen(1000, 8.0, 7.0, 4.3, 0.3, 0.7)
        r2 = Resumen(999, 8.0, 7.0, 4.3, 0.3, 0.7)
        self.assertFalse(Resumen.__eq__(r1, r2))

    def test_eq_false_por_float(self):
        r1 = Resumen(1000, 8.0, 7.0, 4.3, 0.3, 0.7)
        r2 = Resumen(1000, 8.0, 7.0, 4.3, 0.3, 0.702)
        self.assertFalse(Resumen.__eq__(r1, r2))

    def test_repr_redondeo(self):
        r = Resumen(1, 9.995, 0.02, 10.01, 0.99, 0.01)
        esperado = "<Mat:9.99, Len:0.02, NSE:10.01, Rural:0.99, Estado:0.01, N:1>"
        self.assertEqual(repr(r), esperado)

    def test_eq_true_muchos_redondeos(self):
        r1 = Resumen(333, 0.0049, 9.995, 5.0005, 0.0001, 0.9999)
        r2 = Resumen(333, 0.0051, 9.994, 5.0004, 0.0002, 0.9998)
        self.assertTrue(r1 == r2)


## y asi con el resto de los metodos a testear.
        
####################################################################

unittest.main()