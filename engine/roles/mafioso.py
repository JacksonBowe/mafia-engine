from typing import List

from engine.roles import Actor, Mafia
from engine.models import Player

class Mafioso(Mafia):
    tags = ["any_random", "mafia_random", "mafia_killing"]
    
    def __init__(self, player: Player, settings: dict):
        super().__init__(player)
        self.role_name = 'Mafioso'
        
    def find_possible_targets(self, actors: List[Actor] = None) -> List[Actor]:
        # Number of targets
        num_targets = 1
        
        self.possible_targets = []
        for i in range(num_targets):
            self.possible_targets.insert(i, {
                actor for actor in actors
                if actor.alive
                and actor.alignment != self.alignment
                and actor.number != self.number # Seems a bit redundant, but can't hurt
            })
            
        return self.possible_targets