# data_resource/api.py

import requests

BASE_URL = "https://pokeapi.co/api/v2"

def get_pokemon_data(name: str):
    response = requests.get(f"{BASE_URL}/pokemon/{name.lower()}")
    if response.status_code != 200:
        return None
    return response.json()


