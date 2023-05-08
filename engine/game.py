from __future__ import annotations
from typing import List
import random
import json

from engine.utils.logger import logger

from engine.game_save import GameSave
from engine.game_state import GameState

from engine.roles import Actor


class Game:
    def __init__(self) -> None:
        self.save: GameSave = None
        self.state = None
        self.roles: list = None
        self.failed_roles: list = None
        
    @property
    def actors(self) -> List[Actor]:
        return [actor.state for actor in self.state.actors]
          
    def new(self, players: List[dict], config: dict) -> Game:
        logger.info('--- Creating a new Game ---')
        logger.info("Players: {}".format(players))
        
        self.save = GameSave(config=config)
        self.roles, self.failed_roles =self.save.generate_roles()
        
        # Assign roles and numbers to players
        random.shuffle(players)
        random.shuffle(self.save.roles)
        
        # Allocate roles
        logger.info("--- Allocating roles ---")
        for index, player in enumerate(players):
            player['role'] = self.save.roles[index]
            logger.info(f"  |-> {player['alias']} ({player['name']}):".ljust(40) + f" {player['role']}")
        
        # Generate GameState
        logger.info("--- Generating initial GameState ---")
        self.state = GameState().new(players, self.save.roles_settings)
        
        return self
    
    def load(self, players, state, config) -> Game:
        logger.info('--- Loading Game ---')
        logger.info("Players: {}".format(players))
        logger.info("GameState: {}".format(state))
        
        self.save = GameSave(config=config)
        
        # Generate GameState
        self.state = GameState().load(players, state, self.save.roles_settings)
        
        return self
    
    def dump_state(self) -> dict:
        return self.state.json()
        