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
        self.possible_targets: List[List[Actor]] = []
        self.allies: List[Actor] = []
        self.death_reason = None
        
    def __repr__(self) -> str:
        return f"|{self.role_name}| {self.alias}({self.number})"
    
    @property
    def state(self):
        # print(self)
        # Returns the base player used to construct the Actor, and some actor fields
        return {**self.player,**{
            'number': self.number,
            # 'house': self.house,
            'alive': self.alive,
            'possible_targets': [ # self.possible_targets is a list of lists [[], []]. Need to loop through the internal lists and convert the actors to just their numbers
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
    
    def set_number_and_house(self, number: int) -> None:
        self.number = number
    
    def find_allies(self, actors: List[Actor]=None) -> None:
        self.allies = []
        return self.allies
    
    def find_possible_targets(self, actors: List[Actor]=None) -> None:
        self.possible_targets = []
        return self.possible_targets
    
    
        
    