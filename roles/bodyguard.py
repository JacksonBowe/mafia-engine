from roles.actor import Actor
from typing import List
import logging

class Bodyguard(Actor):
    def __init__(self, player: dict=dict(), settings: dict=dict()):
        super().__init__(player)
        self.role_name = "Bodyguard"
        self.alignment = "Town"
    
    def _find_possible_targets(self, actors):
        num_targets = 1
        self.possible_targets = []
        for i in range(num_targets):
            self.possible_targets.insert(i, [
                actor for actor in actors
                if actor.alive
                and actor.number != self.number
            ])

    def _action(self, targets: List[Actor]=[]):
        if not targets: return
        target = targets[0]
        logging.info(f"{self} will protect {target} tonight")
        target.bodyguards.append(self)

    

    

        

        
        
        