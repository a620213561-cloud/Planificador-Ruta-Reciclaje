from abc import ABC, abstractmethod


# Clase base abstracta
class MaterialReciclable(ABC):

    def __init__(self, nombre, cantidad_kg):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if not isinstance(cantidad_kg, (int, float)):
            raise TypeError("La cantidad debe ser numérica.")

        if isinstance(cantidad_kg, bool) or cantidad_kg < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        self.nombre = nombre
        self.cantidad_kg = cantidad_kg

    @abstractmethod
    def tipo_material(self):
        """Cada subclase debe definir su tipo."""
        pass

    def describir(self):
        return (
            f"Material: {self.nombre} | "
            f"Tipo: {self.tipo_material()} | "
            f"Cantidad: {self.cantidad_kg} kg"
        )


# Subclases: herencia y polimorfismo
class Plastico(MaterialReciclable):

    def tipo_material(self):
        return "Plástico"


class Metal(MaterialReciclable):

    def tipo_material(self):
        return "Metal"


class Papel(MaterialReciclable):

    def tipo_material(self):
        return "Papel"


class Electronico(MaterialReciclable):

    def tipo_material(self):
        return "Electrónico"


# Lugar donde se reciben los materiales
class PuntoRecoleccion:

    def __init__(self, codigo, nombre, ubicacion):
        if not codigo.strip() or not nombre.strip():
            raise ValueError("El código y el nombre son obligatorios.")

        self.codigo = codigo
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.materiales = []

    def agregar_material(self, material):
        if not isinstance(material, MaterialReciclable):
            raise TypeError("Debe ser un material reciclable válido.")

        self.materiales.append(material)

    def cantidad_total_kg(self):
        return sum(m.cantidad_kg for m in self.materiales)

    def describir(self):
        return (
            f"{self.codigo} - {self.nombre} | "
            f"Ubicación: {self.ubicacion} | "
            f"Materiales: {len(self.materiales)} | "
            f"Total: {self.cantidad_total_kg()} kg"
        )


# Ruta con puntos de recolección ordenados
class Ruta:

    def __init__(self, nombre):
        if not nombre.strip():
            raise ValueError("La ruta debe tener un nombre.")

        self.nombre = nombre
        self.puntos = []

    def agregar_punto(self, punto):
        if not isinstance(punto, PuntoRecoleccion):
            raise TypeError("Debe ser un punto de recolección.")

        if any(p.codigo == punto.codigo for p in self.puntos):
            raise ValueError("El punto ya está en esta ruta.")

        self.puntos.append(punto)

    def cantidad_total_kg(self):
        return sum(p.cantidad_total_kg() for p in self.puntos)

    def describir(self):
        nombres = " -> ".join(p.nombre for p in self.puntos)

        return (
            f"Ruta: {self.nombre} | "
            f"Puntos: {nombres} | "
            f"Carga total: {self.cantidad_total_kg()} kg"
        )


# Administración de puntos y creación de rutas
class PlanificadorRutas:

    def __init__(self):
        self.puntos = {}

    def registrar_punto(self, punto):
        if punto.codigo in self.puntos:
            raise ValueError("Ya existe un punto con ese código.")

        self.puntos[punto.codigo] = punto

    def crear_ruta(self, nombre, codigos):
        if not codigos:
            raise ValueError("La ruta necesita al menos un punto.")

        if len(codigos) != len(set(codigos)):
            raise ValueError("La ruta contiene códigos repetidos.")

        ruta = Ruta(nombre)

        for codigo in codigos:
            if codigo not in self.puntos:
                raise ValueError(
                    f"No existe el punto con código {codigo}."
                )

            ruta.agregar_punto(self.puntos[codigo])

        return ruta
