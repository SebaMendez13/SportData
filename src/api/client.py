import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("SPORTMONKS_API_TOKEN")

url = "https://api.sportmonks.com/v3/my/leagues"

response = requests.get(
    url,
    params={
        "api_token": API_TOKEN
    }
)

data = response.json()

for league in data["data"]:
    print(league["id"], "-", league["name"])