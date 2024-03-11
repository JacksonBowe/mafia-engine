import random
from typing import List
from pydantic import BaseModel, ValidationError

from engine.models import Player, GameState, GameConfig
# from engine.game import Game

from engine.utils.logger import logger

def new_game(players: List[dict], config: dict):
    logger.info('--- Creating a new Game ---')
    logger.info("Players: {}".format(players))
    
    try:
        Players = [Player(**player) for player in players]
        Config = GameConfig(**config)
    except ValidationError as e:
        print(f"An error occurred while initializing the game: {e}")
        return
    
    roles, failures = Config.generate_roles()
    
    # Assign rules and numbers to players
    
    
    return

def load_game():
    pass

def validate_save():
    pass

def generate_roles():
    pass

def simulate():
    pass
