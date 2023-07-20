from typing import List
from dataclasses import dataclass

import engine.roles as roles
from engine.utils.logger import logger

@dataclass
class CitizenSettings:
    max_vests: int = 2
    
    def __init__(self, settings: dict=dict()) -> None:
        self.max_vests = settings.get('maxVests', self.max_vests)
        pass


class Citizen(roles.Town):
    def __init__(self, player: dict, settings: dict=dict()):
        super().__init__(player)
        self.role_name = "Citizen"
        self.settings = CitizenSettings(settings)
        self.remaining_vests = player.get('remainingVests', self.settings.max_vests)
        
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
        
    def check_for_win(self, actors: List[roles.Actor]) -> bool:
        # Check if the faction has won
        faction_win = super().check_for_win(actors)
        if faction_win: return faction_win

        # Check if role has won via special conditions
        if len(actors) == 2:
            return True # Citizen wins ties
        
        return False
