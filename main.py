'''
This file houses all of the user-facing commands such as create_game, build_game, resolve_state
It is essentially the API
'''
import json
import logging
from controller import MafiaController



def main():
    logging.basicConfig(filename="log.txt",
        level=logging.DEBUG, 
        format="[%(funcName)s][%(levelname)s] \t%(message)s",
        filemode="w")

    with open('test-actors.json', 'r') as l:
        players = json.load(l)

    with open('test-game-save.json', 'r') as s:
        save = json.load(s)

    with open('test-game-state.json', 'r') as st:
        state = json.load(st)

    # apply state
    game = MafiaController().load_game(players, save, state)
    
    with open('test-actors-output.json', 'w') as f:
        f.write(json.dumps([actor.state for actor in game.actors], indent=4))   
        
        # log("Saving GameState to file 'output-game-state.json'...")
    with open('test-game-state-output.json', 'w') as f:
        f.write(json.dumps(game.dump(), indent=4))
        
        
    game.resolve()
    
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