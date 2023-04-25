import os
import logging
import json

import engine.interface as Mafia


def test_create_game():
    ''' 
        Create a new game and verify the following in the output:
            1. 
    '''
    logging.info("--- TEST: Create game ---")
    
    print(os.getcwd(), __file__, os.path)
    
    with open(f'{os.path.dirname(__file__)}\\players.json', 'r') as players:
        players = json.load(players)
        
    with open(f'{os.path.dirname(__file__)}\\save.json', 'r') as save:
        save = json.load(save)
        
    game = Mafia.create_game(players, save)

    output = game.

    # A game has been created. Now need to verify the following
    # 1. Have all players been created successfully
    #   - Do they each have a role


    
if __name__=='__main__':
    test_create_game()