def formatear_partido(partido):
    equipo_local = None
    equipo_visitante = None

    goles_local = None
    goles_visitante = None

    for equipo in partido["participants"]:
        if equipo["meta"]["location"] == "home":
            equipo_local = equipo["name"]

        elif equipo["meta"]["location"] == "away":
            equipo_visitante = equipo["name"]

    for marcador in partido["scores"]:
        if marcador["description"] == "CURRENT":

            if marcador["score"]["participant"] == "home":
                goles_local = marcador["score"]["goals"]

            elif marcador["score"]["participant"] == "away":
                goles_visitante = marcador["score"]["goals"]

    return {
        "id": partido["id"],
        "local": equipo_local,
        "visitante": equipo_visitante,
        "goles_local": goles_local,
        "goles_visitante": goles_visitante,
        "fecha": partido["starting_at"]
    }


def formatear_partidos(partidos):
    partidos_formateados = []

    for partido in partidos:
        partidos_formateados.append(
            formatear_partido(partido)
        )

    return partidos_formateados













