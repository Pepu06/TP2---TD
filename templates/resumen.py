class Resumen:
    def __init__(self, cantidad: int, promedio_matematica: float, promedio_lengua: float, promedio_nse: float, proporcion_ambito_rural: float, proporcion_sector_estatal: float):
        '''
        Requiere: 0.0 <= proporcion_ambito_rural <= 1.0. 0.0 <= proporcion_sector_estatal <= 1.0
        Devuelve: nada.
        Modifica: los atributos del objeto con los valores dados.
        '''
        self.cantidad = cantidad
        self.promedio_matematica = promedio_matematica
        self.promedio_lengua = promedio_lengua
        self.promedio_nse = promedio_nse
        self.proporcion_ambito_rural = proporcion_ambito_rural
        self.proporcion_sector_estatal = proporcion_sector_estatal

    def __repr__(self) -> str:
        '''
        Requiere: nada.
        Devuelve: Un string con las caracteristicas del resumen: el promedio en matematica, seguido del promedio de lengua, seguido de promedio en NSE (todos los promedios con 2 decimales maximo), luego la proporción de estudiantes que van a una escuela del sector estatal, proporción de estudiantes que van a una escuela en el ámbito rural y la cantidad de estudiantes considerada en el resumen.
        Modifica: nada.
        '''
        return (f"<Mat:{round(self.promedio_matematica, 2)}, " f"Len:{round(self.promedio_lengua, 2)}, " f"NSE:{round(self.promedio_nse, 2)}, " f"Rural:{round(self.proporcion_ambito_rural, 2)}, " f"Estado:{round(self.proporcion_sector_estatal, 2)}, " f"N:{self.cantidad}")

    def __eq__(self, other) -> bool:
        '''
        Requiere: nada.
        Devuelve: True si los dos resumenes son iguales, teniendo en cuenta una tolerancia de 0.001 en sus promedios y proporciones, False en caso contrario.
        Modifica: nada.
        '''
        tolerancia: float = 0.001
        return (self.cantidad == other.cantidad and abs(self.promedio_matematica - other.promedio_matematica) < tolerancia and abs(self.promedio_lengua - other.promedio_lengua) < tolerancia and abs(self.promedio_nse - other.promedio_nse) < tolerancia and abs(self.proporcion_ambito_rural - other.proporcion_ambito_rural) < tolerancia and abs(self.proporcion_sector_estatal - other.proporcion_sector_estatal) < tolerancia)
