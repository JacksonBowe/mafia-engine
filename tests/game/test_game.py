import os
import logging
import json
import pytest
import random

from typing import Tuple, List

import engine as Mafia

def dummy_players(n) -> List[dict]:
    players = []
    for i in range(1,n+1):
        players.append({
            'id': f'user-{i}',
            'name': f'UserName{i}',
            'alias': f'UserAlias{i}'
        })
        
    return players

@pytest.fixture(scope="session")
def test_new_game() -> Tuple[List[dict], dict, Mafia.Game]:
    logging.info("--- TEST: New game ---")
    num_players = 15
    players = dummy_players(num_players)
    
    config = {
        "tags": [
            "town_government", 
            "town_protective", 
            "town_protective", 
            "town_power", 
            "town_investigative", 
            "town_killing", 
            "town_investigative", 
            "town_random", 
            "mafia_killing",
            "mafia_deception",
            "mafia_support",
            "neutral_evil",
            "neutral_benign",
            "neutral_random",
            "any_random"
        ],
        "settings": {},
        "roles": {
            "Citizen": {
                "max": 1,
                "weight": 1,
                "settings": {
                    "maxVests": 2
                }
            },
            # "Mayor": {
            #     "max": 0,
            #     "weight": 1,
            #     "settings": {}
            # },
            # "Doctor": {
            #     "max": 3,
            #     "weight": 1,
            #     "settings": {}
            # },
            "Bodyguard": {
                "max": 1,
                "weight": 1,
                "settings": {}
            },
            # "Escort": {
            #     "max": 0,
            #     "weight": 1,
            #     "settings": {}
            # },
            # "Sheriff": {
            #     "max": 0,
            #     "weight": 1,
            #     "settings": {}
            # },
            # "Investigator": {
            #     "max": 0,
            #     "weight": 1,
            #     "settings": {}
            # },
            # "Detective": {
            #     "max": 3,
            #     "weight": 1,
            #     "settings": {}
            # },
            "Mafioso": {
                "max": 3,
                "weight": 1,
                "settings": {}
            },
            # "Consort": {
            #     "max": 0,
            #     "weight": 1,
            #     "settings": {}
            # },
            # "Janitor": {
            #     "max": 0,
            #     "weight": 1,
            #     "settings": {}
            # },
            # "Survivor": {
            #     "max": 0,
            #     "weight": 1,
            #     "settings": {}
            # },
            # "SerialKiller": {
            #     "max": 0,
            #     "weight": 1,
            #     "settings": {}
            # }
        }
    }
    
    game = Mafia.new_game(players, config)
    
    assert game is not None
    assert len(game.graveyard) == 0
    assert len(game.actors) == num_players
    
    assert len(game.events.events) == 0, "Game's should start with no events"
    
    return players, config, game

def test_new_game_dump_actors(test_new_game: Tuple[List[dict], dict, Mafia.Game]):
    logging.info("--- TEST: New game dump actors ---")
    players, config, game = test_new_game
    
    actors_state = [actor.dump_state() for actor in game.actors]
    
    assert len(actors_state) == len(players)

@pytest.fixture(scope='session')
def test_new_game_dump_state(test_new_game: Tuple[List[dict], dict, Mafia.Game]) -> Tuple[List[dict], dict, dict]:
    logging.info("--- TEST: New game dump state ---")
    
    players, config, game = test_new_game
    
    game_state = game.dump_state()
    actors_state = [actor.dump_state() for actor in game.actors]
    
    # Test the GameState
    assert game_state['day'] == 1
    assert len(game_state['graveyard']) == 0
    assert len(game_state['players']) == len(game.actors)
    
    for player in game_state['players']:
        actor = game.get_actor_by_number(player['number'])
        assert actor
        assert player['alive'] == actor.alive
        
    return actors_state, config, game_state

def test_game_load(test_new_game_dump_state: Tuple[List[dict], dict, dict]):
    logging.info("--- TEST: Load game ---")
    
    players, config, state = test_new_game_dump_state
    
    print(players)
    
    game = Mafia.load_game(players, config, state)
    
    assert len(game.actors) == len(players)
    
    