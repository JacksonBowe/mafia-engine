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

def test_new_game():
    logging.info("--- TEST: New game ---")