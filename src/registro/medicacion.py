from .registro import Registro
from datetime import datetime

class Medicacion(Registro):
    def __init__(self, descripcion, fecha_hora, dosis = None):
        super().__init__(descripcion, fecha_hora)
        self.dosis = dosis

    def _str_(self):
        return f"Medicación: {self.descripcion} - Dosis: {self.dosis} - Fecha y hora de medicación: {self.fecha_hora}"