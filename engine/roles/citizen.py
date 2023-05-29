from typing import List

import engine.roles as roles
from engine.utils.logger import logger


class Citizen(roles.Town):
    def __init__(self, player: dict, settings: dict=dict()):
        super().__init__(player)
        self.role_name = "Citizen"
        self.alignment = roles.Alignment.TOWN
        self.max_vests = settings.get('maxVests', 2)
        self.remaining_vests = player.get('remainingVests', self.max_vests)
        
    @property
    def state(self):
        # Return 'self.state' merged with 'parent.state'
        return {**super().state,**{
            "remainingVests": self.remaining_vests
        }}

    def find_possible_targets(self, actors: List[roles.Actor]=None) -> None:
        self.possible_targets = []
        if self.remaining_vests > 0:
            self.possible_targets = [[self]]
            
    def action(self) -> None:
        if not self.remaining_vests > 0:
            logger.critical(f"{self} tried to use vest but has 0 remaining")
            return
            
        self.remaining_vests -= 1
        self.night_immune = True
        logger.info(f"|{self.role_name}| {self.alias}({self.number}) used vest. {self.remaining_vests} remaining")
        