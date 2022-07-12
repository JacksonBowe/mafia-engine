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
            player['role'] = game_save.roles[index][1]
            player['number'] = index + 1
            player['house'] = index + 1

        # Sort by new numbers
        players = sorted(players, key=lambda player: player['number'])
        for player in players:
            print(player)
            
        # Generate a GameState
        actors = []
        for player in players:
            

        
    def test_save(self, save):
        Test = GameSave(save)
        Test.generate_roles()
        return Test.roles