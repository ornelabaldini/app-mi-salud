from datetime import datetime

class Medicacion:
    def __init__(self, descripcion, dosis, fecha_hora=None):
        self.descripcion = descripcion
        self.dosis = dosis
        self.fecha_hora = fecha_hora if fecha_hora else datetime.now().strftime("%Y-%m-%d %H:%M:%S")