from .registro import Registro

class Medicacion(Registro):
    def _init_(self, descripcion, dosis, fecha_hora=None):
        super()._init_(descripcion, fecha_hora)
        self.dosis = dosis

    def _str_(self):
        return f"Medicación: {self.descripcion} - Dosis: {self.dosis} - Fecha y hora: {self.fecha_hora}"