from game_state import GameState
from game_save import GameSave
import importlib
import random


class MafiaEngine():
    def __init__(self):
        pass
    
    def create_game(self, players, save: str):
        # TODO: Needs to take a a GameSave rather than simply a roles list
        print("Creating Game")
        print("Players:", len(players), players)
        
        print("\nSelecting roles")
        self.GameSave = GameSave(save)
        # roles = self.select_roles()
        # print("Roles:", roles)
        # print("\n\nAssigning roles")
        
    
        