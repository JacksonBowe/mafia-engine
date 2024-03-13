from __future__ import annotations
from enum import Enum
from typing import List
from abc import ABC, abstractmethod

from engine.models import Player

class Actor(ABC):
    tags = ['any_random']
    def __init__(self, player: Player) -> None:
        self.role_name = 'Actor'
        self.name = 'Actor'
        self.alignment = None
        
        self.player = player
        self.alias = player.alias
        self.number = player.number
        self.alive = player.alive
        
        self.allies: List[Actor] = []
        self.possible_targets: List[List[Actor]] = []
    
    # @property
    # def role_name(self) -> str:
    #     return self.__class__.__name__
    
    def dump_state(self):
        # print(self)
        # Returns the base player used to construct the Actor, and some actor fields
        return {**self.player.model_dump(by_alias=True),**{
            'number': self.number,
            # 'house': self.house,
            'alive': self.alive,
            'possibleTargets': [ # self.possible_targets is a list of lists [[], []]. Need to loop through the internal lists and convert the actors to just their numbers
                [ actor.number for actor in pos_targets_list]
                for pos_targets_list in self.possible_targets],
            'targets': [],
            'allies': [{
                "alias": ally.alias,
                "number": ally.number,
                "role": ally.role_name,
                "alive": ally.alive
                } for ally in self.allies],
            'alias': self.alias,
            # 'events': self.events
        }}
          
    def __repr__(self) -> str:
        return f"|{self.role_name}| {self.alias}({self.number})"
    
    def find_allies(self, actors: List[Actor] = None) -> List[Actor] | None:
        self.allies = []
        return self.allies
    
    def find_possible_targets(self, actors: List[Actor] = None) -> List[Actor] | None:
        self.possible_targets = []
        return self.possible_targets
    
    def set_targets(self, targets: List[Actor]):
        self.targets = targets
        
    def clear_targets(self) -> None:
        self.targets = []
        
class Alignment(Enum):
    TOWN = "Town"
    MAFIA = "Mafia"
    
class Town(Actor):
    def __init__(self, player: Player) -> None:
        super().__init__(player)
        self.alignment = Alignment.TOWN
        
    def check_for_win(self):
        pass
    
class Mafia(Actor):
    def __init__(self, player: Player) -> None:
        super().__init__(player)
        self.alignment = Alignment.MAFIA
        
    def find_allies(self, actors: List[Actor] = []) -> List[Actor]:
        self.allies = [actor for actor in actors if actor.alignment == self.alignment]
        
    def check_for_win(self):
        pass