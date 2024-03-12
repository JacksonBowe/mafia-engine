import random
from typing import List
from pydantic import BaseModel, ValidationError

from engine.models import Player, GameState, GameConfig
from engine.game import Game

from engine.utils.logger import logger

def new_game(players: List[dict], config: dict, tries=1):
    try:
        Players = [Player(**player) for player in players]
        Config = GameConfig(**config)
    except ValidationError as e:
        print(f"An error occurred while initializing the game: {e}")
        return
    
    for i in range(tries):
        game = Game.new(Players, Config)
 
    return game

def load_game(players: List[dict], config: dict, state: dict):
    
    
    try:
        Players = [Player(**player) for player in players]
        Config = GameConfig(**config)
        State = GameState(**state)
    except ValidationError as e:
        print(f"An error occurred while initializing the game: {e}")
        return
    
    
    
     
    game = Game.load(Players, Config, State)
    
    
    return game


def validate_config():
    pass

def generate_roles():
    pass

def simulate():
    pass
