from estudiante import Estudiante

class Resumen:
    def __init__(self, estudiantes: list[Estudiante]):
        '''
        Requiere: 0.0 <= proporcion_ambito_rural <= 1.0. 0.0 <= proporcion_sector_estatal <= 1.0
        Devuelve: nada.
        Modifica: los atributos del objeto con los valores dados.
        '''
        self.cantidad = len(estudiantes)

        total_mate: float = 0
        total_len: float = 0
        total_nse: float = 0
        total_rural: float = 0
        total_estatal: float = 0
        for estudiante in estudiantes:
            total_mate += estudiante.puntaje_matematica
            total_len += estudiante.puntaje_lengua
            total_nse += estudiante.puntaje_nse
            if estudiante.ambito.lower() == 'rural':
                total_rural += 1
            if estudiante.sector.lower() == 'estatal':
                total_estatal += 1

        promedio_matematica: float = total_mate / self.cantidad
        promedio_lengua: float = total_len / self.cantidad
        promedio_nse: float = total_nse / self.cantidad
        proporcion_rural: float = total_rural / self.cantidad
        proporcion_estatal: float = total_estatal / self.cantidad

        self.promedio_matematica = promedio_matematica
        self.promedio_lengua = promedio_lengua
        self.promedio_nse = promedio_nse
        self.proporcion_ambito_rural = proporcion_rural
        self.proporcion_sector_estatal = proporcion_estatal

    def __repr__(self) -> str:
        '''
        Requiere: nada.
        Devuelve: Un string con las caracteristicas del resumen: el promedio en matematica, seguido del promedio de lengua, seguido de promedio en NSE (todos los promedios con 2 decimales maximo), luego la proporción de estudiantes que van a una escuela del sector estatal, proporción de estudiantes que van a una escuela en el ámbito rural y la cantidad de estudiantes considerada en el resumen.
        Modifica: nada.
        '''
        return (f"<Mat:{self.promedio_matematica:.2f}, " f"Len:{self.promedio_lengua:.2f}, " f"NSE:{self.promedio_nse:.2f}, " f"Rural:{self.proporcion_ambito_rural:.2f}, " f"Estado:{self.proporcion_sector_estatal:.2f}, " f"N:{self.cantidad}>")

    def __eq__(self, other) -> bool:
        '''
        Requiere: nada.
        Devuelve: True si los dos resumenes son iguales, teniendo en cuenta una tolerancia de 0.001 en sus promedios y proporciones, False en caso contrario.
        Modifica: nada.
        '''
        tolerancia: float = 0.001

        return (self.cantidad == other.cantidad and abs(self.promedio_matematica - other.promedio_matematica) < tolerancia and abs(self.promedio_lengua - other.promedio_lengua) < tolerancia and abs(self.promedio_nse - other.promedio_nse) < tolerancia and abs(self.proporcion_ambito_rural - other.proporcion_ambito_rural) < tolerancia and abs(self.proporcion_sector_estatal - other.proporcion_sector_estatal) < tolerancia)