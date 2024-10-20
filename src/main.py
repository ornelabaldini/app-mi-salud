import tkinter as tk
from tkinter import messagebox
from src.paciente.paciente import Paciente
from src.registro.sintoma import Sintoma
from src.registro.medicacion import Medicacion
from src.utils.fecha_hora import FechaHora

class Aplicacion(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("                      Registro en Mi Salud")
            self.geometry("900x700")

            self.pacientes = {}

            self.etiqueta_titulo = tk.Label(self, text="Registro de Pacientes")
            self.etiqueta_titulo.pack()

            self.etiqueta_nombre_paciente = tk.Label(self, text="Nombre:")
            self.etiqueta_nombre_paciente.pack()

            self.entrada_nombre_paciente = tk.Entry(self)
            self.entrada_nombre_paciente.pack()
            self.entrada_nombre_paciente.bind("<Return>", lambda event: self.entrada_edad_paciente.focus_set())

            self.etiqueta_edad_paciente = tk.Label(self, text="Edad:")
            self.etiqueta_edad_paciente.pack()

            self.entrada_edad_paciente = tk.Entry(self)
            self.entrada_edad_paciente.pack()
            self.entrada_edad_paciente.bind("<Return>", lambda event: self.entrada_descripcion_sintoma.focus_set())

            self.boton_ingresar_paciente = tk.Button(self, text="Ingresar paciente", command=self.ingresar_paciente)
            self.boton_ingresar_paciente.pack()

            self.etiqueta_descripcion_sintoma = tk.Label(self, text="Descripción del síntoma:")
            self.etiqueta_descripcion_sintoma.pack()

            self.entrada_descripcion_sintoma = tk.Entry(self)
            self.entrada_descripcion_sintoma.pack()
            self.entrada_descripcion_sintoma.bind("<Return>", lambda event: self.entrada_fecha_hora_sintoma.focus_set())

            self.etiqueta_fecha_hora_sintoma = tk.Label(self, text="Fecha y hora del síntoma (YYYY-MM-DD HH:MM):")
            self.etiqueta_fecha_hora_sintoma.pack()

            self.entrada_fecha_hora_sintoma = tk.Entry(self)
            self.entrada_fecha_hora_sintoma.pack()
            self.entrada_fecha_hora_sintoma.bind("<Return>",
                                                 lambda event: self.entrada_descripcion_medicacion.focus_set())

            self.boton_registrar_sintoma = tk.Button(self, text="Registrar síntoma", command=self.registrar_sintoma)
            self.boton_registrar_sintoma.pack()

            self.etiqueta_descripcion_medicacion = tk.Label(self, text="Descripción de la medicación:")
            self.etiqueta_descripcion_medicacion.pack()

            self.entrada_descripcion_medicacion = tk.Entry(self)
            self.entrada_descripcion_medicacion.pack()
            self.entrada_descripcion_medicacion.bind("<Return>",
                                                     lambda event: self.entrada_dosis_medicacion.focus_set())

            self.etiqueta_dosis_medicacion = tk.Label(self, text="Dosis de la medicación:")
            self.etiqueta_dosis_medicacion.pack()

            self.entrada_dosis_medicacion = tk.Entry(self)
            self.entrada_dosis_medicacion.pack()
            self.entrada_dosis_medicacion.bind("<Return>", lambda event: self.entrada_fecha_hora_medicacion.focus_set())

            self.etiqueta_fecha_hora_medicacion = tk.Label(self,
                                                           text="Fecha y hora de la medicación (YYYY-MM-DD HH:MM:SS):")
            self.etiqueta_fecha_hora_medicacion.pack()

            self.entrada_fecha_hora_medicacion = tk.Entry(self)
            self.entrada_fecha_hora_medicacion.pack()

            self.boton_registrar_medicacion = tk.Button(self, text="Registrar medicación",
                                                        command=self.registrar_medicacion)
            self.boton_registrar_medicacion.pack()
            self.boton_registrar_medicacion.pack(pady=(0,20))

            self.boton_ver_registros = tk.Button(self, text="Ver registro actual", command=self.ver_registros)
            self.boton_ver_registros.pack()


            self.boton_ver_registro_pacientes = tk.Button(self, text="Ver registro de pacientes",
                                                          command=self.ver_registro_pacientes)
            self.boton_ver_registro_pacientes.pack()
            self.texto_registros = tk.Text(self, width=100, height=10.4)
            self.texto_registros.pack()


        def ingresar_paciente(self):
            nombre_paciente = self.entrada_nombre_paciente.get()
            edad_paciente = self.entrada_edad_paciente.get()
            if nombre_paciente in self.pacientes:
                messagebox.showerror("Error", "Paciente ya existe.")
                return
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

            paciente = self.pacientes[nombre_paciente]
            for registro in paciente.registros:
                if isinstance(registro, Medicacion) and registro.fecha_hora == fecha_hora_sintoma.fecha_hora:
                    messagebox.showerror("Error", "La fecha y hora síntoma ya están registradas.")
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

            paciente = self.pacientes[nombre_paciente]
            for registro in paciente.registros:
                if isinstance(registro, Medicacion) and registro.fecha_hora == fecha_hora_medicacion.fecha_hora:
                    messagebox.showerror("Error", "La fecha y hora de la medicación ya están registradas.")
                    return

            medicacion = Medicacion(descripcion_medicacion, fecha_hora_medicacion.fecha_hora, dosis_medicacion)
            paciente.registrar_medicacion(medicacion)
            messagebox.showinfo("Éxito", "Medicación registrada con éxito.")

        def ver_registros(self):
            self.texto_registros.delete(5.0, tk.END)
            nombre_paciente = self.entrada_nombre_paciente.get()
            if nombre_paciente not in self.pacientes:
                messagebox.showerror("Error", "Paciente no encontrado.")
                return
            paciente = self.pacientes[nombre_paciente]
            self.texto_registros.insert(tk.END, f"Registro de {paciente.nombre}:\n")
            for registro in paciente.registros:
                if isinstance(registro, Sintoma):
                    self.texto_registros.insert(tk.END,
                                                f"{registro.descripcion}\nFecha y hora del registro: {registro.fecha_hora}\n\n")
                elif isinstance(registro, Medicacion):
                    self.texto_registros.insert(tk.END,
                                                f"Medicación: {registro.descripcion}\nDosis: {registro.dosis}\nFecha y hora de medicación: {registro.fecha_hora}\n\n")

        def ver_registros_paciente(self):
            nombre_paciente = self.entrada_nombre_paciente.get()
            if nombre_paciente not in self.pacientes:
                messagebox.showerror("Error", "Paciente no encontrado.")
                return
            paciente = self.pacientes[nombre_paciente]
            paciente.ver_registros()

        def ver_registro_pacientes(self):
            ventana_registro = tk.Toplevel(self)
            ventana_registro.title("Registro de pacientes")
            texto_registro_pacientes = tk.Text(ventana_registro)
            texto_registro_pacientes.pack(fill="both", expand=True)
            for paciente in self.pacientes.values():
                texto_registro_pacientes.insert(tk.END, f"REGISTRO DE {paciente.nombre}:\n")
                paciente.ver_registros()
                for registro in paciente.registros:
                    if isinstance(registro, Sintoma):
                        texto_registro_pacientes.insert(tk.END,
                                                        f"Hora de registro: {registro.fecha_hora}\n\n")
                    elif isinstance(registro, Medicacion):
                        texto_registro_pacientes.insert(tk.END,
                                                        f"Medicación: {registro.descripcion}\nDosis: {registro.dosis}\nFecha y hora de medicación: {registro.fecha_hora}\n\n")

class AutoFocusEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<Return>", self.next_field)

    def next_field(self, event=None):
        widgets = self.master.winfo_children()
        index = widgets.index(self)
        if index < len(widgets) - 1:
            widgets[index + 1].focus_set()


if __name__ == "__main__":
    aplicacion = Aplicacion()
    aplicacion.mainloop()
