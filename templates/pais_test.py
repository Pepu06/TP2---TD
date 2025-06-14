import unittest

# Importamos el codigo a testear.
from pais import Pais
import csv

####################################################################
p = Pais('datos.csv')
p_vacio = Pais('datos_vacio.csv')


class TestPais(unittest.TestCase):

    def test_inicializacion(self):
        self.assertEqual(p.provincias, 5)
        self.assertEqual(len(p.estudiantes), 12)
        self.assertEqual(p_vacio.provincias, 0)
        self.assertEqual(len(p_vacio.estudiantes), 0)

    def test_tamano(self):
        self.assertEqual(p.tamano(), 12)
        self.assertEqual(p_vacio.tamano(), 0)

        p.estudiantes.append(p.estudiantes[0])
        self.assertEqual(p.tamano(), 13)


    def test_resumen_provincia(self):
        r = p.resumen_provincia('SFE')
        esperado = '<Mat:458.5, Len:507.46, NSE:0.09, Rural:0.0, Estado:1.0, N:3>'
        self.assertEqual(repr(r), esperado)

        r2 = p.resumen_provincia('ETR')
        self.assertEqual(r2.cantidad, 1)
        self.assertEqual(r2.promedio_matematica, 405.51733)
        self.assertEqual(r2.promedio_lengua, 473.92374)
        self.assertEqual(r2.promedio_nse, 1.0763631)
        self.assertEqual(r2.proporcion_ambito_rural, 0.0)
        self.assertEqual(r2.proporcion_sector_estatal, 0.0)

    def test_resumen_pais(self):
        rp = p.resumenes_pais()
        self.assertIn('SFE', rp)
        self.assertEqual(len(rp), 5)
        self.assertEqual(repr(rp['ETR']), '<Mat:405.52, Len:473.92, NSE:1.08, Rural:0.0, Estado:0.0, N:1>')
        self.assertEqual(repr(rp['MZA']), '<Mat:454.02, Len:489.1, NSE:0.29, Rural:0.0, Estado:1.0, N:4>')
        self.assertEqual(repr(rp['SFE']), '<Mat:458.5, Len:507.46, NSE:0.09, Rural:0.0, Estado:1.0, N:3>')
        self.assertEqual(repr(rp['SDE']), '<Mat:636.44, Len:728.6, NSE:-1.65, Rural:1.0, Estado:1.0, N:2>')
        self.assertEqual(repr(rp['TUC']), '<Mat:341.45, Len:447.09, NSE:-0.52, Rural:1.0, Estado:1.0, N:2>')

    def test_resumen_pais_vacio(self):
        rp_vacio = p_vacio.resumenes_pais()
        self.assertEqual(len(rp_vacio), 0)
        self.assertNotIn('SFE', rp_vacio)
        self.assertNotIn('ETR', rp_vacio)

    def test_estudiantes_en_intervalo(self):
        res = p.estudiantes_en_intervalo('mat', 400, 500, {'SFE'})
        self.assertEqual(res, 2)

        res2 = p.estudiantes_en_intervalo('len', 480, 500, {'MZA'})
        self.assertEqual(res2, 0)

        res3 = p.estudiantes_en_intervalo('nse', -1, 0, {'TUC'})
        self.assertEqual(res3, 2)

    def test_exportar_por_provincias(self):
        archivo = 'archivo_test.csv'
        provincias = ['SFE', 'TUC']
        p.exportar_por_provincias(archivo, provincias)
        
        lectura = open(archivo)
        lineas = list(csv.DictReader(lectura))

        self.assertEqual(len(lineas), 2)
        self.assertEqual(lineas[0]['provincia'], 'SFE')
        self.assertEqual(lineas[1]['provincia'], 'TUC')
        self.assertEqual(lineas[0]['cantidad'], '3')
        self.assertEqual(lineas[1]['cantidad'], '2')
        self.assertEqual(float(lineas[0]['promedio_matematica']), 458.4992066666667)
        self.assertEqual(float(lineas[1]['promedio_matematica']), 341.45064)
        self.assertEqual(float(lineas[0]['promedio_lengua']), 507.45515)
        self.assertEqual(float(lineas[1]['promedio_lengua']), 447.090345)
        self.assertEqual(float(lineas[0]['promedio_nse']), 0.08912636933333333)
        self.assertEqual(float(lineas[1]['promedio_nse']), -0.5184160480000001)
        self.assertEqual(float(lineas[0]['proporcion_ambito_rural']), 0.0)
        self.assertEqual(float(lineas[1]['proporcion_ambito_rural']), 1.0)
        self.assertEqual(float(lineas[0]['proporcion_sector_estatal']), 1.0)
        self.assertEqual(float(lineas[1]['proporcion_sector_estatal']), 1.0)

        archivo2 = 'archivo_test2.csv'
        provincias2 = ['ETR', 'SDE']
        p.exportar_por_provincias(archivo2, provincias2)
        lectura2 = open(archivo2)
        lineas2 = list(csv.DictReader(lectura2))
        self.assertEqual(len(lineas2), 2)
        self.assertEqual(lineas2[0]['provincia'], 'ETR')
        self.assertEqual(lineas2[1]['provincia'], 'SDE')
        self.assertEqual(lineas2[0]['cantidad'], '1')
        self.assertEqual(lineas2[1]['cantidad'], '2')
        self.assertEqual(float(lineas2[0]['promedio_matematica']), 405.51733)
        self.assertEqual(float(lineas2[1]['promedio_matematica']), 636.436765)
        self.assertEqual(float(lineas2[0]['promedio_lengua']), 473.92374)
        self.assertEqual(float(lineas2[1]['promedio_lengua']), 728.5989099999999)
        self.assertEqual(float(lineas2[0]['promedio_nse']), 1.0763631)
        self.assertEqual(float(lineas2[1]['promedio_nse']), -1.648647945)
        self.assertEqual(float(lineas2[0]['proporcion_ambito_rural']), 0.0)
        self.assertEqual(float(lineas2[1]['proporcion_ambito_rural']), 1.0)
        self.assertEqual(float(lineas2[0]['proporcion_sector_estatal']), 0.0)
        self.assertEqual(float(lineas2[1]['proporcion_sector_estatal']), 1.0)


    
    


            
####################################################################

unittest.main()
