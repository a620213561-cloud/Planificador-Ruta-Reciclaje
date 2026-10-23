import pytest

from src.reciclaje import (
    MaterialReciclable,
    Plastico,
    Metal,
    Papel,
    Electronico,
    PuntoRecoleccion,
    Ruta,
    PlanificadorRutas,
)


def test_materiales_identifican_su_tipo():
    assert Plastico("Botellas", 15).tipo_material() == "Plástico"
    assert Metal("Latas", 8).tipo_material() == "Metal"
    assert Papel("Cartón", 12).tipo_material() == "Papel"
    assert Electronico("Cables", 2.5).tipo_material() == "Electrónico"


def test_material_describe_su_informacion():
    material = Plastico("Botellas PET", 15)
    assert "Botellas PET" in material.describir()
    assert "15 kg" in material.describir()


def test_material_no_acepta_cantidad_negativa():
    with pytest.raises(ValueError):
        Plastico("Botellas", -1)


def test_material_no_acepta_nombre_vacio():
    with pytest.raises(ValueError):
        Plastico("   ", 10)


def test_material_base_es_abstracta():
    with pytest.raises(TypeError):
        MaterialReciclable("Material", 10)


def test_punto_calcula_peso_total():
    punto = PuntoRecoleccion("P001", "Centro Norte", "CDMX")
    punto.agregar_material(Plastico("Botellas", 15))
    punto.agregar_material(Metal("Latas", 8))

    assert punto.cantidad_total_kg() == 23


def test_punto_rechaza_objeto_que_no_es_material():
    punto = PuntoRecoleccion("P001", "Centro Norte", "CDMX")

    with pytest.raises(TypeError):
        punto.agregar_material("Plástico")


def test_ruta_calcula_peso_de_sus_puntos():
    punto1 = PuntoRecoleccion("P001", "Centro Norte", "CDMX")
    punto1.agregar_material(Plastico("Botellas", 15))

    punto2 = PuntoRecoleccion("P002", "Parque Central", "CDMX")
    punto2.agregar_material(Papel("Cartón", 12))

    ruta = Ruta("Ruta 1")
    ruta.agregar_punto(punto1)
    ruta.agregar_punto(punto2)

    assert ruta.cantidad_total_kg() == 27


def test_ruta_rechaza_punto_duplicado():
    punto = PuntoRecoleccion("P001", "Centro Norte", "CDMX")
    ruta = Ruta("Ruta 1")
    ruta.agregar_punto(punto)

    with pytest.raises(ValueError):
        ruta.agregar_punto(punto)


def test_planificador_crea_ruta():
    planificador = PlanificadorRutas()
    punto1 = PuntoRecoleccion("P001", "Centro Norte", "CDMX")
    punto2 = PuntoRecoleccion("P002", "Parque Central", "CDMX")

    planificador.registrar_punto(punto1)
    planificador.registrar_punto(punto2)

    ruta = planificador.crear_ruta(
        "Ruta de prueba",
        ["P001", "P002"],
    )

    assert len(ruta.puntos) == 2
    assert ruta.puntos[0].codigo == "P001"
    assert ruta.puntos[1].codigo == "P002"


def test_planificador_rechaza_codigo_desconocido():
    planificador = PlanificadorRutas()

    with pytest.raises(ValueError):
        planificador.crear_ruta("Ruta inválida", ["P999"])


def test_planificador_rechaza_punto_registrado_dos_veces():
    planificador = PlanificadorRutas()
    punto = PuntoRecoleccion("P001", "Centro Norte", "CDMX")
    planificador.registrar_punto(punto)

    with pytest.raises(ValueError):
        planificador.registrar_punto(punto)
