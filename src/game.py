from __future__ import annotations
from typing import List

from src.utils.logger import logger


class Game:
    def __init__(self) -> None:
        self.save = None
        self.state = None
        
    def new(self, players: List[dict], save: dict) -> Game:
        logger.info('--- Creating a new Game ---')
        logger.info("Players: {}".format(players))
        
        self.save = save
        
        return self
        