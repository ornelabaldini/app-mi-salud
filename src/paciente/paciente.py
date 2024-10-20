from src.registro.sintoma import Sintoma
from src.registro.medicacion import Medicacion

class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.registros = []

    def registrar_sintoma(self, descripcion):
        sintoma = Sintoma(descripcion)
        self.registros.append(sintoma)


    def registrar_medicacion(self, medicacion):
        self.registros.append(medicacion)


    def ver_registros(self):
        for registro in self.registros:
            if isinstance(registro, Sintoma):
                print(f"{registro.descripcion}\nFecha y hora de sintoma : {registro.fecha_hora}\n")
            elif isinstance(registro, Medicacion):
                print(
                    f"Medicación: {registro.descripcion}\nDosis: {registro.dosis}\nFecha y hora: {registro.fecha_hora}\n")
