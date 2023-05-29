import random
from typing import List
from engine.utils.logger import logger
from engine.game_save import GameSave
from engine.game import Game


def new_game(players: List[dict], config: dict):
    return Game().new(players, config)

def load_game(players: List[dict], state: dict, save: dict):
    return Game().load(players, state, save)

