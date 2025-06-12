import unittest

# Importamos el codigo a testear.
from pais import Pais

####################################################################
p = Pais('Aprender2023_curado.csv')

class TestPais(unittest.TestCase):

    def test_tamano(self):
        self.assertEqual(p.tamano(), 583967)
   
    def test_provincias(self):
        self.assertEqual(p.provincias, 24)
        
    def test_resultado(self):
        res = (p.estudiantes_en_intervalo('mat', 600, 601,  {'SFE', 'CHA', 'MZA'}))
        esperado = (137)
        self.assertEqual(res,esperado)
  
    def test_intervalo_provincias_vacio(self):
        res = (p.estudiantes_en_intervalo('mat', 400, 500, set()))
        esperado = (0)
        self.assertEqual(res, esperado)

    def test_resumen_provincia(self):
        res = p.resumen_provincia('CHU')
        self.assertEqual(res.promedio_matematica, 476.9460445429056)
        self.assertEqual(res.promedio_lengua, 505.8221022368013)
        self.assertEqual(res.promedio_nse,  0.3330461067653736)
        self.assertEqual(res.proporcion_ambito_rural, 0.11235623709820113)
        self.assertEqual(res.proporcion_sector_estatal,  0.8118549100560307)
        self.assertEqual(res.cantidad, 6782)
    
    


            
####################################################################

unittest.main()
