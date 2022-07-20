import os 
import json
from controller import MafiaController

TEST_NAME = "Test 1"
DESCRIPTION = '''
    Create game test
'''

        
def run():
    print(f"Running {TEST_NAME}")
    print(DESCRIPTION)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    with open(dir_path+'/test1-input-lobby.json', 'r') as l:
        lobby = json.load(l)
        players = lobby['players']

    with open(dir_path+'/test1-input-game-save.json', 'r') as s:
        save = json.load(s)
        
    Mafia = MafiaController(verbose=False)
    game = Mafia.create_game(players, save)
    
    # log("\nSaving Actors to file 'output-actors.json'...")
    with open(dir_path+'/test1-output-actors.json', 'w') as f:
        f.write(json.dumps([actor.state for actor in game.actors], indent=4))   
        
        # log("Saving GameState to file 'output-game-state.json'...")
    with open(dir_path+'/test1-output-game-state.json', 'w') as f:
        f.write(json.dumps(game.dump(), indent=4))  
    
    
    
    

    
    
    
    