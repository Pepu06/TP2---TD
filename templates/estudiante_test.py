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

        e2 = Estudiante('SFE', 344.212323, 452.12, 1.233, "rural", 'privado')
        self.assertEqual(e2.provincia, "SFE")
        self.assertEqual(e2.puntaje_matematica, 344.212323)
        self.assertEqual(e2.puntaje_lengua, 452.12)
        self.assertEqual(e2.puntaje_nse, 01.233)
        self.assertEqual(e2.ambito, "rural")
        self.assertEqual(e2.sector, "privado")
    
    def test_repr_estudiante(self):
        e = Estudiante("CHU", 100.11, 200.22, 300.33, "urbano", "estatal")
        esperado = "<Mat:100.11, Len:200.22, NSE:300.33, urbano, estatal, CHU>"
        self.assertEqual(repr(e), esperado)

        e2 = Estudiante('SFE', 344.212323, 452.12, 1.233, "urbano", 'privado')
        esperado2 = "<Mat:344.21, Len:452.12, NSE:1.23, urbano, privado, SFE>"
        self.assertEqual(repr(e2), esperado2)
        
        e3 = Estudiante('CHA', 221.35642, 145.3233, 0.1243, "rural", 'estatal')
        esperado3 = "<Mat:221.36, Len:145.32, NSE:0.12, rural, estatal, CHA>"
        self.assertEqual(repr(e3), esperado3)

    def test_estudiantes_iguales(self):
        e1 = Estudiante("CHU", 500.0, 400.0, 1.0, "urbano", "privado")
        e2 = Estudiante("CHU", 500.0, 400.0, 1.0, "urbano", "privado")
        self.assertEqual(e1, e2)

        e3 = Estudiante("SFE", 321.0, 250.0, 0.5, "rural", "estatal")
        e4 = Estudiante("SFE", 321.0, 250.0, 0.5, "rural", "estatal")
        self.assertEqual(e3, e4)

        e5 = Estudiante("TUC", 600.0, 500.0, 1.5, "urbano", "privado")
        e6 = Estudiante("TUC", 600.0, 500.0, 1.5, "urbano", "privado")
        self.assertEqual(e5, e6)
    
    def test_estudiantes_iguales_tolerancia(self):
        e1 = Estudiante("CHU", 500.00001, 400.00003, 1.00099, "urbano", "privado")
        e2 = Estudiante("CHU", 500.0, 400.0, 1.0, "urbano", "privado")
        self.assertEqual(e1, e2)

        e3 = Estudiante("SFE", 321.0001, 250.0002, 0.5003, "rural", "estatal")
        e4 = Estudiante("SFE", 321.0, 250.0, 0.5, "rural", "estatal")
        self.assertEqual(e3, e4)

        e5 = Estudiante("TUC", 600.0005, 500.0006, 1.5007, "urbano", "privado")
        e6 = Estudiante("TUC", 600.0, 500.0, 1.5, "urbano", "privado")
        self.assertEqual(e5, e6)

    def test_estudiantes_distinto_puntaje(self):
        e1 = Estudiante("CHU", 500.0, 400.0, 1.0, "urbano", "privado")
        e2 = Estudiante("CHU", 500.1, 400.0, 1.0, "urbano", "privado")
        self.assertNotEqual(e1, e2)

        e3 = Estudiante("SFE", 321.0, 250.0, 0.5, "rural", "estatal")
        e4 = Estudiante("SFE", 321.0, 250.1, 0.5, "rural", "estatal")
        self.assertNotEqual(e3, e4)

        e5 = Estudiante("TUC", 600.0, 500.0, 1.5, "urbano", "privado")
        e6 = Estudiante("TUC", 600.0, 500.1, 1.5, "urbano", "privado")
        self.assertNotEqual(e5, e6)

    def test_estudiantes_distinta_provincia(self):
        e1 = Estudiante("CHU", 500.0, 400.0, 1.0, "urbano", "privado")
        e2 = Estudiante("SFE", 500.0, 400.0, 1.0, "urbano", "privado")
        self.assertNotEqual(e1, e2)

        e3 = Estudiante("SFE", 321.0, 250.0, 0.5, "rural", "estatal")
        e4 = Estudiante("TUC", 321.0, 250.0, 0.5, "rural", "estatal")
        self.assertNotEqual(e3, e4)

        e5 = Estudiante("CHA", 600.0, 500.0, 1.5, "urbano", "privado")
        e6 = Estudiante("CHU", 600.0, 500.0, 1.5, "urbano", "privado")
        self.assertNotEqual(e5, e6)

    def test_estudiantes_distinto_ambito(self):
        e1 = Estudiante("CHU", 500.0, 400.0, 1.0, "rural", "privado")
        e2 = Estudiante("CHU", 500.0, 400.0, 1.0, "urbano", "privado")
        self.assertNotEqual(e1, e2)

        e3 = Estudiante("SFE", 321.0, 250.0, 0.5, "urbano", "estatal")
        e4 = Estudiante("SFE", 321.0, 250.0, 0.5, "rural", "estatal")
        self.assertNotEqual(e3, e4)

    def test_estudiantes_distinto_sector(self):
        e1 = Estudiante("CHU", 500.0, 400.0, 1.0, "urbano", "estatal")
        e2 = Estudiante("CHU", 500.0, 400.0, 1.0, "urbano", "privado")
        self.assertNotEqual(e1, e2)

        e3 = Estudiante("SFE", 321.0, 250.0, 0.5, "rural", "privado")
        e4 = Estudiante("SFE", 321.0, 250.0, 0.5, "rural", "estatal")
        self.assertNotEqual(e3, e4)

    def estudiante_vacio(self):
        e = Estudiante('', 0, 0, 0, '', '')
        esperado = "<Mat:, Len:, NSE:, , , >"
        self.assertEqual(repr(e), esperado)
        e2 = Estudiante('', 0, 0, 0, '', '')
        esperado2 = "<Mat:0, Len:0, NSE:0, , , >"
        self.assertEqual(repr(e2), esperado2)

        
####################################################################

unittest.main()