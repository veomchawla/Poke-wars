from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

BASE_URL = "https://pokeapi.co/api/v2"


@router.get("/{name}")
async def get_pokemon_by_name(name: str):
    """
    Fetch Pokémon details by name from the PokeAPI.
    Example: /pokemon/eevee
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{BASE_URL}/pokemon/{name.lower()}")
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=f"Error connecting to API: {str(e)}")

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail=f"Pokémon '{name}' not found")

    return response.json()

