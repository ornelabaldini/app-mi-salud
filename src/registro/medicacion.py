from .registro import Registro

class Medicacion(Registro):
    def __init__(self, descripcion, dosis, fecha_hora):
        super().__init__(descripcion, fecha_hora)  # Llama al constructor de Registro
        self.dosis = dosis

    def _str_(self):
        return f"Medicación: {self.descripcion} - Dosis: {self.dosis} - Fecha y hora: {self.fecha_hora}"