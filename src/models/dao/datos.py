from datetime import datetime

class FechaHora:
    def obtener_fecha_hora(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M")
