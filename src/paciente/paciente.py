from src.registro.registro import Registro
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

    def registrar_medicacion(self, descripcion, dosis):
        medicacion = Medicacion(descripcion, dosis)
        self.registros.append(medicacion)

    def ver_registros(self):
        print(f"Registros del paciente {self.nombre}:")
        for registro in self.registros:
            print(registro)