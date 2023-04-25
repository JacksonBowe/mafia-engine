from engine.roles.actor import Actor
from engine.utils.logger import logger
from typing import List
from engine.consts import Alignment


class Citizen(Actor):
    def __init__(self, player: dict, settings: dict):
        super().__init__(player)
        self.role_name = "Citizen"
        self.alignment = Alignment.TOWN
        self.max_vests = settings.get('maxVests', 2)
        self.remaining_vests = settings.get('remainingVests', self.max_vests)

    def find_possible_targets(self, actors: List[Actor]=None) -> None:
        self.possible_targets = []
        if self.remaining_vests > 0:
            self.possible_targets = [[self]]