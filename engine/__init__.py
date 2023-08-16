import random
from typing import List
from engine.utils.logger import logger
from engine.game_save import GameSave
from engine.game import Game

class AssConfigException(Exception):
    pass



def new_game(players: List[dict], config: dict, tries: int=5):
    games: List[Game] = []
    for i in range(tries):
        game = Game().new(players, config)
        if not game.check_for_win(): games.append(game)
    
    if games:
        # Find the game with the lowest failure rate
        games.sort(key=lambda g: len(g.failed_roles))
        return games[0]
    else:
        raise AssConfigException('Bad save idiot')

def load_game(players: List[dict], state: dict, save: dict):
    return Game().load(players, state, save)

