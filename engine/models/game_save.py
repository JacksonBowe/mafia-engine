from typing import List
from pydantic import BaseModel

class SaveSettings(BaseModel):
    pass

class GameSave(BaseModel):
    tags: List[str]
    settings: dict
    roles: dict