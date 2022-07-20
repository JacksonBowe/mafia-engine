from game_state import GameState
from game_save import GameSave

import random
import json

class MafiaController():
    def __init__(self, verbose: bool=False):
        self.verbose = verbose
        self.logs = ''
        pass
    
    def log(self, *args):
        if not self.verbose: return
        print(*args)
    
    def create_game(self, players, save: str):
        # TODO: Needs to take a a GameSave rather than simply a roles list
        self.log("\n--- Creating Game ---")
        self.log("Players:", len(players))
        self.log("Tags:", save['tags'])        
        
        game_save = GameSave(save)
        game_save.generate_roles()
        self.log("\nRoles:", game_save.roles)
        
        # Assign roles and numbers to players
        random.shuffle(players)
        random.shuffle(game_save.roles)
        
        # Allocate Roles
        self.log("\n--- Allocating roles ---")
        for index, player in enumerate(players):
            player['role'] = game_save.roles[index]
            self.log(f"{player['alias']} ({player['name']}): {player['role']}")
            
        # Generate GameState
        self.log("\n--- Generating initial GameState ---")
        game_state = GameState(players, game_save)
        game_state.generate_allies_and_possible_targets()
        
        return game_state
        
        
          
            


        


        
    def test_save(self, save):
        Test = GameSave(save)
        Test.generate_roles()
        return Test.roles
    
    