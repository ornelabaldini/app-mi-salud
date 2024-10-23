import customtkinter as ctk


from src.models.entidades.paciente import Paciente
from src.models.entidades.medicacion import Medicacion
from src.models.entidades.sintoma import Sintoma
from src.models.dao.fecha_hora import FechaHora

class InterfazGrafica(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Registro de Pacientes")
        self.geometry("1000x1000")
        self.pacientes = {}
        self.fecha_hora = FechaHora()

        # Frame para entrada de datos
        self.frame_entrada = ctk.CTkFrame(self, corner_radius=10, fg_color="#3a3d3f")
        self.frame_entrada.pack(pady=10, padx=10)

        # Etiquetas y entradas para paciente
        self.etiqueta_nombre_paciente = ctk.CTkLabel(self.frame_entrada, text="Nombre:", font=("Arial",20))
        self.etiqueta_nombre_paciente.grid(row=0, column=0, pady=10, padx=10)
        self.entrada_nombre_paciente = ctk.CTkEntry(self.frame_entrada)
        self.entrada_nombre_paciente.grid(row=0, column=1, pady=10, padx=(5,0))

        self.etiqueta_edad_paciente = ctk.CTkLabel(self.frame_entrada, text="Edad:", font=("Arial",20))
        self.etiqueta_edad_paciente.grid(row=1, column=0, pady=10, padx=(5,0))
        self.entrada_edad_paciente = ctk.CTkEntry(self.frame_entrada)
        self.entrada_edad_paciente.grid(row=1, column=1, pady=10, padx=10)

        # Botón para ingresar paciente
        self.boton_ingresar_paciente = ctk.CTkButton(self.frame_entrada, text="Ingresar paciente", command=self.ingresar_paciente, font=("Arial",20))
        self.boton_ingresar_paciente.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

        # Frame para registro de síntomas y medicaciones
        self.frame_registro = ctk.CTkFrame(self)
        self.frame_registro.pack(pady=20, padx=10)

        # Etiquetas y entradas para síntoma
        self.etiqueta_descripcion_sintoma = ctk.CTkLabel(self.frame_registro, text="Descripción del síntoma:",font=("Arial",20))
        self.etiqueta_descripcion_sintoma.grid(row=0, column=0, pady=10, padx=10)
        self.entrada_descripcion_sintoma = ctk.CTkEntry(self.frame_registro)
        self.entrada_descripcion_sintoma.grid(row=0, column=1, pady=10, padx=10)

        self.etiqueta_fecha_hora_sintoma = ctk.CTkLabel(self.frame_registro, text="Fecha y hora del síntoma:", font=("Arial",20))
        self.etiqueta_fecha_hora_sintoma.grid(row=1, column=0, pady=10, padx=10)
        self.entrada_fecha_hora_sintoma = ctk.CTkEntry(self.frame_registro)
        self.entrada_fecha_hora_sintoma.grid(row=1, column=1, pady=10, padx=10)

        # Botón para registrar síntoma
        self.boton_registrar_sintoma = ctk.CTkButton(self.frame_registro, text="Registrar síntoma", command=self.registrar_sintoma, font=("Arial",20))
        self.boton_registrar_sintoma.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

        # Etiquetas y entradas para medicación
        self.etiqueta_descripcion_medicacion = ctk.CTkLabel(self.frame_registro, text="Descripción de la medicación:", font=("Arial",20))
        self.etiqueta_descripcion_medicacion.grid(row=3, column=0, pady=10, padx=10)
        self.entrada_descripcion_medicacion = ctk.CTkEntry(self.frame_registro)
        self.entrada_descripcion_medicacion.grid(row=3, column=1, pady=10, padx=10)

        self.etiqueta_dosis_medicacion = ctk.CTkLabel(self.frame_registro, text="Dosis de la medicación:", font=("Arial",20))
        self.etiqueta_dosis_medicacion.grid(row=4, column=0, pady=10, padx=10)
        self.entrada_dosis_medicacion = ctk.CTkEntry(self.frame_registro)
        self.entrada_dosis_medicacion.grid(row=4, column=1)

        self.etiqueta_fecha_hora_medicacion = ctk.CTkLabel(self.frame_registro, text="Fecha y hora de la medicación:", font=("Arial",20))
        self.etiqueta_fecha_hora_medicacion.grid(row=5, column=0, pady=10, padx=10)
        self.entrada_fecha_hora_medicacion = ctk.CTkEntry(self.frame_registro)
        self.entrada_fecha_hora_medicacion.grid(row=5, column=1, pady=10, padx=10)

        # Botón para registrar medicación
        self.boton_registrar_medicacion = ctk.CTkButton(self.frame_registro, text="Registrar medicación", command=self.registrar_medicacion, font=("Arial",20))
        self.boton_registrar_medicacion.grid(row=6, column=0, columnspan=2, pady=10, padx=10)

        # Botón para ver registros
        self.boton_ver_registros = ctk.CTkButton(self.frame_registro, text="Ver registros", command=self.ver_registros, font=("Arial",20))
        self.boton_ver_registros.grid(row=7, column=0, columnspan=2, pady=10, padx=10)


        # Botón para ver registro actual
        self.boton_ver_registro_actual = ctk.CTkButton(self.frame_registro, text="Ver registro actual",
                                                       command=self.ver_registro_actual, font=("Arial",20))
        self.boton_ver_registro_actual.grid(row=8, column=0, columnspan=2, pady=10, padx=10)


    def ingresar_paciente(self):
        nombre_paciente = self.entrada_nombre_paciente.get()
        edad_paciente = self.entrada_edad_paciente.get()

        if not edad_paciente:
            self.mostrar_mensaje_exito("Error: La edad no puede estar vacía.")
            return

        if nombre_paciente in self.pacientes:
            self.mostrar_mensaje_exito("Error: Paciente ya existe.")
            return

        try:
            edad_paciente = int(edad_paciente)
        except ValueError:
            self.mostrar_mensaje_exito("Error: La edad debe ser un número.")
            return

        paciente = Paciente(nombre_paciente, edad_paciente)
        self.pacientes[nombre_paciente] = paciente
        self.mostrar_mensaje_exito("Paciente ingresado con éxito.")

    def registrar_sintoma(self):
        nombre_paciente = self.entrada_nombre_paciente.get()
        descripcion_sintoma = self.entrada_descripcion_sintoma.get()
        fecha_hora_sintoma = self.entrada_fecha_hora_sintoma.get()
        if nombre_paciente not in self.pacientes:
            self.mostrar_mensaje_exito("Error: Paciente no existe.")
            return
        sintoma = Sintoma(descripcion_sintoma, fecha_hora_sintoma)
        self.pacientes[nombre_paciente].registrar_sintoma(sintoma)
        self.mostrar_mensaje_exito("Síntoma registrado con éxito.")

    def registrar_medicacion(self):
        nombre_paciente = self.entrada_nombre_paciente.get()
        descripcion_medicacion = self.entrada_descripcion_medicacion.get()
        dosis_medicacion = self.entrada_dosis_medicacion.get()
        fecha_hora_medicacion = self.entrada_fecha_hora_medicacion.get()
        if nombre_paciente not in self.pacientes:
            self.mostrar_mensaje_exito("Error: Paciente no existe.")
            return
        medicacion = Medicacion(descripcion_medicacion, dosis_medicacion, fecha_hora_medicacion)
        self.pacientes[nombre_paciente].registrar_medicacion(medicacion)
        self.mostrar_mensaje_exito("Medicación registrada con éxito.")

    def ver_registros(self):
        mensaje = "Registros de todos los pacientes:\n\n"
        self.geometry("1000x1000")

        for paciente, registros_paciente in self.pacientes.items():
            mensaje += f"Registros de {paciente}:\n\n"

            for registro in registros_paciente.registros:
                if isinstance(registro, Sintoma):
                    mensaje += f"Síntoma: {registro.descripcion} - Fecha y hora: {registro.fecha_hora}\n\n"
                elif isinstance(registro, Medicacion):
                    mensaje += f"Medicación: {registro.descripcion} - Dosis: {registro.dosis} - Fecha y hora: {registro.fecha_hora}\n\n"

            mensaje += "\n"

        self.mostrar_mensaje_exito(mensaje)

    def ver_registro_actual(self):
        nombre_paciente = self.entrada_nombre_paciente.get()
        if nombre_paciente in self.pacientes:
            registros = self.pacientes[nombre_paciente].registros
            if registros:
                registro = registros[-1]
                if isinstance(registro, Sintoma):
                    mensaje = f"Registro de {nombre_paciente}:\n\nSíntoma: {registro.descripcion} - Fecha y hora: {registro.fecha_hora}"
                elif isinstance(registro, Medicacion):
                    mensaje = f"Registro de {nombre_paciente}:\n\nMedicación: {registro.descripcion} - Dosis: {registro.dosis} - Fecha y hora: {registro.fecha_hora}"
                    self.mostrar_mensaje_exito(mensaje)
            else:
                self.mostrar_mensaje_exito("No hay registros.")
        else:
            self.mostrar_mensaje_exito("Error: Paciente no existe.")

    def mostrar_mensaje_exito(self, mensaje):
        ventana_mensaje = ctk.CTkToplevel(self)
        ventana_mensaje.title("Éxito")

        etiqueta_mensaje = ctk.CTkLabel(ventana_mensaje, text=mensaje, font=("Arial",20))
        etiqueta_mensaje.pack(pady=20, padx=10)

        boton_aceptar = ctk.CTkButton(ventana_mensaje, text="Aceptar", command=ventana_mensaje.destroy, font=("Arial",20))
        boton_aceptar.pack(pady=20, padx=10)




