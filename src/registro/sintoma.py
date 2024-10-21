from .registro import Registro

class Sintoma(Registro):
    def __init__(self, descripcion, fecha_hora=None):
        super().__init__(descripcion, fecha_hora)

    def __str__(self):
        return f"-Síntoma: {self.descripcion}\n  Fecha y hora de síntoma: {self.fecha_hora}"
