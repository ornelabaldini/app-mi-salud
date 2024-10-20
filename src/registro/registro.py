from datetime import datetime

class Registro:
    def __init__(self, descripcion, fecha_hora=None):
        self.descripcion = descripcion
        if fecha_hora is None:
            self.fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M")
        else:
            self.fecha_hora = fecha_hora.strftime("%Y-%m-%d %H:%M")

    def __str__(self):
        return f"Registro: {self.descripcion} - Fecha y hora: {self.fecha_hora}"