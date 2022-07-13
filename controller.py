from game_state import GameState
from game_save import GameSave
import importlib
import random

class MafiaController():
    def __init__(self):
        pass
    
    def create_game(self, players, save: str):
        # TODO: Needs to take a a GameSave rather than simply a roles list
        print("Creating Game")
        print("Players:", len(players))
        print(players)
        
        
        game_save = GameSave(save)
        role = game_save.generate_roles()
        print(game_save.roles)
        
        # Assign roles and numbers to players
        random.shuffle(players)
        random.shuffle(game_save.roles)
        
        for index, player in enumerate(players):
            player['role'] = game_save.roles[index]
            player['number'] = index + 1
            player['house'] = index + 1

        # Sort by new numbers
        players = sorted(players, key=lambda player: player['number'])
        for player in players:
            print(player)
            
        # Generate a GameState
        print()
        actors = []
        for player in players:
            role = self.class_for_name('roles', player['role'])
            print(role(player, save['roles'][player['role']]['settings']))
            print(player['role'], save['roles'][player['role']]['settings'])
        


        
    def test_save(self, save):
        Test = GameSave(save)
        Test.generate_roles()
        return Test.roles
    
    def class_for_name(self, module_name, class_name):
        # Imports a class based on a provided string 
        # i.e ->
        #       :module_name = roles
        #       :class_name = citizen
        # Result: from roles.citizen import Citizen
        m = importlib.import_module(module_name)
        c = getattr(m, class_name)
        return c