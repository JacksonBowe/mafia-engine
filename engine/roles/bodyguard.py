from engine.roles import Actor
from engine.models import Player

class Bodyguard(Actor):
    tags = ["any_random", "town_random", "town_protective", "town_killing"]
    def __init__(self, player: Player):
        self.player = player