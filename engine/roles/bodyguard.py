from engine.roles import Actor, Town
from engine.models import Player

class Bodyguard(Town):
    tags = ["any_random", "town_random", "town_protective", "town_killing"]
    
    def __init__(self, player: Player, settings: dict):
        super().__init__(player)
        # self.role_name = "Bodyguard"