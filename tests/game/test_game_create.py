import os
import logging
import json
import pytest
import random

import engine as Mafia

def dummy_players(n):
    players = []
    for i in range(1,n+1):
        players.append({
            'id': f'user-{i}',
            'name': f'UserName{i}',
            'alias': f'UserAlias{i}'
        })
        
    return players

@pytest.fixture(scope="session")
def test_new_game() -> Mafia.Game:
    logging.info("--- TEST: New game ---")
    num_players = 3
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
    
    return game

def test_new_game_state(test_new_game: Mafia.Game):
    logging.info("--- TEST: New game state ---")
    
    game = test_new_game
    
    