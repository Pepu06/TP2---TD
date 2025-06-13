import unittest

# Importamos el codigo a testear.
from estudiante import Estudiante

####################################################################

class TestEstudiante(unittest.TestCase):

    def test_creacion_estudiante(self):
        e = Estudiante("CHU", 390.5, 370.75, 0.85, "rural", "estatal")
        self.assertEqual(e.provincia, "CHU")
        self.assertEqual(e.puntaje_matematica, 390.5)
        self.assertEqual(e.puntaje_lengua, 370.75)
        self.assertEqual(e.puntaje_nse, 0.85)
        self.assertEqual(e.ambito, "rural")
        self.assertEqual(e.sector, "estatal")
    
    def test_repr_estudiante(self):
        e = Estudiante("CHU", 100.11, 200.22, 300.33, "urbano", "estatal")
        esperado = "<Mat:100.11, Len:200.22, NSE:300.33, urbano, estatal, CHU>"
        self.assertEqual(repr(e), esperado)

    def test_estudiantes_iguales(self):
        e1 = Estudiante("CHU", 500.0, 400.0, 1.0, "urbano", "privado")
        e2 = Estudiante("CHU", 500.0, 400.0, 1.0, "urbano", "privado")
        self.assertEqual(e1, e2)
    
    def test_estudiantes_iguales_tolerancia(self):
        e1 = Estudiante("CHU", 500.00001, 400.00003, 1.00099, "urbano", "privado")
        e2 = Estudiante("CHU", 500.0, 400.0, 1.0, "urbano", "privado")
        self.assertEqual(e1, e2)

    def test_estudiantes_distinto_puntaje(self):
        e1 = Estudiante("CHU", 500.0, 400.0, 1.0, "urbano", "privado")
        e2 = Estudiante("CHU", 500.1, 400.0, 1.0, "urbano", "privado")
        self.assertNotEqual(e1, e2)

    def test_estudiantes_distinta_provincia(self):
        e1 = Estudiante("CHU", 500.0, 400.0, 1.0, "urbano", "privado")
        e2 = Estudiante("SFE", 500.0, 400.0, 1.0, "urbano", "privado")
        self.assertNotEqual(e1, e2)

    def test_estudiantes_distinto_ambito(self):
        e1 = Estudiante("CHU", 500.0, 400.0, 1.0, "rural", "privado")
        e2 = Estudiante("CHU", 500.0, 400.0, 1.0, "urbano", "privado")
        self.assertNotEqual(e1, e2)

    def test_estudiantes_distinto_sector(self):
        e1 = Estudiante("CHU", 500.0, 400.0, 1.0, "urbano", "estatal")
        e2 = Estudiante("CHU", 500.0, 400.0, 1.0, "urbano", "privado")
        self.assertNotEqual(e1, e2)

    def estudiante_vacio(self):
        e = Estudiante('', 0, 0, 0, '', '')
        esperado = "<Mat:, Len:, NSE:, , , >"
        self.assertEqual(repr(e), esperado)
        e2 = Estudiante('', 0, 0, 0, '', '')
        esperado2 = "<Mat:0, Len:0, NSE:0, , , >"
        self.assertEqual(repr(e2), esperado2)

        
####################################################################

unittest.main()