from datetime import datetime

class Registro:
    def __init__(self, descripcion, fecha_hora=None):
        self.descripcion = descripcion
        self.fecha_hora = fecha_hora if fecha_hora else datetime.now()

    def __str__(self):
        return f"Registro: {self.descripcion} - Fecha y hora: {self.fecha_hora}"
