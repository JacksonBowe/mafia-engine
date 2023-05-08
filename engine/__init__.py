import random
from typing import List
from engine.utils.logger import logger
from engine.game_save import GameSave
from engine.game import Game



# def generate_roles(save: dict) -> GameSave:
#     game_save = GameSave(save)

#     return game_save.generate_roles()

# def assign_roles(players: dict, roles):
#     # Assign roles and numbers to players
#     random.shuffle(players)
#     random.shuffle(roles)
    
#     # Allocate roles
#     logger.info("--- Allocating roles ---")
#     for index, player in enumerate(players):
#         player['role'] = roles[index]
#         logger.info(f"  |-> {player['alias']} ({player['name']}):".ljust(40) + f" {player['role']}")

#     return players

def new_game(players: List[dict], config: dict):
    return Game().new(players, config)

def load_game(players: List[dict], state: dict, save: dict):
    return Game().load(players, state, save)

