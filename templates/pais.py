from resumen import Resumen
from estudiante import Estudiante
import csv

class Pais:
    def __init__(self, archivo_csv:str):
        '''
        Requiere: nada.
        Devuelve: nada.
        Modifica: se le crea un atributo al objeto con todos los estudiantes dentro del archivo_csv.
        '''
        self.estudiantes: list[Estudiante] = []
        archivo = open(archivo_csv)
        filas = csv.DictReader(archivo)
        for fila in filas:
            estudiante: Estudiante = Estudiante(
                provincia = fila['provincia'],
                puntaje_matematica = float(fila['mpuntaje']),
                puntaje_lengua = float(fila['lpuntaje']),
                puntaje_nse = float(fila['NSE_puntaje']),
                ambito = fila['ambito'],
                sector = fila['sector']
            )
            self.estudiantes.append(estudiante)

        provincias: set[str] = set()
        for estudiante in self.estudiantes:
            provincias.add(estudiante.provincia)

        self.provincias = len(provincias)

   
    def tamano(self) -> int:
        '''
        Requiere: nada.
        Devuelve: la cantidad de estudiantes que hay en el objeto.
        Modifica: nada.
        '''
        return (len(self.estudiantes))

    def resumen_provincia(self, provincia: str) -> Resumen:
        '''
        Requiere: que provincia sea la provincia de algun estudiante dentro del objeto.
        Devuelve: un objeto de la clase Resumen, con todos los datos de la provincia dada.
        Modifica: nada.
        '''
        filtrados: list[Estudiante] = []
        for estudiante in self.estudiantes:
            if estudiante.provincia == provincia:
                filtrados.append(estudiante)

        cantidad: int = len(filtrados)

        total_mate: float = 0
        total_len: float = 0
        total_nse: float = 0
        total_rural: float = 0
        total_estatal: float = 0
        for estudiante in filtrados:
            total_mate += estudiante.puntaje_matematica
            total_len += estudiante.puntaje_lengua
            total_nse += estudiante.puntaje_nse
            if estudiante.ambito == 'Rural':
                total_rural += 1
            if estudiante.sector == 'Estatal':
                total_estatal += 1

        promedio_matematica: float = total_mate / cantidad
        promedio_lengua: float = total_len / cantidad
        promedio_nse: float = total_nse / cantidad
        proporcion_rural: float = total_rural / cantidad
        proporcion_estatal: float = total_estatal / cantidad

        return Resumen(cantidad, promedio_matematica, promedio_lengua, promedio_nse, proporcion_rural, proporcion_estatal)
    
    def resumenes_pais(self) -> dict[str, Resumen]:
        '''
        Requiere: nada.
        Devuelve: un diccionario con los paises dentro del objeto como clave, y sus resumenes como valor.
        Modifica: nada.
        '''
        provincias: set[str] = set()
        resumenes: dict[str, Resumen] = dict()
        for estudiante in self.estudiantes:
            provincias.add(estudiante.provincia)
        
        for provincia in provincias:
            resumenes[provincia] = self.resumen_provincia(provincia)

        return resumenes
    
    def estudiantes_en_intervalo(self, categoria: str, x: int, y: int, provincias: set[str]) -> int:
        '''
        Requiere: que categoria tome el valor 'mat', 'len' o 'nse'. x < y. provincia sea la provincia de algun estudiante en el objeto.
        Devuelve: la cantidad de estudiantes dentro del objeto que tienen puntaje de la materia indicada en categoria, mayor o igual que x y menor que y.
        Modifica: nada.
        '''
        vr: int = 0

        for provincia in provincias:
            for estudiante in self.estudiantes:
                if estudiante.provincia == provincia:
                    valores: dict[str, float] = {
                        'mat': estudiante.puntaje_matematica,
                        'len': estudiante.puntaje_lengua,
                        'nse': estudiante.puntaje_nse
                    }
                    valor: float = valores[categoria]
                    if x <= valor < y:
                        vr += 1

        return vr

   
    def exportar_por_provincias(self, archivo_csv: str, provincias: list[str]):
        '''
        Requiere: archivo_csv termine con '.csv'. provincia sea la provincia de algun estudiante en el objeto.
        Devuelve: nada.
        Modifica: crea un nuevo archivo con el nombre de archivo_csv, con len(provincias) filas. Donde en cada una indica la provincia, la cantidad de estudiantes de la misma, el promedio de puntaje en matematica, el promedio de puntaje en lengua, el promedio de puntaje en nse, la proporción de estudiantes que van a una escuela en el ámbito rural y la proporción de estudiantes que van a una escuela del sector estatal.
        '''
        encabezados: list[str] = ['provincia', 'cantidad', 'promedio_matematica', 'promedio_lengua', 'promedio_nse', 'proporcion_ambito_rural', 'proporcion_sector_estatal']
        archivo = open(archivo_csv, 'w')
        filas = csv.DictWriter(archivo, fieldnames=encabezados)
        filas.writeheader()
        for provincia in provincias:
            resumen: Resumen = self.resumen_provincia(provincia)
            filas.writerow({
                'provincia': provincia,
                'cantidad': resumen.cantidad,
                'promedio_matematica': resumen.promedio_matematica,
                'promedio_lengua': resumen.promedio_lengua,
                'promedio_nse': resumen.promedio_nse,
                'proporcion_ambito_rural': resumen.proporcion_ambito_rural,
                'proporcion_sector_estatal': resumen.proporcion_sector_estatal,
            })




p = Pais('./filtrado_CHA_SFE.csv')

print(p.tamano())
print(p.provincias)
print(p.resumen_provincia('SFE'))
print(p.resumenes_pais())
resultado = p.estudiantes_en_intervalo('mat', 600, 601, {'MZA', 'SFE'})
print("Cantidad de estudiantes con matemática entre 600 y 601:", resultado)
p.exportar_por_provincias('hola.csv', ['SFE', 'CHA'])