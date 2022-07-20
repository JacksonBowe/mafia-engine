from game_state import GameState
from game_save import GameSave

import random
import json
import logging

class MafiaController():
    def __init__(self):
        pass
    

    
    def create_game(self, players, save: str):
        # TODO: Needs to take a a GameSave rather than simply a roles list
        logging.info("--- Creating Game ---")
        logging.info("Players: {}".format(len(players)))
        logging.info("Tags: {}".format(save['tags']))
        
        game_save = GameSave(save)
        game_save.generate_roles()
        logging.info("Roles: {}".format(game_save.roles))
        
        # Assign roles and numbers to players
        random.shuffle(players)
        random.shuffle(game_save.roles)
        
        # Allocate Roles
        logging.info("--- Allocating roles ---")
        for index, player in enumerate(players):
            player['role'] = game_save.roles[index]
            logging.info(f"\t--> {player['alias']} ({player['name']}):\t\t{player['role']}")
        
            
        # Generate GameState
        logging.info("--- Generating initial GameState ---")
        game_state = GameState(players, game_save)
        game_state.generate_allies_and_possible_targets()
        
        return game_state
        
        
          
            


        


        
    def test_save(self, save):
        Test = GameSave(save)
        Test.generate_roles()
        return Test.roles
    
    