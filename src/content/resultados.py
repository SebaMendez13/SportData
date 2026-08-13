def generar_texto_resultado(partido):
    return (
        f"{partido['local']} "
        f"{partido['goles_local']} - "
        f"{partido['goles_visitante']} "
        f"{partido['visitante']}"
    )