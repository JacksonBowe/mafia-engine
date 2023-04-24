from __future__ import annotations
from typing import List
import importlib

from src.utils.logger import logger
from src.roles.actor import Actor

import json

class GameState:
    day: int = 0
    actors: List[Actor] = None
    
    def __init__(self) -> None:
        pass
    
    def __repr__(self) -> str:
        return json.dumps(self.json(), indent=4)
    
    def json(self) -> str:
        return {
            "day": self.day,
            "players": self.players,
            "graveyard": self.graveyard
        }
    
    def _class_for_name(self, module_name, class_name) -> Actor:
        '''Imports a class based on a provided string 
        i.e ->
              :module_name = roles
              :class_name = citizen
        Result: from roles.citizen import Citizen
        '''
        m = importlib.import_module(module_name)
        c = getattr(m, class_name)
        return c
    
    @property
    def alive_actors(self) -> List[Actor]:
        return [actor for actor in self.actors if actor.alive]
    
    @property
    def dead_actors(self) -> List[Actor]:
        return [actor for actor in self.actors if not actor.alive]
    
    @property
    def players(self) -> List[Actor]:
        return [{
            "number": actor.number,
            "name": actor.alias,
            "alive": actor.alive
        } for actor in self.actors]
    
    @property
    def graveyard(self) -> List[Actor]:
        return [{
            "number": actor.number,
            "alias": actor.alias,
            "deathReason": actor.death_reason
        } for actor in self.dead_actors]
    
    def new(self, players: List[dict], roles_settings: dict) -> GameState:
        self.day = 1
        self.actors = []
        
        logger.info("Importing required roles and instantiating actors")
        for index, player in enumerate(players):
            Role = self._class_for_name('src.roles', player['role'])
            # Instantiate a Role class with a :player and :roles_settings[role]
            actor = Role(player, roles_settings[player['role']])
            actor.set_number_and_house(index+1)
            self.actors.append(actor)
    
        self.generate_allies_and_possible_targets()
        
        return self
    
    def generate_allies_and_possible_targets(self) -> None:
        for actor in self.alive_actors:
            actor.find_allies(self.actors)
            actor.find_possible_targets(self.actors)
            
    

