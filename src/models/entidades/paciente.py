from src.models.entidades.medicacion import Medicacion
from src.models.entidades.sintoma import Sintoma

class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.registros = []

    def registrar_sintoma(self, sintoma):
        self.registros.append(sintoma)

    def registrar_medicacion(self, medicacion):
        self.registros.append(medicacion)

    def ver_registros(self):
        for registro in self.registros:
            if isinstance(registro, Sintoma):
                print(f"Síntoma: {registro.descripcion} - Fecha y hora: {registro.fecha_hora}")
            elif isinstance(registro, Medicacion):
                print(f"Medicación: {registro.descripcion} - Dosis: {registro.dosis} - Fecha y hora: {registro.fecha_hora}")
