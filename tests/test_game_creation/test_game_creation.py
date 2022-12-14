import os
import json

from logger import logger
import api as Mafia

def test_create_game():
    logger.debug(" --- TEST: Create game ---")
    p = "tests/test_game_creation/test-1/" # Basepath
    
    with open(p + 'input/input-lobby.json', 'r') as lobby:
        players = json.load(lobby)['players']
        
    with open(p +'/input/input-game-save.json', 'r') as s:
        save = json.load(s)
        
    game = Mafia.create_game(players, save)
    
    logger.debug(f"Game: {game}")
    
    with open(p +'/output/output-actors.json', 'w') as oa:
        json.dump(game.actors, oa, indent=4)
        logger.debug("Wrote output actors to file: test-1/output/output-actors.json")
        
    with open(p +'/output/output-game-state.json', 'w') as ogs:
        json.dump(game.state, ogs, indent=4)
        logger.debug("Wrote output game state to file: test-1/output/output-game-sate")
        
    # Verify that all players start out as 'alive'
    for player in game.state['players']:
        assert player['alive'] == True
        
    for actor in game.actors:
        assert actor['alive'] == True
        
    assert len(game.state['graveyard']) == 0
        
    