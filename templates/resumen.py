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
        return (f"<Mat:{self.promedio_matematica:.2f}, " f"Len:{self.promedio_lengua:.2f}, " f"NSE:{self.promedio_nse:.2f}, " f"Rural:{self.proporcion_ambito_rural:.2f}, " f"Estado:{self.proporcion_sector_estatal:.2f}, " f"N:{self.cantidad}")

    def __eq__(self, r2: "Resumen") -> ...:
        '''
        Requiere: nada.
        Devuelve: True si los dos resumenes son iguales, teniendo en cuenta una tolerancia de 0.001 en sus promedios y proporciones, False en caso contrario.
        Modifica: nada.
        '''
        vr: bool = False
        tolerancia: float = 0.001
        if self.cantidad == r2.cantidad and abs(self.promedio_matematica - r2.promedio_matematica) < tolerancia and abs(self.promedio_lengua - r2.promedio_lengua) < tolerancia and abs(self.promedio_nse - r2.promedio_nse) < tolerancia and abs(self.proporcion_ambito_rural - r2.proporcion_ambito_rural) < tolerancia and abs(self.proporcion_sector_estatal - r2.proporcion_sector_estatal) < tolerancia:
            vr = True
        return vr

