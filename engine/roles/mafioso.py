from engine.roles import Actor
from engine.models import Player

class Mafioso(Actor):
    tags = ["any_random", "mafia_random", "mafia_killing"]
    
    def __init__(self, player: Player):
        self.player = player