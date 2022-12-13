from __future__ import annotations
from dataclasses import dataclass
from typing import List, Type

import importlib

from roles import Actor
from game_save2 import GameSave
from logger import logger

@dataclass
class GameState():
    day: int = 0
    
    def _class_for_name(self, module_name, class_name) -> Type[Actor]:
        '''Imports a class based on a provided string 
        i.e ->
              :module_name = roles
              :class_name = citizen
        Result: from roles.citizen import Citizen
        '''
        m = importlib.import_module(module_name)
        c = getattr(m, class_name)
        return c
    
    def from_lobby(self, players: list, roles_settings: dict) -> GameState:
        self.day = 1
        self.actors = []
        
        logger.info("Importing required roles and instantiating actos")
        for index, player in enumerate(players):
            Role = self._class_for_name('roles', player['role'])
            # Instantiate a Role class with a :player and :roles_settings[role]
            actor = Role(player, roles_settings[player['role']])
            actor.set_number_and_house(index+1)
            self.actors.append(actor)
   
        return self
    
    def from_previous(self, prev_state: dict) -> GameState:
        # TODO
        pass
    
    def generate_allies_and_possible_targets(self) -> None:
        for actor in self.alive_actors:
            actor.find_allies(self.actors)
            actor.find_possible_targets(self.actors)
            
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
    
    def dump(self) -> dict:
        return {
            "day": self.day,
            "players": self.players,
            "graveyard": self.graveyard
        }
    
    