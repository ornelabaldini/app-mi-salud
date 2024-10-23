from datetime import datetime

class Sintoma:
    def __init__(self, descripcion, fecha_hora=None):
        self.descripcion = descripcion
        self.fecha_hora = fecha_hora if fecha_hora else datetime.now().strftime("%Y-%m-%d %H:%M:%S")