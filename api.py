'''
This file houses all of the user-facing commands such as create_game, build_game, resolve_state
It is essentially the API
'''
import json
import logging
import random
from game import Game
from game_state import GameState
from game_save import GameSave

# logging.basicConfig(filename="log.txt",
#         level=logging.DEBUG, 
#         format="[%(funcName)-15s][%(levelname)-8s] %(message)s",
#         filemode="w")


# def create_game(players: list, save: dict):
#     logging.info("--- Creating Game ---")
#     logging.info("Players: {}".format(len(players)))
#     logging.info("Tags: {}".format(save['tags']))
    
#     # Parse the save file and generate starting roles
#     game_save = GameSave(save)
#     roles, failed_roles = game_save.generate_roles()
#     logging.info("Roles: {}".format(game_save.roles))
    
#     # Assign roles and numbers to players
#     random.shuffle(players)
#     random.shuffle(game_save.roles)
    
#     # Allocate Roles
#     logging.info("--- Allocating roles ---")
#     for index, player in enumerate(players):
#         player['role'] = game_save.roles[index]
#         logging.info(f"\t--> {player['alias']} ({player['name']}):\t\t{player['role']}")
    
        
#     # Generate GameState
#     logging.info("--- Generating initial GameState ---")
#     game_state = GameState()
#     game_state.new(players, game_save)
#     game_state.generate_allies_and_possible_targets()
    
#     return game_state


# def resolve_state(players: list, save: dict(), state: dict()):
#     logging.info("--- Resolving GameState ---")
    
#     random.shuffle(players)
    
#     # Load the supplied state
#     game_state = GameState()
#     game_save = GameSave(save)
#     game_state.load(players, game_save, game_save)
    
#     # Resolve it
#     game_state.resolve()
    
#     # Dump the result
#     new_state = game_state.dump()
#     return new_state

def create_game(players, save):
    game = Game().new(players, save)
    
    return game
    
def load_game():
    pass
