import tkinter as tk
from tkinter import messagebox
from paciente import Paciente
from registro.registro import Registro
from registro.sintoma import Sintoma
from registro.medicacion import Medicacion
from utils.fecha_hora import FechaHora

class Aplicacion(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("Registro de Pacientes")
            self.geometry("400x300")

            self.pacientes = {}

            self.etiqueta_titulo = tk.Label(self, text="Registro de Pacientes")
            self.etiqueta_titulo.pack()

            self.etiqueta_nombre_paciente = tk.Label(self, text="Nombre del paciente:")
            self.etiqueta_nombre_paciente.pack()

            self.entrada_nombre_paciente = tk.Entry(self)
            self.entrada_nombre_paciente.pack()

            self.etiqueta_edad_paciente = tk.Label(self, text="Edad del paciente:")
            self.etiqueta_edad_paciente.pack()

            self.entrada_edad_paciente = tk.Entry(self)
            self.entrada_edad_paciente.pack()

            self.boton_ingresar_paciente = tk.Button(self, text="Ingresar paciente", command=self.ingresar_paciente)
            self.boton_ingresar_paciente.pack()

            self.etiqueta_descripcion_sintoma = tk.Label(self, text="Descripción del síntoma:")
            self.etiqueta_descripcion_sintoma.pack()

            self.entrada_descripcion_sintoma = tk.Entry(self)
            self.entrada_descripcion_sintoma.pack()

            self.etiqueta_fecha_hora_sintoma = tk.Label(self, text="Fecha y hora del síntoma (YYYY-MM-DD HH:MM):")
            self.etiqueta_fecha_hora_sintoma.pack()

            self.entrada_fecha_hora_sintoma = tk.Entry(self)
            self.entrada_fecha_hora_sintoma.pack()

            self.boton_registrar_sintoma = tk.Button(self, text="Registrar síntoma", command=self.registrar_sintoma)
            self.boton_registrar_sintoma.pack()

            self.etiqueta_descripcion_medicacion = tk.Label(self, text="Descripción de la medicación:")
            self.etiqueta_descripcion_medicacion.pack()

            self.entrada_descripcion_medicacion = tk.Entry(self)
            self.entrada_descripcion_medicacion.pack()

            self.etiqueta_dosis_medicacion = tk.Label(self, text="Dosis de la medicación:")
            self.etiqueta_dosis_medicacion.pack()

            self.entrada_dosis_medicacion = tk.Entry(self)
            self.entrada_dosis_medicacion.pack()

            self.etiqueta_fecha_hora_medicacion = tk.Label(self,
                                                           text="Fecha y hora de la medicación (YYYY-MM-DD HH:MM:SS):")
            self.etiqueta_fecha_hora_medicacion.pack()

            self.entrada_fecha_hora_medicacion = tk.Entry(self)
            self.entrada_fecha_hora_medicacion.pack()

            self.boton_registrar_medicacion = tk.Button(self, text="Registrar medicación",
                                                        command=self.registrar_medicacion)
            self.boton_registrar_medicacion.pack()

            self.boton_ver_registros = tk.Button(self, text="Ver registros", command=self.ver_registros)
            self.boton_ver_registros.pack()

        def ingresar_paciente(self):
            nombre_paciente = self.entrada_nombre_paciente.get()
            edad_paciente = self.entrada_edad_paciente.get()

            try:
                edad_paciente = int(edad_paciente)
            except ValueError:
                messagebox.showerror("Error", "La edad debe ser un número.")
                return

            paciente = Paciente(nombre_paciente, edad_paciente)
            self.pacientes[nombre_paciente] = paciente

            messagebox.showinfo("Éxito", "Paciente ingresado con éxito.")

        def registrar_sintoma(self):
            nombre_paciente = self.entrada_nombre_paciente.get()
            descripcion_sintoma = self.entrada_descripcion_sintoma.get()
            fecha_hora_sintoma = self.entrada_fecha_hora_sintoma.get()

            if nombre_paciente not in self.pacientes:
                messagebox.showerror("Error", "Paciente no encontrado.")
                return

            try:
                fecha_hora_sintoma = FechaHora(fecha_hora_sintoma)
            except ValueError:
                messagebox.showerror("Error", "La fecha y hora deben estar en el formato YYYY-MM-DD HH:MM.")
                return

            sintoma = Sintoma(descripcion_sintoma, fecha_hora_sintoma.fecha_hora)
            self.pacientes[nombre_paciente].registrar_sintoma(sintoma)

            messagebox.showinfo("Éxito", "Síntoma registrado con éxito.")

        def registrar_medicacion(self):
            nombre_paciente = self.entrada_nombre_paciente.get()
            descripcion_medicacion = self.entrada_descripcion_medicacion.get()
            dosis_medicacion = self.entrada_dosis_medicacion.get()
            fecha_hora_medicacion = self.entrada_fecha_hora_medicacion.get()

            if nombre_paciente not in self.pacientes:
                messagebox.showerror("Error", "Paciente no encontrado.")
                return

            try:
                fecha_hora_medicacion = FechaHora(fecha_hora_medicacion)
            except ValueError:
                messagebox.showerror("Error", "La fecha y hora deben estar en el formato YYYY-MM-DD HH:MM:SS.")
                return

            medicacion = Medicacion(descripcion_medicacion, dosis_medicacion, fecha_hora_medicacion.fecha_hora)
            self.pacientes[nombre_paciente].registrar_medicacion(medicacion)

            messagebox.showinfo("Éxito", "Medicación registrada con éxito.")

        def ver_registros(self):
            self.texto_registros.delete(1.0, tk.END)

            nombre_paciente = self.entrada_nombre_paciente.get()

            if nombre_paciente not in self.pacientes:
                messagebox.showerror("Error", "Paciente no encontrado.")
                return

            paciente = self.pacientes[nombre_paciente]

            self.texto_registros.insert(tk.END, f"Registro de {paciente.nombre}:\n")

            for sintoma in paciente.sintomas:
                self.texto_registros.insert(tk.END,
                                            f"Síntoma: {sintoma.descripcion}\nFecha y hora: {sintoma.fecha_hora}\n\n")

            for medicacion in paciente.medicaciones:
                self.texto_registros.insert(tk.END,
                                            f"Medicación: {medicacion.descripcion}\nDosis: {medicacion.dosis}\nFecha y hora: {medicacion.fecha_hora}\n\n")


if __name__ == "__main__":
    aplicacion = Aplicacion()
    aplicacion.mainloop()
