from enum import Enum

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