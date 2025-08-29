from fastapi.testclient import TestClient
from mcp_tool import router
import pytest
import random

from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

client = TestClient(app)

def test_simulate_valid_pokemon():
    response = client.post("/simulate", params={"pokemon1": "Pikachu", "pokemon2": "Charmander"})
    assert response.status_code == 200
    data = response.json()
    assert "winner" in data
    assert "log" in data
    assert isinstance(data["log"], list)

def test_simulate_invalid_pokemon():
    response = client.post("/simulate", params={"pokemon1": "Invalid1", "pokemon2": "Invalid2"})
    assert response.status_code == 200
    data = response.json()
    assert data["winner"] == "None"
    assert "One or both Pokémon not found." in data["log"]

def test_strategy_valid_pokemon():
    response = client.get("/strategy/pikachu")
    assert response.status_code == 200
    data = response.json()
    assert data["pokemon"].lower() == "pikachu"
    assert "recommended_move" in data
    assert isinstance(data["type_advantage"], list)

def test_strategy_invalid_pokemon():
    response = client.get("/strategy/unknownmon")
    assert response.status_code == 404
    assert response.json()["detail"] == "Strategy not found"

def test_status_valid_pokemon():
    response = client.get("/status/squirtle")
    assert response.status_code == 200
    data = response.json()
    assert data["pokemon"].lower() == "squirtle"
    assert "hp" in data
    assert data["status_condition"] is None

def test_status_invalid_pokemon():
    response = client.get("/status/somefake")
    assert response.status_code == 404

def test_moves_valid_pokemon():
    response = client.get("/moves/bulbasaur")
    assert response.status_code == 200
    moves = response.json()
    assert isinstance(moves, list)
    assert any("name" in move for move in moves)

def test_moves_invalid_pokemon():
    response = client.get("/moves/missingno")
    assert response.status_code == 404

