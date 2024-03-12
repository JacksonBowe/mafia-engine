from pydantic import BaseModel, Field

from engine.roles import Actor, Town
from engine.models import Player

class CitizenSettings(BaseModel):
    max_vests: int = Field(default=2, alias="maxVests")

class Citizen(Town):
    tags = ["any_random", "town_random", "town_government"]
    
    def __init__(self, player: Player, settings: dict):
        super().__init__(player)
        self.settings = CitizenSettings.model_validate(settings)