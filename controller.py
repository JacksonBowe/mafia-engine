from game_state import GameState
from game_save import GameSave

import random
import json
import logging

class MafiaController():
    def __init__(self):
        self.game_state = None
        self.game_save = None
        pass
    

    
    def create_game(self, players, save: str):
        # TODO: Needs to take a a GameSave rather than simply a roles list
        logging.info("--- Creating Game ---")
        logging.info("Players: {}".format(len(players)))
        logging.info("Tags: {}".format(save['tags']))
        
        self.game_save = GameSave(save)
        self.game_save.generate_roles()
        logging.info("Roles: {}".format(self.game_save.roles))
        
        # Assign roles and numbers to players
        random.shuffle(players)
        random.shuffle(self.game_save.roles)
        
        # Allocate Roles
        logging.info("--- Allocating roles ---")
        for index, player in enumerate(players):
            player['role'] = self.game_save.roles[index]
            logging.info(f"\t--> {player['alias']} ({player['name']}):\t\t{player['role']}")
        
            
        # Generate GameState
        logging.info("--- Generating initial GameState ---")
        self.game_state = GameState()
        self.game_state.new(players, self.game_save)
        self.game_state.generate_allies_and_possible_targets()
        
        return self.game_state

    def load_game(self, players, save, prev_state):
        logging.info("--- Loading Game ---")
        
        random.shuffle(players)
        
        # Load the previous state
        self.game_state = GameState()
        self.game_state.load(players, GameSave(save), prev_state)
        
        # random.shuffle(players)
        # for (player, actor) in zip(players, self.game_state.actors):
        #     # WHen GameState is initialised it treats players as if they were just created, need to make it not do that
        #     print(f"{player['alias']}: {player['number']} --> {actor.alias}: {actor.number}")
            
        # for actor in game_state.actors:
            
        
        # print(json.dumps([actor.state for actor in self.game_state.actors], indent=4))
        return self.game_state




        
        
        
        
        
          
            


        


        
    def test_save(self, save):
        Test = GameSave(save)
        Test.generate_roles()
        return Test.roles
    
    