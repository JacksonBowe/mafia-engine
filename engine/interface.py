'''
This file houses all of the user-facing commands such as create_game, build_game, resolve_state
It is essentially the API
'''

from engine.utils.logger import logger

from engine.game import Game


def create_game(players, save) -> Game:
    print('Creating a game yeet yeet')
    logger.info('Creating a game yeet yeet')
    
    return Game().new(players, save)
