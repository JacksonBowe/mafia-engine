from game_state import GameState
from game_save import GameSave

import random
import json

class MafiaController():
    def __init__(self):
        pass
    
    def create_game(self, players, save: str):
        # TODO: Needs to take a a GameSave rather than simply a roles list
        print("\n--- Creating Game ---")
        print("Players:", len(players))
        print("Tags:", save['tags'])        
        
        game_save = GameSave(save)
        role = game_save.generate_roles()
        print("\nRoles:", game_save.roles)
        
        # Assign roles and numbers to players
        random.shuffle(players)
        random.shuffle(game_save.roles)
        
        # Allocate Roles
        print("\n--- Allocating roles ---")
        for index, player in enumerate(players):
            player['role'] = game_save.roles[index]
            print(f"{player['state']['alias']} ({player['name']}): {player['role']}")
            
        # Generate GameState
        game_state = GameState(players, game_save)
        
        print(json.dumps(game_state.dump_state(), indent=4))
            
            
        


        
    def test_save(self, save):
        Test = GameSave(save)
        Test.generate_roles()
        return Test.roles
    
    