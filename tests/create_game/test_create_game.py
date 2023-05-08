import os
import logging
import json
import pytest

import engine as Mafia

'''
    Tests:
        - Can we successfully create a new game
        - Are all the players assigned roles?
        - Are the roles in the game correct 
'''



def test_new_game():
    return
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
        
    game = Mafia.new_game(players, save)

    return game




    
if __name__=='__main__':
    # test_create_game()
    pass