from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Type

import importlib

from roles import Actor
from consts import TURN_ORDER
from logger import logger

@dataclass
class GameState():
    day: int = 0
    actors: List[Actor] = field(default_factory=list)
    
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
    
        self.generate_allies_and_possible_targets()

        return self
    
    def from_previous(self, prev_state: dict, players: list, roles_settings: dict()) -> GameState:
        self.day = prev_state['day']
        self.actors = []
        
        logger.info("Converting players to Actors")
        for player in players:
            Role = self._class_for_name('roles', player['role'])
            # Instantiate a Role class with a :player and :roles_settings[role]
            actor = Role(player, roles_settings[player['role']])
            self.actors.append(actor)
            
        return self
    
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
        
    def get_actor_by_number(self, number):
        for actor in self.actors:
            if actor.number == number:
                return actor
        
    def resolve(self):
        self.day += 1
        
        self.generate_allies_and_possible_targets() # As a precaution
        
        # sort the actors based on TURN_ORDER
        self.actors.sort(key=lambda actor: TURN_ORDER.index(actor.role_name))
        
        for actor in self.actors:
            if not actor.targets: continue
            logger.info(f"|{actor.role_name}| {actor.alias}({actor.number}) is targetting {actor.targets}")
            
            # The targets are just numbers, need to find associated Actors
            targets = [self.get_actor_by_number(target) for target in actor.targets]
            
            # Create a new GameEventGroup. This will get p
            
    
    def dump(self) -> dict:
        return {
            "day": self.day,
            "players": self.players,
            "graveyard": self.graveyard
        }
    
    