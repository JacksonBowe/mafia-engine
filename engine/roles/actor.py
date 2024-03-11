from abc import ABC, abstractmethod

from engine.models import Player

class Actor(ABC):
    tags = ['any_random']
    def __init__(self, player: Player) -> None:
        self.name = 'Actor'