
import customtkinter as ctk

# Configuración visual
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")


class AplicacionReciclaje(ctk.CTk):
    def __init__(self):
        super().__init__()

                # Registros temporales de materiales
        self.materiales = []

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
                font=("Arial", 15),
                command=lambda nombre=opcion: self.abrir_seccion(nombre)
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

                # Mostrar el Dashboard al iniciar la aplicación
        self.mostrar_dashboard()

    def mostrar_dashboard(self):
                # Limpiar el contenido anterior
        for elemento in self.contenido.winfo_children():
            elemento.destroy()

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

        # Contenedor de tarjetas de estadísticas
        self.tarjetas = ctk.CTkFrame(
            self.contenido,
            fg_color="transparent"
        )
        self.tarjetas.pack(fill="x", pady=(10, 20))

       
        # Calcular estadísticas con los materiales registrados
        total_kg = sum(material["peso"] for material in self.materiales)
        tipos_registrados = len(
            set(material["tipo"] for material in self.materiales)
        )

        estadisticas = [
            ("📍 Puntos de recolección", "0", "#E1F8EC"),
            ("♻️ Materiales recolectados", f"{total_kg:.2f} kg", "#E1F8EC"),
            ("🚚 Rutas creadas", "0", "#E8F3FF"),
            ("📦 Tipos de materiales", str(tipos_registrados), "#F1E8FF")
        ]


        for columna, (nombre, valor, color) in enumerate(estadisticas):
            tarjeta = ctk.CTkFrame(
                self.tarjetas,
                fg_color="white",
                corner_radius=12,
                border_width=1,
                border_color="#E2E8F0"
            )
            tarjeta.grid(
                row=0,
                column=columna,
                padx=5,
                sticky="nsew"
            )

            ctk.CTkLabel(
                tarjeta,
                text=nombre,
                font=("Arial", 12),
                text_color="#475569",
                wraplength=150
            ).pack(padx=12, pady=(20, 8))

            ctk.CTkLabel(
                tarjeta,
                text=valor,
                font=("Arial", 27, "bold"),
                text_color="#087A53"
            ).pack(padx=12, pady=(0, 20))

            self.tarjetas.grid_columnconfigure(columna, weight=1)


    def abrir_seccion(self, nombre):

        
        # Mostrar el Dashboard al seleccionar Inicio
        if nombre == "Inicio":
            self.mostrar_dashboard()
            return


        # Eliminar el contenido actual de la pantalla
        for elemento in self.contenido.winfo_children():
            elemento.destroy()

        # Mostrar el título de la sección seleccionada
        titulo = ctk.CTkLabel(
            self.contenido,
            text=nombre,
            font=("Arial", 32, "bold"),
            text_color="#10201B"
        )
        titulo.pack(anchor="w", pady=(0, 10))

        if nombre == "Materiales":
            descripcion = (
                "Administra los materiales reciclables "
                "y sus cantidades en kilogramos."
            )
        else:
            descripcion = f"Sección de {nombre} en desarrollo."

        ctk.CTkLabel(
            self.contenido,
            text=descripcion,
            font=("Arial", 16),
            text_color="#64748B"
        ).pack(anchor="w")

                # Botón para agregar materiales
        if nombre == "Materiales":
            boton_agregar = ctk.CTkButton(
                self.contenido,
                text="+ Agregar material",
                font=("Arial", 15, "bold"),
                fg_color="#007A43",
                hover_color="#005C32",
                height=45,
                corner_radius=10,
                command=self.mostrar_formulario_material
            )
            boton_agregar.pack(anchor="e", pady=(20, 10))
            
            # Tabla de materiales registrados
            tabla = ctk.CTkFrame(
                self.contenido,
                fg_color="white",
                corner_radius=10
            )
            tabla.pack(fill="x", pady=(15, 10))

            encabezados = ["Tipo", "Nombre", "Cantidad (kg)", "Descripción"]

            for columna, texto in enumerate(encabezados):
                etiqueta = ctk.CTkLabel(
                    tabla,
                    text=texto,
                    font=("Arial", 13, "bold"),
                    text_color="#10201B"
                )
                etiqueta.grid(
                    row=0,
                    column=columna,
                    padx=12,
                    pady=15,
                    sticky="w"
                )
                tabla.grid_columnconfigure(columna, weight=1)
                
            # Mostrar los materiales registrados
            for fila, material in enumerate(self.materiales, start=1):
                datos = [
                    material["tipo"],
                    material["nombre"],
                    f'{material["peso"]:g} kg',
                    material["descripcion"]
                ]

                for columna, valor in enumerate(datos):
                    etiqueta = ctk.CTkLabel(
                        tabla,
                        text=valor,
                        font=("Arial", 12),
                        text_color="#475569",
                        wraplength=180
                    )
                    etiqueta.grid(
                        row=fila,
                        column=columna,
                        padx=12,
                        pady=10,
                        sticky="w"
                    )



            
    def mostrar_formulario_material(self):
        # Crear ventana secundaria
        self.ventana_material = ctk.CTkToplevel(self)
        self.ventana_material.title("Agregar material reciclable")
        self.ventana_material.geometry("450x520")
        self.ventana_material.resizable(False, False)
        self.ventana_material.grab_set()

        ctk.CTkLabel(
            self.ventana_material,
            text="Agregar material reciclable",
            font=("Arial", 23, "bold")
        ).pack(pady=(25, 20))

        # Seleccionar tipo de material
        ctk.CTkLabel(
            self.ventana_material,
            text="Tipo de material"
        ).pack(pady=(5, 5))

        self.tipo_material = ctk.CTkOptionMenu(
            self.ventana_material,
            values=["Plástico", "Metal", "Papel", "Electrónico"],
            width=330
        )
        self.tipo_material.pack(pady=(0, 15))

        # Nombre del material
        self.nombre_material = ctk.CTkEntry(
            self.ventana_material,
            placeholder_text="Ejemplo: Botellas PET",
            width=330
        )
        self.nombre_material.pack(pady=10)

        # Cantidad en kilogramos
        self.peso_material = ctk.CTkEntry(
            self.ventana_material,
            placeholder_text="Cantidad en kg (ejemplo: 25.5)",
            width=330
        )
        self.peso_material.pack(pady=10)

        # Descripción
        self.descripcion_material = ctk.CTkEntry(
            self.ventana_material,
            placeholder_text="Descripción del material",
            width=330
        )
        self.descripcion_material.pack(pady=10)

        # Botón guardar
        ctk.CTkButton(
            self.ventana_material,
            text="Guardar material",
            fg_color="#007A43",
            hover_color="#005C32",
            width=330,
            height=45,
            command=self.guardar_material
        ).pack(pady=25)


    def guardar_material(self):
        from tkinter import messagebox

        tipo = self.tipo_material.get()
        nombre = self.nombre_material.get().strip()
        peso_texto = self.peso_material.get().strip()
        descripcion = self.descripcion_material.get().strip()

        if not nombre or not peso_texto:
            messagebox.showwarning(
                "Datos incompletos",
                "Ingresa el nombre y el peso del material."
            )
            return

        try:
            peso = float(peso_texto.replace(",", "."))
            if peso <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Error",
                "El peso debe ser un número mayor que cero."
            )
            return

        material = {
            "tipo": tipo,
            "nombre": nombre,
            "peso": peso,
            "descripcion": descripcion
        }

        self.materiales.append(material)
        self.ventana_material.destroy()
        self.abrir_seccion("Materiales")

        messagebox.showinfo(
            "Registro exitoso",
            f"Se registró {nombre} con {peso:g} kg."
        )



if __name__ == "__main__":
    app = AplicacionReciclaje()
    app.mainloop()
