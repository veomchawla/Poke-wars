import random
from typing import List, Dict, Optional


# Define type effectiveness chart
TYPE_EFFECTIVENESS = {
    'electric': {'water': 2.0, 'flying': 2.0, 'ground': 0.0},
    'water': {'fire': 2.0, 'electric': 0.5, 'grass': 0.5},
    'fire': {'grass': 2.0, 'water': 0.5},
    'grass': {'water': 2.0, 'fire': 0.5},
    'ground': {'electric': 2.0, 'fire': 2.0},
    'flying': {'grass': 2.0}
}

# Mock Pokémon data
POKEMON_DATABASE = {
    'pikachu': {
        'type': 'electric',
        'hp': 100,
        'moves': [
            {'name': 'Thunderbolt', 'type': 'electric', 'power': 40, 'status_effect': 'paralysis'},
            {'name': 'Quick Attack', 'type': 'normal', 'power': 20}
        ]
    },
    'charmander': {
        'type': 'fire',
        'hp': 100,
        'moves': [
            {'name': 'Ember', 'type': 'fire', 'power': 30, 'status_effect': 'burn'},
            {'name': 'Scratch', 'type': 'normal', 'power': 20}
        ]
    },
    'squirtle': {
        'type': 'water',
        'hp': 100,
        'moves': [
            {'name': 'Water Gun', 'type': 'water', 'power': 35},
            {'name': 'Tackle', 'type': 'normal', 'power': 20}
        ]
    },
    'bulbasaur': {
        'type': 'grass',
        'hp': 100,
        'moves': [
            {'name': 'Vine Whip', 'type': 'grass', 'power': 35, 'status_effect': 'poison'},
            {'name': 'Tackle', 'type': 'normal', 'power': 20}
        ]
    }
}


def type_multiplier(move_type: str, target_type: str) -> float:
    return TYPE_EFFECTIVENESS.get(move_type, {}).get(target_type, 1.0)


def apply_status_effect(status: Optional[str], target: Dict) -> str:
    if status == 'burn':
        target['hp'] -= 5
        return f"{target['name']} is burned and loses 5 HP!"
    elif status == 'poison':
        target['hp'] -= 5
        return f"{target['name']} is poisoned and loses 5 HP!"
    elif status == 'paralysis':
        if random.random() < 0.25:
            return f"{target['name']} is paralyzed and cannot move!"
    return ""


def simulate_battle(pokemon1: str, pokemon2: str) -> Dict:
    log = []
    p1 = POKEMON_DATABASE.get(pokemon1.lower())
    p2 = POKEMON_DATABASE.get(pokemon2.lower())

    if not p1 or not p2:
        return {'winner': 'None', 'log': ['One or both Pokémon not found.']}

    p1 = p1.copy()
    p2 = p2.copy()
    p1['name'] = pokemon1
    p2['name'] = pokemon2

    p1_status = None
    p2_status = None

    while p1['hp'] > 0 and p2['hp'] > 0:
        for attacker, defender, attacker_status in [(p1, p2, p2_status), (p2, p1, p1_status)]:
            if defender['hp'] <= 0:
                break

            move = random.choice(attacker['moves'])
            move_power = move.get('power', 0)
            multiplier = type_multiplier(move['type'], defender['type'])
            damage = int(move_power * multiplier)
            defender['hp'] -= damage
            defender['hp'] = max(0, defender['hp'])

            log.append(f"{attacker['name']} used {move['name']}! It's {'super effective' if multiplier > 1 else 'not very effective' if multiplier < 1 else 'effective'} ({damage} damage). {defender['name']} has {defender['hp']} HP left.")

            if 'status_effect' in move:
                status_message = apply_status_effect(move['status_effect'], defender)
                if status_message:
                    log.append(status_message)
                    if attacker == p1:
                        p2_status = move['status_effect']
                    else:
                        p1_status = move['status_effect']

            if 'status_effect' in move and move['status_effect'] == 'paralysis':
                if random.random() < 0.25:
                    log.append(f"{defender['name']} is paralyzed and misses their turn!")

    winner = p1['name'] if p1['hp'] > 0 else p2['name']
    return {'winner': winner, 'log': log}


def get_battle_strategy(pokemon: str) -> Optional[Dict]:
    poke = POKEMON_DATABASE.get(pokemon.lower())
    if not poke:
        return None

    recommended_move = max(poke['moves'], key=lambda m: m.get('power', 0))
    type_adv = TYPE_EFFECTIVENESS.get(poke['type'], {}).keys()
    return {
        'pokemon': pokemon,
        'recommended_move': recommended_move['name'],
        'type_advantage': list(type_adv)
    }


def get_battle_status(pokemon: str) -> Optional[Dict]:
    poke = POKEMON_DATABASE.get(pokemon.lower())
    if not poke:
        return None

    return {
        'pokemon': pokemon,
        'hp': poke['hp'],
        'status_condition': None
    }


def get_available_moves(pokemon: str) -> Optional[List[Dict]]:
    poke = POKEMON_DATABASE.get(pokemon.lower())
    if not poke:
        return None
    return poke['moves']


