from engine.roles.actor import Actor
from engine.utils.logger import logger
from typing import List
from engine.consts import Alignment

from engine.events import GameEventGroup, GameEvent, EVENTS
import engine.events as events

class Citizen(Actor):
    def __init__(self, player: dict, settings: dict):
        super().__init__(player)
        self.role_name = "Citizen"
        self.alignment = Alignment.TOWN
        self.max_vests = settings.get('maxVests', 2)
        self.remaining_vests = settings.get('remainingVests', self.max_vests)
        
    @property
    def state(self):
        # Return 'self.state' merged with 'parent.state'
        return {**super().state,**{
            "remainingVests": self.remaining_vests
        }}

    def find_possible_targets(self, actors: List[Actor]=None) -> None:
        self.possible_targets = []
        if self.remaining_vests > 0:
            self.possible_targets = [[self]]
            
    def action(self, targets: List[Actor]) -> None:
        print(targets)
        if not self.remaining_vests > 0:
            logger.critical(f"{self} tried to use vest but has 0 remaining")
            return
        
        target = targets[0]
        if target != self: # Tipple checking that Citizen is only targetting themselves
            logger.critical(f"{self.alias}({self.number}) invalid target ({targets[0].number}). {self.role_name} can only target self")
            return
            
        self.remaining_vests -= 1
        self.night_immune = True
        logger.info(f"|{self.role_name}| {self.alias}({self.number}) used vest. {self.remaining_vests} remaining")
        