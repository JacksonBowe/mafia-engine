from typing_extensions import Annotated
from annotated_types import Ge, Le
from typing import List, Optional, Mapping, Any
from pydantic import BaseModel, Field, validator

# from engine.roles import ROLE_TAGS

class Player(BaseModel):
    id: str
    name: str
    alias: str
    role: Optional[str] = None
    number: Optional[int] = None  # TODO: Ensure number is between 1 and 15 inclusive
    alive: Optional[bool] = True
    possible_targets: Optional[List[List[int]]] = Field(default_factory=list, max_items=2, alias='possibleTargets')
    targets: Optional[List[int]] = Field(default_factory=list, max_items=15)
    allies: Optional[List[int]] = Field(default_factory=list, max_items=15)
    role_actions: Optional[Mapping[str, Any]] = Field(default_factory=dict, alias='roleActions')

    # @validator('role')
    # def role_must_exist_in_external_dict(cls, v):
    #     if v not in ROLE_TAGS.keys():
    #         raise ValueError(f"Role {v} is not a valid role")
    #     return v

    @validator('targets', 'allies', each_item=True)
    def validate_target_lists(cls, v):
        if isinstance(v, list):
            print('YOOOOOOOOOOOOOOOO', v)
            if any(not (1 <= item <= 15) for item in v):
                raise ValueError("All values must be between 1 and 15 inclusive")
        return v

    @validator('possible_targets')
    def validate_possible_targets(cls, v):
        if len(v) > 2:
            raise ValueError("possible_targets list cannot have more than 2 lists")
        for sublist in v:
            if len(sublist) > 15:
                raise ValueError("Sublists in possible_targets cannot have more than 15 items")
            
            if any(not (1 <= item <= 15) for item in sublist):
                raise ValueError("All values must be between 1 and 15 inclusive")
        return v