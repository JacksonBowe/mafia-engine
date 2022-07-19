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
        game_save.generate_roles()
        print("\nRoles:", game_save.roles)
        
        # Assign roles and numbers to players
        random.shuffle(players)
        random.shuffle(game_save.roles)
        
        # Allocate Roles
        print("\n--- Allocating roles ---")
        for index, player in enumerate(players):
            player['role'] = game_save.roles[index]
            print(f"{player['alias']} ({player['name']}): {player['role']}")
            
        # Generate GameState
        print("\n--- Generating initial GameState ---")
        game_state = GameState(players, game_save)
        game_state.generate_allies_and_possible_targets()
        
        
        print("\nSaving Actors to file 'output-actors.json'...")
        with open('output-actors.json', 'w') as f:
            f.write(json.dumps([actor.state for actor in game_state.actors], indent=4))   
        
        print("Saving GameState to file 'output-game-state.json'...")
        with open('output-game-state.json', 'w') as f:
            f.write(json.dumps(game_state.dump(), indent=4))    
            


        


        
    def test_save(self, save):
        Test = GameSave(save)
        Test.generate_roles()
        return Test.roles
    
    