from src.api.client import obtener_partidos_por_fecha
from src.services.partidos import formatear_partidos, crear_texto_resultado
from src.content.resultados import generar_texto_resultado


partidos = obtener_partidos_por_fecha("2026-08-09", 501)

partidos_formateados = formatear_partidos(partidos)

for partido in partidos_formateados:
    print(generar_texto_resultado(partido))