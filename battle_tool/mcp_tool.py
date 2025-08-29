from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from battle_tool.engine import (
    simulate_battle,
    get_battle_strategy,
    get_battle_status,
    get_available_moves
)

router = APIRouter()


# Pydantic response models
class MoveModel(BaseModel):
    name: str
    type: str
    power: Optional[int]
    status_effect: Optional[str] = None


class StrategyModel(BaseModel):
    pokemon: str
    recommended_move: str
    type_advantage: List[str]


class StatusModel(BaseModel):
    pokemon: str
    hp: int
    status_condition: Optional[str] = None


class SimulationResultModel(BaseModel):
    winner: str
    log: List[str]


@router.post("/simulate", response_model=SimulationResultModel)
def simulate(pokemon1: str, pokemon2: str):
    """
    Simulate a battle between two Pokémon.
    """
    result = simulate_battle(pokemon1, pokemon2)
    return result


@router.get("/strategy/{pokemon}", response_model=StrategyModel)
def strategy(pokemon: str):
    """
    Get the recommended battle strategy for a given Pokémon.
    """
    strat = get_battle_strategy(pokemon)
    if not strat:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return strat


@router.get("/status/{pokemon}", response_model=StatusModel)
def status(pokemon: str):
    """
    Get the current battle status of the given Pokémon.
    """
    status = get_battle_status(pokemon)
    if not status:
        raise HTTPException(status_code=404, detail="Status not found")
    return status


@router.get("/moves/{pokemon}", response_model=List[MoveModel])
def moves(pokemon: str):
    """
    Get available moves for a given Pokémon.
    """
    moves = get_available_moves(pokemon)
    if not moves:
        raise HTTPException(status_code=404, detail="No moves found for this Pokémon")
    return moves

