from __future__ import annotations
from enum import Enum
from typing import List
from abc import ABC, abstractmethod

from engine.models import Player

class Actor(ABC):
    tags = ['any_random']
    def __init__(self, player: Player) -> None:
        self.name = 'Actor'
        self.player = player
        self.alias = player.alias
        self.number = player.number
        self.alive = player.alive
        
        
        self.algnment = None
    
    @property
    def role_name(self) -> str:
        return self.__class__.__name__
          
    def __repr__(self) -> str:
        return f"|{self.role_name}| {self.alias}({self.number})"
    
    def find_allies(self, actors: List[Actor] = None) -> List[Actor] | None:
        self.allies = []
        return self.allies
    
    def find_possible_targets(self, actors: List[Actor] = None) -> List[Actor] | None:
        self.possible_targets = []
        return self.possible_targets
        
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
        
    def check_for_win(self):
        pass