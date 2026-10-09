class MaterialReciclable:
    """Representa un material que se puede reciclar."""

    def __init__(self, nombre, cantidad_kg):
        self.nombre = nombre
        self.cantidad_kg = cantidad_kg

    def describir(self):
        return (
            f"Material: {self.nombre} | "
            f"Cantidad: {self.cantidad_kg} kg"
        )