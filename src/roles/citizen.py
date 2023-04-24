from src.roles.actor import Actor
from src.utils.logger import logger
from typing import List
from src.consts import Alignment


class Citizen(Actor):
    def __init__(self, player: dict, settings: dict):
        super().__init__(player)
        self.role_name = "Citizen"
        self.alignment = Alignment.TOWN
        self.max_vests = settings.get('maxVests', 2)
        self.remaining_vests = settings.get('remainingVests', self.max_vests)