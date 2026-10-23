from reciclaje import (
    Plastico,
    Metal,
    Papel,
    Electronico,
    PuntoRecoleccion,
    PlanificadorRutas,
)


def main():
    print("=" * 45)
    print("PLANIFICADOR DE RUTA DE RECICLAJE")
    print("=" * 45)

    # 1. Crear materiales reciclables
    plastico = Plastico("Botellas PET", 15)
    metal = Metal("Latas de aluminio", 8)
    papel = Papel("Carton", 12)
    electronico = Electronico("Cables", 2.5)

    # 2. Crear puntos de recoleccion
    punto1 = PuntoRecoleccion(
        "P001", "Centro Norte", "CDMX"
    )
    punto2 = PuntoRecoleccion(
        "P002", "Parque Central", "CDMX"
    )

    # 3. Asociar materiales a los puntos
    punto1.agregar_material(plastico)
    punto1.agregar_material(metal)

    punto2.agregar_material(papel)
    punto2.agregar_material(electronico)

    # 4. Registrar los puntos en el planificador
    planificador = PlanificadorRutas()
    planificador.registrar_punto(punto1)
    planificador.registrar_punto(punto2)

    # 5. Crear una ruta con los puntos registrados
    ruta = planificador.crear_ruta(
        "Ruta 1", ["P001", "P002"]
    )

    # 6. Mostrar los resultados
    print("\nMATERIALES REGISTRADOS")
    for material in [plastico, metal, papel, electronico]:
        print(material.describir())

    print("\nPUNTOS DE RECOLECCION")
    print(punto1.describir())
    print(punto2.describir())

    print("\nRUTA GENERADA")
    print(ruta.describir())

    print("\nProceso finalizado.")


if __name__ == "__main__":
    main()
