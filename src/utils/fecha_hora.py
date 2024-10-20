from datetime import datetime

class FechaHora:
    def __init__(self, fecha_hora):
        try:
            self.fecha_hora = datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M")
        except ValueError:
            raise ValueError("La fecha y hora deben estar en el formato YYYY-MM-DD HH:MM")

    def __str__(self):
        return self.fecha_hora.strftime("%Y-%m-%d ")