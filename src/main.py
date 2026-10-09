from reciclaje import MaterialReciclable


def main():
    print("==============================")
    print("PLANIFICADOR DE RUTA DE RECICLAJE")
    print("==============================")

    material = MaterialReciclable("Plástico", 15)

    print("Proyecto iniciado correctamente.")
    print(material.describir())


if __name__ == "__main__":
    main()