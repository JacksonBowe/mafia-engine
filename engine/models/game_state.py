import json
from typing import List
from dataclasses import dataclass, field
from pydantic import BaseModel

import engine.roles as roles
from engine.utils.logger import logger

class StatePlayer(BaseModel):
    pass

class GameState(BaseModel):
    day: int = 0
    players: List = []
    graveyard: List = []
    
    