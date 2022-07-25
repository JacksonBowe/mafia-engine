import os
import json
import pytest
import logging

from controller import MafiaController

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+f'/test_mafioso_files/test-mafioso-actors.json', 'r') as p:
    players = json.load(p)

with open(dir_path+'/test_mafioso_files/test-mafioso-game-save.json', 'r') as s:
    save = json.load(s)

with open('test-game-state.json', 'r') as st:
    state = json.load(st)

def test_mafioso_find_allies():
    logging.info("Running test: mafioso_find_allies")
    game = MafiaController().load_game(players, save, state)

    
    for actor in game.actors:
        if actor.alias != 'Jackson': continue
        Mafioso = actor

    Mafioso.find_allies(game.actors)
    logging.info(json.dumps(Mafioso.allies, indent=4))

    # Should be 2 allies, self inclusive
    assert len(Mafioso.allies) == 2, f"{Mafioso} should only have 2 allies"

    # # Get the two ally Actors and check that their alignment is the same
    ally_numbers = [ally['number'] for ally in Mafioso.allies]
    for actor in game.actors:
        if actor.number in ally_numbers:
            assert actor.alignment == Mafioso.alignment, f"{Mafioso} incorrectly has {actor} as an ally"
    
    
def test_mafioso_find_possible_targets():
    logging.info("Running test: mafioso_find_possible_targets")
    game = MafiaController().load_game(players, save, state)
    
    for actor in game.actors:
        if actor.alias != 'Jackson': continue
        Mafioso = actor
    
    Mafioso.find_possible_targets(game.actors)
    logging.info(json.dumps(Mafioso.possible_targets, indent=4))
    
    # Should have a single list of targets [ [targets] ]
    assert len(Mafioso.possible_targets) == 1, f"Mafioso should only have 1 list of targets, has {len(Mafioso.possible_targets)}"
    
    # For all the possible targets, none of them should be allies
    for actor in game.actors:
        if actor.number in Mafioso.possible_targets[0]:
            assert actor.alignment != Mafioso.alignment, "Mafioso 'possible_targets' contains other Mafia members"
    
def test_mafioso_action_basic():
    logging.info("Running test: mafioso_action_basic")
    game = MafiaController().load_game(players, save, state)    
    
    for actor in game.actors:
        if actor.alias != 'Jackson': continue
        Mafioso = actor
        
    Mafioso.find_possible_targets(game.actors)
    
    for actor in game.actors:
        if actor.number in Mafioso.possible_targets[0]:
            Mafioso.action([actor]) # List<Actor> of targets
            assert actor.alive == False, f"Mafioso attempted to kill {actor}, but target not dead"
            break
        
    

#     game.resolve()

#     players_out = [actor.state for actor in game.actors]

#     logging.info(json.dumps(players_out, indent=4))

#     state_out = game.dump()
