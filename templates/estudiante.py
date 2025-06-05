import csv

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
    
    def __eq__(self, e2: "Estudiante") -> bool:
        '''
        Requiere: nada.
        Devuelve: True si los dos estudiantes son iguales, teniendo en cuenta una tolerancia de 0.001 en sus puntajes, False en caso contrario.
        Modifica: nada.
        '''
        vr: bool = False
        tolerancia: float = 0.001
        if self.provincia == e2.provincia and self.ambito == e2.ambito and self.sector == e2.sector and abs(self.puntaje_matematica - e2.puntaje_matematica) < tolerancia and abs(self.puntaje_lengua - e2.puntaje_lengua) < tolerancia and abs(self.puntaje_nse - e2.puntaje_nse) < tolerancia:
            vr = True
        return vr


estudiantes = []

with open('./datos_chico.csv') as f:
    reader = csv.DictReader(f)
    for fila in reader:
        estudiante = Estudiante(
            provincia=fila['provincia'],
            puntaje_matematica=float(fila['mpuntaje']),
            puntaje_lengua=float(fila['lpuntaje']),
            puntaje_nse=float(fila['NSE_puntaje']),
            ambito=fila['ambito'],
            sector=fila['sector']
        )
        estudiantes.append(estudiante)

for i in range(len(estudiantes)):
    for j in range(i + 1, len(estudiantes)):
        if estudiantes[i] == estudiantes[j]:
            print(f'Estudiante {i+1} y Estudiante {j+1} son iguales')
            print(estudiantes[i])
            print(estudiantes[j])
        else:
            pass