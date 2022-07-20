import importlib
import logging
from os import listdir

'''
This file houses all of the user-facing commands such as create_game, build_game, resolve_state
It is essentially the API
'''

# from tests.Test1 import test

    
    
    
def class_for_name(module_name, class_name):
        # Imports a class based on a provided string 
        # i.e ->
        #       :module_name = roles
        #       :class_name = citizen
        # Result: from roles.citizen import Citizen
        m = importlib.import_module(module_name)
        c = getattr(m, class_name)
        return c
    
# def run_tests():
    


def main():
    logging.basicConfig(filename="log.txt",
        level=logging.DEBUG, 
        format="[%(funcName)s][%(levelname)s] \t%(message)s",
        filemode="w")
    for test_dir in listdir('tests'):
        if test_dir.endswith('.py'): continue
        for file in listdir(f"tests/{test_dir}"):
            if file == "test.py":
                TestCase = class_for_name(f"tests.{test_dir}.{file.replace('.py', '')}", 'TestCase')
                # test = class_for_name(f"tests.{test_dir}", file.replace('.py', ''))
                test = TestCase()
                test.run()
                
   
    
    # Test1(game)
    
    # test1.run()
    
    
    
    
    
    
    
    # print(Mafia.test_save(save))
    # Mafia = MafiaEngine()
    # game = Mafia.create_game(players=players, roles=roles)
    # print("\nPrinting GameState")
    # print(json.dumps(game, indent=4))
    pass






if __name__ == "__main__":
    main()






'''
Game Builder:
    This should take in a GameSave and a PlayerList, the output should be a GameState

GameState:
    This object should represent the complete state of a game
    {
        day: int,
        actors: [
            {
                number: int,
                userid: str,
                nickname: str,
                role: str (to be converted to object on Game.ResolveState)
                target: [] (can be a list in event of two-target night actions),
                house: int (what house is the actor at on this night),
            
            }
        ], ...
    }
'''