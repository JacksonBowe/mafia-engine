'''
This file houses all of the user-facing commands such as create_game, build_game, resolve_state
It is essentially the API
'''

from src.utils.logger import logger

from src.game import Game


def create_game(players, save):
    print('Creating a game yeet yeet')
    logger.info('Creating a game yeet yeet')
    
    game = Game().new(players, save)
    
    print(game)