from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
import importlib

from engine.utils.logger import logger
from engine.roles.actor import Actor

import json

@dataclass
class GameState:
    day: int = 0
    actors: List[Actor] = None
    _graveyard: List[dict] = field(default_factory=list)
    
    def __init__(self) -> None:
        pass
    
    def __repr__(self) -> str:
        return json.dumps(self.json(), indent=4)
    
    def json(self) -> dict:
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
            "alias": actor.alias,
            "alive": actor.alive
        } for actor in self.actors]
    
    @property
    def graveyard(self) -> List[Actor]:
        return self._graveyard + [{
            "number": actor.number,
            "alias": actor.alias,
            "deathReason": actor.death_reason
        } for actor in self.dead_actors]
    
    def new(self, players: List[dict], roles_settings: dict) -> GameState:
        self.day = 1
        self.actors = []
        self._graveyard = []
        
        logger.info("Importing required roles and instantiating actors")
        for index, player in enumerate(players):
            Role = self._class_for_name('engine.roles', player['role'])
            # Instantiate a Role class with a :player and :roles_settings[role]
            actor = Role(player, roles_settings[player['role']])
            actor.set_number_and_house(index+1)
            self.actors.append(actor)
        
        self.generate_allies_and_possible_targets()
        return self
    
    def load(self, players: List[dict], previous_state: dict, roles_settings: dict) -> GameState:
        self.day = previous_state['day']
        self._graveyard = previous_state['graveyard']
        self.actors = []
        
        logger.info("Importing required roles and instantiating actors")
        for player in players:
            Role = self._class_for_name('engine.roles', player['role'])
            actor = Role(player, roles_settings[player['role']])
            self.actors.append(actor)
        
        self.generate_allies_and_possible_targets()
        return self
    
    def generate_allies_and_possible_targets(self) -> None:
        for actor in self.alive_actors:
            actor.find_allies(self.actors)
            actor.find_possible_targets(self.actors)
            
    

