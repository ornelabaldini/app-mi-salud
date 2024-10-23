import customtkinter as ctk

ctk.set_appearance_mode("dark")  # Modo oscuro
ctk.set_default_color_theme("blue")  # Tema de colores azul


class Colores(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configura el estilo de la ventana
        self.configure(bg_color="#2a2d2e", corner_radius=10)

        # Configura el estilo de los frames
        self.frame_entrada = ctk.CTkFrame(self, corner_radius=10, fg_color="#3a3d3f")
        self.frame_registro = ctk.CTkFrame(self, corner_radius=10, fg_color="#3a3d3f")

        # Configura el estilo de las etiquetas
        self.etiqueta_nombre_paciente = ctk.CTkLabel(self.frame_entrada, text="Nombre:", text_font=("Arial", 12),
                                                     text_color="#ffffff")

        # Configura el estilo de los botones
        self.boton_ingresar_paciente = ctk.CTkButton(self.frame_entrada, text="Ingresar paciente",
                                                     command=self.ingresar_paciente, corner_radius=10,
                                                     fg_color="#4a4d4f", hover_color="#5a5d5f")
