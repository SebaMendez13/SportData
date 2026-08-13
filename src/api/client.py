import os
import requests
from dotenv import load_dotenv
from datetime import date

from src.services.partidos import formatear_partido, formatear_partidos


load_dotenv()

TOKEN_API = os.getenv("SPORTMONKS_API_TOKEN")

#INICIO DEL PROGRAMA

def obtener_partidos_por_fecha(fecha, id_liga=None):
    url = f"https://api.sportmonks.com/v3/football/fixtures/date/{fecha}"

    parametros = {
        "api_token": TOKEN_API,
        "include": "participants;scores"
    }

    if id_liga is not None:
        parametros["filters"] = f"fixtureLeagues:{id_liga}"

    try:
        respuesta = requests.get(
            url,
            params=parametros,
            timeout=10
        )

        if respuesta.status_code != 200:
            print("Error al consultar Sportmonks:", respuesta.status_code)
            return []

        datos = respuesta.json()

        return datos["data"]

    except requests.exceptions.Timeout:
        print("Sportmonks tardó demasiado en responder.")
        return []

    except requests.exceptions.ConnectionError:
        print("No se pudo conectar con Sportmonks.")
        return []

    except requests.exceptions.RequestException as error:
        print("Ocurrió un error al consultar Sportmonks:", error)
        return []







