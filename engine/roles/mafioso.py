from engine.roles import Actor, Mafia
from engine.models import Player

class Mafioso(Mafia):
    tags = ["any_random", "mafia_random", "mafia_killing"]
    
    def __init__(self, player: Player, settings: dict):
        super().__init__(player)