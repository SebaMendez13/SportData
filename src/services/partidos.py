def formatear_partido(partido):
    equipo_local = None
    equipo_visitante = None

    for equipo in partido["participants"]:
        if equipo["meta"]["location"] == "home":
            equipo_local = equipo["name"]

        elif equipo["meta"]["location"] == "away":
            equipo_visitante = equipo["name"]

    return {
        "id": partido["id"],
        "local": equipo_local,
        "visitante": equipo_visitante,
        "fecha": partido["starting_at"]
    }


def formatear_partidos(partidos):
    partidos_formateados = []

    for partido in partidos:
        partidos_formateados.append(
            formatear_partido(partido)
        )

    return partidos_formateados