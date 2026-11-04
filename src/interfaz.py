
import customtkinter as ctk

# Configuración visual
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")


class AplicacionReciclaje(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Ventana principal
        self.title("Planificador de Ruta de Reciclaje")
        self.geometry("1100x700")
        self.minsize(900, 600)

        # Fondo de la aplicación
        self.configure(fg_color="#F4F7F6")

        # Panel lateral
        self.menu = ctk.CTkFrame(
            self,
            width=250,
            corner_radius=0,
            fg_color="#063D2E"
        )
        self.menu.pack(side="left", fill="y")
        self.menu.pack_propagate(False)

        # Nombre del sistema
        self.logo = ctk.CTkLabel(
            self.menu,
            text="♻  Planificador\n     de Reciclaje",
            font=("Arial", 23, "bold"),
            text_color="white"
        )
        self.logo.pack(pady=(45, 50))

        # Botones del menú
        opciones = [
            "Inicio",
            "Puntos de recolección",
            "Materiales",
            "Rutas",
            "Reportes",
            "Configuración"
        ]

        for opcion in opciones:
            boton = ctk.CTkButton(
                self.menu,
                text=opcion,
                height=45,
                fg_color="transparent",
                hover_color="#087A53",
                anchor="w",
                font=("Arial", 15)
            )
            boton.pack(fill="x", padx=15, pady=5)

        # Área principal
        self.contenido = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        self.contenido.pack(
            side="left",
            fill="both",
            expand=True,
            padx=35,
            pady=35
        )

        self.titulo = ctk.CTkLabel(
            self.contenido,
            text="Dashboard",
            font=("Arial", 32, "bold"),
            text_color="#10201B"
        )
        self.titulo.pack(anchor="w")

        self.subtitulo = ctk.CTkLabel(
            self.contenido,
            text="Resumen general del sistema",
            font=("Arial", 16),
            text_color="#64748B"
        )
        self.subtitulo.pack(anchor="w", pady=(5, 25))

        self.mensaje = ctk.CTkLabel(
            self.contenido,
            text="¡Bienvenido al Planificador de Ruta de Reciclaje!",
            font=("Arial", 19),
            text_color="#087A53"
        )
        self.mensaje.pack(pady=80)


if __name__ == "__main__":
    app = AplicacionReciclaje()
    app.mainloop()
