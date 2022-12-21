import os
import json

from logger import logger
import api as Mafia

def test_resolve():
    logger.debug("--- TEST: Game resolve ---")
    p = "tests/test_game_resolution/test-1/" # Basepath
    
    # -------------- Open the files --------------
    with open(p + 'input/sample-game-state.json', 'r') as pgs:
        prev_game_state = json.load(pgs)
        
    with open(p + 'input/sample-game-actors.json', 'r') as ga:
        players = json.load(ga)
        
    with open(p +'/input/test-game-save.json', 'r') as s:
        save = json.load(s)
        
    # -------------- Resolve --------------
    game = Mafia.load_game(prev_game_state, players, save)
    
    game.resolve_actions()
    
    
    # -------------- Save output --------------
    with open(p +'/output/output-actors.json', 'w') as oa:
        json.dump(game.dump_actors(), oa, indent=4)
        logger.debug("Wrote output actors to file: test-1/output/output-actors.json")
        
    with open(p +'/output/output-game-state.json', 'w') as ogs:
        json.dump(game.dump_state(), ogs, indent=4)
        logger.debug("Wrote output game state to file: test-1/output/output-game-sate")
           
    # -------------- Check --------------
    # Verify that all players start out as 'alive'
        
    # assert len(game.state['graveyard']) == 0
        
    