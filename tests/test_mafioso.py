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
    game = MafiaController().load_game(players, save, state)

    
    for actor in game.actors:
        if actor.alias != 'Jackson': continue
        Mafioso = actor

    Mafioso.find_allies(game.actors)
    logging.info(json.dumps(Mafioso.allies, indent=4))

    # Should be 2 allies, self inclusive
    assert len(Mafioso.allies) == 2

    # # Get the two ally Actors and check that their alignment is the same
    ally_numbers = [ally['number'] for ally in Mafioso.allies]
    for actor in game.actors:
        if actor.number in ally_numbers:
            assert actor.alignment == Mafioso.alignment
    
    
# def test_mafioso_kill_basic():
#     logging.info("Running test: test_mafioso_kill_basic")


#     game = MafiaController().load_game(players, save, prev_state)
#     game.generate_allies_and_possible_targets()

#     game.resolve()

#     players_out = [actor.state for actor in game.actors]

#     logging.info(json.dumps(players_out, indent=4))

#     state_out = game.dump()
