from engine.roles import Actor
from engine.models import Player

class Citizen(Actor):
    tags = ["any_random", "town_random", "town_government"]
    def __init__(self, player: Player):
        self.player = player