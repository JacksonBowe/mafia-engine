from __future__ import annotations
from typing import List

class Actor:
    def __init__(self, player: dict):
        self.alias = player.get('alias', None)
        self.player = player
        self.number = player.get('number', None)
        self.role_name = 'Actor'
        self.house = None
        self.alive = player.get('alive', True)
        self.visitors: List[Actor] = []
        self.possible_targets: List[Actor] = []
        self.allies: List[Actor] = []
        self.death_reason = None
        
    def __repr__(self) -> str:
        return f"|{self.role_name}| {self.alias}({self.number})"
    
    def set_number_and_house(self, number: int) -> None:
        self.number = number
    
    def find_allies(self, actors: List[Actor]=None) -> None:
        self.allies = []
        return self.allies
    
    def find_possible_targets(self, actors: List[Actor]=None) -> None:
        self.possible_targets = []
        return self.possible_targets
    
    
        
    