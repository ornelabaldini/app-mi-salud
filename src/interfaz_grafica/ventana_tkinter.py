import tkinter as tk
from src.paciente import Paciente
from src.registro import registro
from src.utils import fecha_hora

class Ventana((tk.Tk)):
    def __init__(self):
        super().__init__()
        self.title("Registro de Pacientes")
        self.geometry("400x300")

        # Crear widgets
        self.etiqueta_nombre = tk.Label(self, text="Nombre del paciente:")
        self.etiqueta_nombre.pack()

        self.entrada_nombre = tk.Entry(self)
        self.entrada_nombre.pack()

        self.etiqueta_descripcion = tk.Label(self, text="Descripción del síntoma:")
        self.etiqueta_descripcion.pack()

        self.entrada_descripcion = tk.Entry(self)
        self.entrada_descripcion.pack()

        self.etiqueta_fecha = tk.Label(self, text="Fecha y hora del síntoma (YYYY-MM-DD HH:MM):")
        self.etiqueta_fecha.pack()

        self.entrada_fecha = tk.Entry(self)
        self.entrada_fecha.pack()

        self.boton_registrar = tk.Button(self, text="Registrar síntoma", command=self.registrar_sintoma)
        self.boton_registrar.pack()

        self.texto_resultado = tk.Text(self)
        self.texto_resultado.pack()

    def registrar_sintoma(self):
        # Código para registrar síntoma
        pass
