class Estudiante:
    def __init__(self, provincia: str, puntaje_matematica: str, puntaje_lengua: str, puntaje_nse: str, ambito: str, sector: str):
        '''
        Requiere: ambito sea 'rural' o 'urbano'. sector sea 'estatal' o 'privado'.
        Devuelve: nada.
        Modifica: los atributos del objeto con los valores dados.
        '''
        self.provincia: str = provincia
        self.puntaje_matematica: float = puntaje_matematica
        self.puntaje_lengua: float = puntaje_lengua
        self.puntaje_nse: float = puntaje_nse
        self.ambito: str = ambito
        self.sector: str = sector

    def __repr__(self) -> str:
        '''
        Requiere: nada.
        Devuelve: Un string con las caracteristicas del estudiante: su puntaje en matematica, seguido del puntaje de lengua, seguido de su puntaje de NSE (todos los puntajes con 2 decimales maximo), luego el ambito de la escuela, el sector y provincia de la misma.
        Modifica: nada.
        '''
        return (f"<Mat:{self.puntaje_matematica:.2f}, " f"Len:{self.puntaje_lengua:.2f}, " f"NSE:{self.puntaje_nse:.2f}, " f"{self.ambito}, {self.sector}, {self.provincia}>")
    
    def __eq__(self, other) -> bool:
        '''
        Requiere: nada.
        Devuelve: True si los dos estudiantes son iguales, teniendo en cuenta una tolerancia de 0.001 en sus puntajes, False en caso contrario.
        Modifica: nada.
        '''
        vr: bool = False
        tolerancia: float = 0.001
        if self.provincia == other.provincia and self.ambito == other.ambito and self.sector == other.sector and abs(self.puntaje_matematica - other.puntaje_matematica) < tolerancia and abs(self.puntaje_lengua - other.puntaje_lengua) < tolerancia and abs(self.puntaje_nse - other.puntaje_nse) < tolerancia:
            vr = True
        return vr