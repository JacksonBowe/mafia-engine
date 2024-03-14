from typing import List
from pydantic import BaseModel, Field

from engine.roles import Actor, Town
from engine.models import Player

from engine.utils.logger import logger

class CitizenSettings(BaseModel):
    max_vests: int = Field(default=2, alias="maxVests")

class Citizen(Town):
    tags = ["any_random", "town_random", "town_government"]
    
    def __init__(self, player: Player, settings: dict=dict()):
        super().__init__(player)
        # self.role_name = 'Citizen'
        self.settings = CitizenSettings.model_validate(settings)
        self.remaining_vests = player.role_actions.get('remainingVests', self.settings.max_vests)
        
    def dump_state(self):
        return {**super().dump_state(), **{
            "roleActions": {
                "remainingVests": self.remaining_vests
            }
        }}
        
    def find_possible_targets(self, actors: List[Actor]=None) -> None:
        self.possible_targets = []
        if self.remaining_vests > 0:
            self.possible_targets = [[self]]
        
        
    def action(self) -> None:
        if not self.remaining_vests > 0:
            logger.critical(f"{self} tried to use vest but has 0 remaining")
            return
        
        self.remaining_vests -= 1
        target = self.targets[0]
        target.night_immune = True
        logger.info(f"|{self.role_name}| {self.alias}({self.number}) used vest on {'self' if target == self else target}. {self.remaining_vests} remaining")
        