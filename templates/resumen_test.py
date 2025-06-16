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
        esperado = "<Mat:8.97, Len:3.54, NSE:4.37, Rural:0.20, Estado:0.80, N:5>"
        self.assertEqual(repr(r), esperado)
        
        estudiantes2: list[Estudiante] = [
            Estudiante('CHU', 7.50, 4.50, 6.5, 'rural', 'estatal'),
            Estudiante('CHU', 7.50, 4.50, 6.5, 'urbano', 'estatal'), 
            Estudiante('CHU', 7.50, 4.50, 6.5, 'urbano', 'estatal'),
            Estudiante('CHU', 7.50, 4.50, 6.5, 'urbano', 'privado'),
        ]
        r2 = Resumen(estudiantes2)
        esperado2 = "<Mat:7.50, Len:4.50, NSE:6.50, Rural:0.25, Estado:0.75, N:4>"
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
        estudiantes2: list[Estudiante] = [
            Estudiante('CHU', 9.00001, 3.50001, 4.368, 'rural', 'estatal'),
            Estudiante('CHU', 9.00001, 3.50001, 4.368, 'urbano', 'estatal'), 
            Estudiante('CHU', 9.00001, 3.50001, 4.368, 'urbano', 'estatal'),
            Estudiante('CHU', 9.00001, 3.50001, 4.368, 'urbano', 'estatal'),
            Estudiante('CHU', 9.00001, 3.50001, 4.368, 'urbano', 'privado'),
        ]
        r2 = Resumen(estudiantes2)
        self.assertTrue(Resumen.__eq__(r1, r2))
        
        estudiantes3: list[Estudiante] = [
            Estudiante('CHU', 7.9999, 6.9998, 5.0001, 'rural', 'privado'),
            Estudiante('CHU', 7.9999, 6.9998, 5.0001, 'rural', 'privado'), 
            Estudiante('CHU', 7.9999, 6.9998, 5.0001, 'rural', 'privado'),
            Estudiante('CHU', 7.9999, 6.9998, 5.0001, 'rural', 'privado'),
            Estudiante('CHU', 7.9999, 6.9998, 5.0001, 'rural', 'privado'),
        ]
        r3 = Resumen(estudiantes3)
        estudiantes4: list[Estudiante] = [
            Estudiante('CHU', 8.00, 7.00, 5.00, 'rural', 'privado'),
            Estudiante('CHU', 8.00, 7.00, 5.00, 'rural', 'privado'), 
            Estudiante('CHU', 8.00, 7.00, 5.00, 'rural', 'privado'),
            Estudiante('CHU', 8.00, 7.00, 5.00, 'rural', 'privado'),
            Estudiante('CHU', 8.00, 7.00, 5.00, 'rural', 'privado'),
        ]
        r4 = Resumen(estudiantes4)
        self.assertTrue(Resumen.__eq__(r3, r4))

    def test_eq_false_por_cantidad(self):
        estudiantes: list[Estudiante] = [
            Estudiante('CHU', 8.00, 7.00, 5.00, 'rural', 'privado'),
            Estudiante('CHU', 8.00, 7.00, 5.00, 'rural', 'privado'), 
            Estudiante('CHU', 8.00, 7.00, 5.00, 'rural', 'privado'),
            Estudiante('CHU', 8.00, 7.00, 5.00, 'rural', 'privado'),
            Estudiante('CHU', 8.00, 7.00, 5.00, 'rural', 'privado'),
        ]
        r1 = Resumen(estudiantes)
        estudiantes2: list[Estudiante] = [
            Estudiante('CHU', 8.00, 7.00, 5.00, 'rural', 'privado'),
            Estudiante('CHU', 8.00, 7.00, 5.00, 'rural', 'privado'), 
            Estudiante('CHU', 8.00, 7.00, 5.00, 'rural', 'privado'),
            Estudiante('CHU', 8.00, 7.00, 5.00, 'rural', 'privado'),
            Estudiante('CHU', 8.00, 7.00, 5.00, 'rural', 'privado'),
            Estudiante('CHU', 8.00, 7.00, 5.00, 'rural', 'privado'),
        ]
        r2 = Resumen(estudiantes2)
        self.assertFalse(Resumen.__eq__(r1, r2))
        
        estudiantes3: list[Estudiante] = [
            Estudiante('SFE', 5.23, 9.120, 3.410, 'rural', 'privado'),
            Estudiante('SFE', 5.23, 9.120, 3.410, 'rural', 'privado'), 
            Estudiante('SFE', 5.23, 9.120, 3.410, 'rural', 'privado'),
            Estudiante('SFE', 5.23, 9.120, 3.410, 'rural', 'privado'),
            Estudiante('SFE', 5.23, 9.120, 3.410, 'rural', 'privado'),
            Estudiante('SFE', 5.23, 9.120, 3.410, 'rural', 'privado'),
            Estudiante('SFE', 5.23, 9.120, 3.410, 'rural', 'privado'),
        ]
        r3 = Resumen(estudiantes3)
        estudiantes4: list[Estudiante] = [
            Estudiante('SFE', 5.23, 9.120, 3.410, 'rural', 'privado'),
            Estudiante('SFE', 5.23, 9.120, 3.410, 'rural', 'privado'), 
            Estudiante('SFE', 5.23, 9.120, 3.410, 'rural', 'privado'),
            Estudiante('SFE', 5.23, 9.120, 3.410, 'rural', 'privado'),
            Estudiante('SFE', 5.23, 9.120, 3.410, 'rural', 'privado'),
            Estudiante('SFE', 5.23, 9.120, 3.410, 'rural', 'privado'),
        ]
        r4 = Resumen(estudiantes4)
        self.assertFalse(Resumen.__eq__(r3, r4))

    def test_eq_false_por_float(self):
        estudiantes: list[Estudiante] = [
            Estudiante('SFE', 8.0, 7.0, 4.3, 'rural', 'privado'),
            Estudiante('SFE', 8.0, 7.0, 4.3, 'urbano', 'privado'), 
            Estudiante('SFE', 8.0, 7.0, 4.3, 'rural', 'privado'),
            Estudiante('SFE', 8.0, 7.0, 4.3, 'urbano', 'privado'),
            Estudiante('SFE', 8.0, 7.0, 4.3, 'rural', 'estatal'),
            Estudiante('SFE', 8.0, 7.0, 4.3, 'rural', 'privado'),
        ]
        r1 = Resumen(estudiantes)
        estudiantes2: list[Estudiante] = [
            Estudiante('SFE', 8.0, 7.0, 4.21, 'rural', 'privado'),
            Estudiante('SFE', 8.0, 7.0, 4.4, 'rural', 'estatal'), 
            Estudiante('SFE', 8.0, 7.0, 4.7, 'rural', 'privado'),
            Estudiante('SFE', 8.0, 7.0, 4.3, 'urbano', 'estatal'),
            Estudiante('SFE', 8.0, 7.0, 4.3, 'rural', 'privado'),
            Estudiante('SFE', 8.0, 7.0, 4.3, 'rural', 'estatal'),
        ]
        r2 = Resumen(estudiantes2)
        self.assertFalse(Resumen.__eq__(r1, r2))
        
        estudiantes3: list[Estudiante] = [
            Estudiante('SFE', 8.0, 7.0, 4.3, 'rural', 'privado'),
            Estudiante('SFE', 8.0, 7.0, 4.3, 'urbano', 'estatal'), 
            Estudiante('SFE', 8.0, 7.0, 4.3, 'urbano', 'privado'),
            Estudiante('SFE', 8.0, 7.0, 4.3, 'urbano', 'privado'),
            Estudiante('SFE', 8.0, 7.0, 4.3, 'rural', 'privado'),
            Estudiante('SFE', 8.0, 7.0, 4.3, 'rural', 'estatal'),
        ]
        r3 = Resumen(estudiantes3)
        estudiantes4: list[Estudiante] = [
            Estudiante('SFE', 9.0, 7.0, 4.21, 'urbano', 'privado'),
            Estudiante('SFE', 8.0, 7.0, 4.4, 'rural', 'privado'), 
            Estudiante('SFE', 8.0, 7.0, 4.7, 'urbano', 'privado'),
            Estudiante('SFE', 8.0, 7.0, 4.3, 'rural', 'estatal'),
            Estudiante('SFE', 8.0, 7.0, 4.3, 'urbano', 'estatal'),
            Estudiante('SFE', 8.0, 7.0, 4.3, 'urbano', 'estatal'),
        ]
        r4 = Resumen(estudiantes4)
        self.assertFalse(Resumen.__eq__(r3, r4))
        
        estudiantes5: list[Estudiante] = [
            Estudiante('SFE', 8.0, 7.0, 4.3, 'ubrano', 'privado'),
            Estudiante('SFE', 8.0, 5.0, 6.3, 'urbano', 'estatal'), 
            Estudiante('SFE', 8.0, 7.0, 4.3, 'urbano', 'privado'),
            Estudiante('SFE', 1.0, 1.0, 2.3, 'urbano', 'privado'),
            Estudiante('SFE', 8.0, 7.0, 4.3, 'urbano', 'estatal'),
            Estudiante('SFE', 8.0, 7.0, 8.3, 'urbano', 'estatal'),
        ]
        r5 = Resumen(estudiantes5)
        estudiantes6: list[Estudiante] = [
            Estudiante('SFE', 8.0, 9.0, 4.21, 'urbano', 'estatal'),
            Estudiante('SFE', 1.0, 7.0, 4.4, 'rural', 'estatal'), 
            Estudiante('SFE', 8.0, 2.0, 4.7, 'rural', 'estatal'),
            Estudiante('SFE', 8.0, 7.0, 6.3, 'rural', 'privado'),
            Estudiante('SFE', 3.0, 7.0, 4.3, 'rural', 'privado'),
            Estudiante('SFE', 8.0, 7.0, 4.3, 'rural', 'privado'),
        ]
        r6 = Resumen(estudiantes6)
        self.assertFalse(Resumen.__eq__(r5, r6))

    def test_repr_redondeo(self):
        estudiantes: list[Estudiante] = [
            Estudiante('SFE', 9.99232, 0.01340202, 10.01912121, 'rural', 'estatal'),
            Estudiante('SFE', 9.99232, 0.01340202, 10.01912121, 'rural', 'privado'),
            Estudiante('SFE', 9.99232, 0.01340202, 10.01912121, 'rural', 'privado'),
            Estudiante('SFE', 9.99232, 0.01340202, 10.01912121, 'rural', 'privado'),
            Estudiante('SFE', 9.99232, 0.01340202, 10.01912121, 'rural', 'privado'),
            Estudiante('SFE', 9.99232, 0.01340202, 10.01912121, 'rural', 'privado'),
            Estudiante('SFE', 9.99232, 0.01340202, 10.01912121, 'rural', 'privado'),
            Estudiante('SFE', 9.99232, 0.01340202, 10.01912121, 'rural', 'privado'),
            Estudiante('SFE', 9.99232, 0.01340202, 10.01912121, 'rural', 'privado'),
            Estudiante('SFE', 9.99232, 0.01340202, 10.01912121, 'urbano', 'privado'),
        ]
        r = Resumen(estudiantes)
        esperado = "<Mat:9.99, Len:0.01, NSE:10.02, Rural:0.90, Estado:0.10, N:10>"
        self.assertEqual(repr(r), esperado)
        
        estudiantes2: list[Estudiante] = [
            Estudiante('SFE', 8.56789, 7.43210, 5.98765, 'rural', 'estatal'),
            Estudiante('SFE', 8.56789, 7.43210, 5.98765, 'urbano', 'estatal'),
            Estudiante('SFE', 8.56789, 7.43210, 5.98765, 'urbano', 'estatal'),
            Estudiante('SFE', 8.56789, 7.43210, 5.98765, 'urbano', 'estatal'),
            Estudiante('SFE', 8.56789, 7.43210, 5.98765, 'urbano', 'privado'),
            Estudiante('SFE', 8.56789, 7.43210, 5.98765, 'urbano', 'estatal'),
            Estudiante('SFE', 8.56789, 7.43210, 5.98765, 'urbano', 'estatal'),
            Estudiante('SFE', 8.56789, 7.43210, 5.98765, 'urbano', 'estatal'),
            Estudiante('SFE', 8.56789, 7.43210, 5.98765, 'urbano', 'privado'),
            Estudiante('SFE', 8.56789, 7.43210, 5.98765, 'urbano', 'estatal'),
        ]
        r2 = Resumen(estudiantes2)
        esperado2 = "<Mat:8.57, Len:7.43, NSE:5.99, Rural:0.10, Estado:0.80, N:10>"
        self.assertEqual(repr(r2), esperado2)
        
        estudiantes3: list[Estudiante] = [
            Estudiante('SFE', 0.00123, 0.00456, 0.00789, 'rural', 'privado'),
            Estudiante('SFE', 0.00123, 0.00456, 0.00789, 'urbano', 'privado'),
            Estudiante('SFE', 0.00123, 0.00456, 0.00789, 'urbano', 'privado'),
            Estudiante('SFE', 0.00123, 0.00456, 0.00789, 'rural', 'estatal'),
            Estudiante('SFE', 0.00123, 0.00456, 0.00789, 'urbano', 'privado'),
            Estudiante('SFE', 0.00123, 0.00456, 0.00789, 'urbano', 'privado'),
            Estudiante('SFE', 0.00123, 0.00456, 0.00789, 'urbano', 'privado'),
            Estudiante('SFE', 0.00123, 0.00456, 0.00789, 'rural', 'privado'),
            Estudiante('SFE', 0.00123, 0.00456, 0.00789, 'urbano', 'privado'),
            Estudiante('SFE', 0.00123, 0.00456, 0.00789, 'urbano', 'estatal'),
        ]
        r3 = Resumen(estudiantes3)
        esperado3 = "<Mat:0.00, Len:0.00, NSE:0.01, Rural:0.30, Estado:0.20, N:10>"
        self.assertEqual(repr(r3), esperado3)

    def test_eq_true_muchos_redondeos(self):
        estudiantes1: list[Estudiante] = [
            Estudiante('SFE', 0.0049, 9.995, 5.0005, 'rural', 'estatal'),
            Estudiante('SFE', 0.0049, 9.995, 5.0005, 'rural', 'estatal'),
            Estudiante('SFE', 0.0049, 9.995, 5.0005, 'rural', 'estatal'),
            Estudiante('SFE', 0.0049, 9.995, 5.0005, 'rural', 'estatal'),
            Estudiante('SFE', 0.0049, 9.995, 5.0005, 'rural', 'estatal'),
            Estudiante('SFE', 0.0049, 9.995, 5.0005, 'rural', 'privado'),
            Estudiante('SFE', 0.0049, 9.995, 5.0005, 'urbano', 'estatal'),
            Estudiante('SFE', 0.0049, 9.995, 5.0005, 'urbano', 'estatal'),
            Estudiante('SFE', 0.0049, 9.995, 5.0005, 'urbano', 'estatal'),
            Estudiante('SFE', 0.0049, 9.995, 5.0005, 'urbano', 'privado'),
        ]
        r1 = Resumen(estudiantes1) 
        estudiantes2: list[Estudiante] = [
            Estudiante('SFE', 0.0051, 9.996, 5.0004, 'rural', 'estatal'),
            Estudiante('SFE', 0.0051, 9.996, 5.0004, 'rural', 'estatal'),
            Estudiante('SFE', 0.0051, 9.996, 5.0004, 'rural', 'estatal'),
            Estudiante('SFE', 0.0051, 9.996, 5.0004, 'rural', 'estatal'),
            Estudiante('SFE', 0.0051, 9.996, 5.0004, 'rural', 'estatal'),
            Estudiante('SFE', 0.0051, 9.996, 5.0004, 'rural', 'privado'),
            Estudiante('SFE', 0.0051, 9.996, 5.0004, 'urbano', 'estatal'),
            Estudiante('SFE', 0.0051, 9.996, 5.0004, 'urbano', 'estatal'),
            Estudiante('SFE', 0.0051, 9.996, 5.0004, 'urbano', 'estatal'),
            Estudiante('SFE', 0.0051, 9.996, 5.0004, 'urbano', 'privado'),
        ]
        r2 = Resumen(estudiantes2)
        self.assertTrue(r1 == r2)
        
        estudiantes3: list[Estudiante] = [
            Estudiante('SFE', 8.0001, 6.0001, 5.00001, 'rural', 'estatal'),
            Estudiante('SFE', 8.0001, 6.0001, 5.00001, 'rural', 'estatal'),
            Estudiante('SFE', 8.0001, 6.0001, 5.00001, 'rural', 'estatal'),
            Estudiante('SFE', 8.0001, 6.0001, 5.00001, 'rural', 'estatal'),
            Estudiante('SFE', 8.0001, 6.0001, 5.00001, 'rural', 'estatal'),
            Estudiante('SFE', 8.0001, 6.0001, 5.00001, 'rural', 'privado'),
            Estudiante('SFE', 8.0001, 6.0001, 5.00001, 'urbano', 'estatal'),
            Estudiante('SFE', 8.0001, 6.0001, 5.00001, 'urbano', 'estatal'),
            Estudiante('SFE', 8.0001, 6.0001, 5.00001, 'urbano', 'estatal'),
            Estudiante('SFE', 8.0001, 6.0001, 5.00001, 'urbano', 'privado'),
        ]
        r3 = Resumen(estudiantes3)
        estudiantes4: list[Estudiante] = [
            Estudiante('SFE', 8.0, 6.0, 5.0, 'rural', 'estatal'),
            Estudiante('SFE', 8.0, 6.0, 5.0, 'rural', 'estatal'),
            Estudiante('SFE', 8.0, 6.0, 5.0, 'rural', 'estatal'),
            Estudiante('SFE', 8.0, 6.0, 5.0, 'rural', 'estatal'),
            Estudiante('SFE', 8.0, 6.0, 5.0, 'rural', 'estatal'),
            Estudiante('SFE', 8.0, 6.0, 5.0, 'rural', 'privado'),
            Estudiante('SFE', 8.0, 6.0, 5.0, 'urbano', 'estatal'),
            Estudiante('SFE', 8.0, 6.0, 5.0, 'urbano', 'estatal'),
            Estudiante('SFE', 8.0, 6.0, 5.0, 'urbano', 'estatal'),
            Estudiante('SFE', 8.0, 6.0, 5.0, 'urbano', 'privado'),
        ]
        r4 = Resumen(estudiantes4)
        self.assertTrue(r3 == r4)
      
        estudiantes5: list[Estudiante] = [
            Estudiante('SFE', 0.00999999, 0.00000099, 0.9999999099, 'rural', 'estatal'),
            Estudiante('SFE', 0.00999999, 0.00000099, 0.9999999099, 'rural', 'estatal'),
            Estudiante('SFE', 0.00999999, 0.00000099, 0.9999999099, 'rural', 'estatal'),
            Estudiante('SFE', 0.00999999, 0.00000099, 0.9999999099, 'rural', 'estatal'),
            Estudiante('SFE', 0.00999999, 0.00000099, 0.9999999099, 'rural', 'estatal'),
            Estudiante('SFE', 0.00999999, 0.00000099, 0.9999999099, 'rural', 'privado'),
            Estudiante('SFE', 0.00999999, 0.00000099, 0.9999999099, 'urbano', 'estatal'),
            Estudiante('SFE', 0.00999999, 0.00000099, 0.9999999099, 'urbano', 'estatal'),
            Estudiante('SFE', 0.00999999, 0.00000099, 0.9999999099, 'urbano', 'estatal'),
            Estudiante('SFE', 0.00999999, 0.00000099, 0.9999999099, 'urbano', 'privado'),
        ]
        r5 = Resumen(estudiantes5)
        estudiantes6: list[Estudiante] = [
            Estudiante('SFE', 0.01, 0.00, 1.00, 'rural', 'estatal'),
            Estudiante('SFE', 0.01, 0.00, 1.00, 'rural', 'estatal'),
            Estudiante('SFE', 0.01, 0.00, 1.00, 'rural', 'estatal'),
            Estudiante('SFE', 0.01, 0.00, 1.00, 'rural', 'estatal'),
            Estudiante('SFE', 0.01, 0.00, 1.00, 'rural', 'estatal'),
            Estudiante('SFE', 0.01, 0.00, 1.00, 'rural', 'privado'),
            Estudiante('SFE', 0.01, 0.00, 1.00, 'urbano', 'estatal'),
            Estudiante('SFE', 0.01, 0.00, 1.00, 'urbano', 'estatal'),
            Estudiante('SFE', 0.01, 0.00, 1.00, 'urbano', 'estatal'),
            Estudiante('SFE', 0.01, 0.00, 1.00, 'urbano', 'privado'),
        ]
        r6 = Resumen(estudiantes6)
        self.assertTrue(r5 == r6)
    
    def resumen_vacio(self):
        estudiantes: list[Estudiante] = [
            Estudiante('', 0, 0, 0, '', ''),
            Estudiante('', 0, 0, 0, '', ''),
            Estudiante('', 0, 0, 0, '', ''),
            Estudiante('', 0, 0, 0, '', ''),
            Estudiante('', 0, 0, 0, '', ''),
            Estudiante('', 0, 0, 0, '', ''),
            Estudiante('', 0, 0, 0, '', ''),
            Estudiante('', 0, 0, 0, '', ''),
            Estudiante('', 0, 0, 0, '', ''),
            Estudiante('', 0, 0, 0, '', ''),
        ]
        r = Resumen(estudiantes)
        esperado = "<Mat:, Len:, NSE:, Rural:, Estado:, N:>"
        self.assertEqual(repr(r), esperado)
        esperado2 = "<Mat:0, Len:0, NSE:0, Rural:0, Estado:0, N:0>"
        self.assertEqual(repr(r), esperado2)


## y asi con el resto de los metodos a testear.
        
####################################################################

unittest.main()