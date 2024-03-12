import json
from typing import List
from dataclasses import dataclass, field
from pydantic import BaseModel

from engine.roles import Actor
from engine.utils.logger import logger

class StatePlayer(BaseModel):
    number: int
    alias: str
    alive: bool

class StateGraveyardRecord(BaseModel):
    number: int
    alias: str
    cod: str
    dod: int
    role: str
    will: str
class GameState(BaseModel):
    day: int = 0
    players: List = []
    graveyard: List = []
    
    