import os
import logging
import json

import src.interface as Mafia


def test_create_game():
    logging.info("--- TEST: Create game ---")
    
    print(os.getcwd(), __file__, os.path)
    
    with open(f'{os.path.dirname(__file__)}\\players.json', 'r') as players:
        players = json.load(players)
        
    with open(f'{os.path.dirname(__file__)}\\save.json', 'r') as save:
        save = json.load(save)
        
    Mafia.create_game(players, save)
    
if __name__=='__main__':
    test_create_game()