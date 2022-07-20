import os 
import json
import logging
from tests.Test import Test
from controller import MafiaController

TEST_NAME = "Test 1"
DESCRIPTION = '''
    Create game test
'''

class TestCase(Test):
    def __init__(self, name=TEST_NAME) -> None:
        super().__init__(name)

    def check(self):
        try: 
            assert 1 == yes
            return super().success()
        except Exception as e:
            logging.exception(str(e))
            return super().fail()
            
    def _run(self):
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
        
        with open(dir_path+'/test1-input-lobby.json', 'r') as l:
            lobby = json.load(l)
            players = lobby['players']

        with open(dir_path+'/test1-input-game-save.json', 'r') as s:
            save = json.load(s)
            
        Mafia = MafiaController()
        game = Mafia.create_game(players, save)
        
        # log("\nSaving Actors to file 'output-actors.json'...")
        with open(dir_path+'/test1-output-actors.json', 'w') as f:
            f.write(json.dumps([actor.state for actor in game.actors], indent=4))   
            
            # log("Saving GameState to file 'output-game-state.json'...")
        with open(dir_path+'/test1-output-game-state.json', 'w') as f:
            f.write(json.dumps(game.dump(), indent=4))
          
        self.check()  
        # print(("Passed" if check() else "Failed").ljust(60, ' '), sep= ' ', end=" ", flush=True)
        # print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
        
        
    
    
    
    

    
    
    
    