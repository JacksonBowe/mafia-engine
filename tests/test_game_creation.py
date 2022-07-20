import os
import json
import pytest
import logging

from controller import MafiaController

logging.basicConfig(filename="log.txt",
    level=logging.DEBUG, 
    format="[%(funcName)s][%(levelname)s] \t%(message)s",
    filemode="w"
    )

@pytest.fixture
def test_init():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path+f'/test_game_creation_files/test1-input-lobby.json', 'r') as l:
        lobby = json.load(l)
        players = lobby['players']

    with open(dir_path+'/test_game_creation_files/test1-input-game-save.json', 'r') as s:
        save = json.load(s)
        
    Mafia = MafiaController()
    game = Mafia.create_game(players, save)
    
    # log("\nSaving Actors to file 'output-actors.json'...")
    with open(dir_path+'/test_game_creation_files/test1-output-actors.json', 'w') as f:
        f.write(json.dumps([actor.state for actor in game.actors], indent=4))   
        
        # log("Saving GameState to file 'output-game-state.json'...")
    with open(dir_path+'/test_game_creation_files/test1-output-game-state.json', 'w') as f:
        f.write(json.dumps(game.dump(), indent=4))

    

def test_02(test_init):
    # assert test_init == 3
    pass