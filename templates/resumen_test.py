import unittest

# Importamos el codigo a testear.
from resumen import Resumen
from estudiante import Estudiante

####################################################################

class TestResumen(unittest.TestCase):

    def test_creacion(self):
        estudiantes: list[Estudiante] = [
            Estudiante('CHU', 8.5, 5.1, 7.45, 'rural', 'estatal'),
            Estudiante('CHU', 8.5, 5.1, 7.45, 'urbano', 'estatal'), 
            Estudiante('CHU', 8.5, 5.1, 7.45, 'urbano', 'privado'),
        ]
        r = Resumen(estudiantes)
        self.assertEqual(r.cantidad, 3)
        self.assertAlmostEqual(r.promedio_matematica, 8.5)
        self.assertAlmostEqual(r.promedio_lengua, 5.1)
        self.assertAlmostEqual(r.promedio_nse, 7.45)
        self.assertAlmostEqual(r.proporcion_ambito_rural, 1/3)
        self.assertAlmostEqual(r.proporcion_sector_estatal, 2/3)
        
        estudiantes2: list[Estudiante] = [
            Estudiante('CHU', 9.0, 6.0, 8.0, 'rural', 'estatal'),
            Estudiante('CHU', 9.0, 6.0, 8.0, 'urbano', 'estatal'), 
            Estudiante('CHU', 9.0, 6.0, 8.0, 'urbano', 'privado'),
            Estudiante('CHU', 9.0, 6.0, 8.0, 'urbano', 'privado'),
            Estudiante('CHU', 9.0, 6.0, 8.0, 'urbano', 'privado'),
        ]
        r2 = Resumen(estudiantes2)
        self.assertEqual(r2.cantidad, 5)
        self.assertAlmostEqual(r2.promedio_matematica, 9.0)
        self.assertAlmostEqual(r2.promedio_lengua, 6.0)
        self.assertAlmostEqual(r2.promedio_nse, 8.0)
        self.assertAlmostEqual(r2.proporcion_ambito_rural, 1/5)
        self.assertAlmostEqual(r2.proporcion_sector_estatal, 2/5)

    def test_repr(self):
        estudiantes: list[Estudiante] = [
            Estudiante('CHU', 8.967, 3.544, 4.369, 'rural', 'estatal'),
            Estudiante('CHU', 8.967, 3.544, 4.369, 'urbano', 'estatal'), 
            Estudiante('CHU', 8.967, 3.544, 4.369, 'urbano', 'estatal'),
            Estudiante('CHU', 8.967, 3.544, 4.369, 'urbano', 'estatal'),
            Estudiante('CHU', 8.967, 3.544, 4.369, 'urbano', 'privado'),
        ]
        r = Resumen(estudiantes)
        esperado = "<Mat:8.97, Len:3.54, NSE:4.37, Rural:0.2, Estado:0.8, N:5>"
        self.assertEqual(repr(r), esperado)
        
        estudiantes2: list[Estudiante] = [
            Estudiante('CHU', 7.50, 4.50, 6.5, 'rural', 'estatal'),
            Estudiante('CHU', 7.50, 4.50, 6.5, 'urbano', 'estatal'), 
            Estudiante('CHU', 7.50, 4.50, 6.5, 'urbano', 'estatal'),
            Estudiante('CHU', 7.50, 4.50, 6.5, 'urbano', 'privado'),
        ]
        r2 = Resumen(estudiantes2)
        esperado2 = "<Mat:7.5, Len:4.5, NSE:6.5, Rural:0.25, Estado:0.75, N:4>"
        self.assertEqual(repr(r2), esperado2)

    def test_eq_true(self):
        estudiantes: list[Estudiante] = [
            Estudiante('CHU', 8.9999, 3.5, 4.369, 'rural', 'estatal'),
            Estudiante('CHU', 8.9999, 3.5, 4.369, 'urbano', 'estatal'), 
            Estudiante('CHU', 8.9999, 3.5, 4.369, 'urbano', 'estatal'),
            Estudiante('CHU', 8.9999, 3.5, 4.369, 'urbano', 'estatal'),
            Estudiante('CHU', 8.9999, 3.5, 4.369, 'urbano', 'privado'),
        ]
        r1 = Resumen(estudiantes)
        print(r1)
        estudiantes2: list[Estudiante] = [
            Estudiante('CHU', 9.00001, 3.50001, 4.368, 'rural', 'estatal'),
            Estudiante('CHU', 9.00001, 3.50001, 4.368, 'urbano', 'estatal'), 
            Estudiante('CHU', 9.00001, 3.50001, 4.368, 'urbano', 'estatal'),
            Estudiante('CHU', 9.00001, 3.50001, 4.368, 'urbano', 'estatal'),
            Estudiante('CHU', 9.00001, 3.50001, 4.368, 'urbano', 'privado'),
        ]
        r2 = Resumen(estudiantes2)
        print(r2)
        self.assertTrue(Resumen.__eq__(r1, r2))
        
    #     r3 = Resumen(1500, 7.9999, 6.9998, 5.0001, 0.2001, 0.7999)
    #     r4 = Resumen(1500, 8.00, 7.00, 5.00, 0.20, 0.80)
    #     self.assertTrue(Resumen.__eq__(r3, r4))

    # def test_eq_false_por_cantidad(self):
    #     r1 = Resumen(1000, 8.0, 7.0, 4.3, 0.3, 0.7)
    #     r2 = Resumen(999, 8.0, 7.0, 4.3, 0.3, 0.7)
    #     self.assertFalse(Resumen.__eq__(r1, r2))
        
    #     r3 = Resumen(500, 9.0, 8.0, 7.0, 0.4, 0.6)
    #     r4 = Resumen(501, 9.0, 8.0, 7.0, 0.4, 0.6)
    #     self.assertFalse(Resumen.__eq__(r3, r4))
        
    #     r5 = Resumen(2000, 7.5, 6.5, 5.5, 0.25, 0.75)
    #     r6 = Resumen(1999, 7.5, 6.5, 5.5, 0.25, 0.75)
    #     self.assertFalse(Resumen.__eq__(r5, r6))

    # def test_eq_false_por_float(self):
    #     r1 = Resumen(1000, 8.0, 7.0, 4.3, 0.3, 0.7)
    #     r2 = Resumen(1000, 8.0, 7.0, 4.3, 0.3, 0.702)
    #     self.assertFalse(Resumen.__eq__(r1, r2))
        
    #     r3 = Resumen(1000, 8.0, 7.0, 4.3, 0.3, 0.7)
    #     r4 = Resumen(1000, 8.02, 7.0, 4.3, 0.3, 0.7)
    #     self.assertFalse(Resumen.__eq__(r3, r4))
        
    #     r5 = Resumen(1000, 8.0, 7.0, 4.3, 0.3, 0.7)
    #     r6 = Resumen(1000, 8.0, 7.0, 4.3, 0.31, 0.7)
    #     self.assertFalse(Resumen.__eq__(r5, r6))

    # def test_repr_redondeo(self):
    #     r = Resumen(1, 9.99232, 0.01340202, 10.01912121, 0.99, 0.01)
    #     esperado = "<Mat:9.99, Len:0.01, NSE:10.02, Rural:0.99, Estado:0.01, N:1>"
    #     self.assertEqual(repr(r), esperado)
        
    #     r2 = Resumen(100, 8.56789, 7.43210, 5.98765, 0.12345, 0.87654)
    #     esperado2 = "<Mat:8.57, Len:7.43, NSE:5.99, Rural:0.12, Estado:0.88, N:100>"
    #     self.assertEqual(repr(r2), esperado2)
        
    #     r3 = Resumen(50, 0.00123, 0.00456, 0.00789, 0.00012, 0.00034)
    #     esperado3 = "<Mat:0.0, Len:0.0, NSE:0.01, Rural:0.0, Estado:0.0, N:50>"
    #     self.assertEqual(repr(r3), esperado3)

    # def test_eq_true_muchos_redondeos(self):
    #     r1 = Resumen(333, 0.0049, 9.995, 5.0005, 0.0001, 0.9999)
    #     r2 = Resumen(333, 0.0051, 9.994, 5.0004, 0.0002, 0.9998)
    #     self.assertTrue(r1 == r2)
        
    #     r3 = Resumen(500, 8.0001, 6.0001, 5.00001, 0.5001, 0.500000001)
    #     r4 = Resumen(500, 8.0, 6.0, 5.0, 0.50, 0.50)
    #     self.assertTrue(r3 == r4)
        
    #     r5 = Resumen(1000, 0.00999999, 0.00000099, 0.9999999099, 3.0100000012121212, 0.00099999999)
    #     r6 = Resumen(1000, 0.01, 0.00, 1.00, 3.01, 0.0)
    #     self.assertTrue(r5 == r6)

    # def resumen_vacio(self):
    #     r = Resumen('', 0, 0, 0, '', '')
    #     esperado = "<Mat:, Len:, NSE:, Rural:, Estado:, N:>"
    #     self.assertEqual(repr(r), esperado)
    #     r2 = Resumen('', 0, 0, 0, '', '')
    #     esperado2 = "<Mat:0, Len:0, NSE:0, Rural:0, Estado:0, N:0>"
    #     self.assertEqual(repr(r2), esperado)


## y asi con el resto de los metodos a testear.
        
####################################################################

unittest.main()