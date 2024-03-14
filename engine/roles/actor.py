from __future__ import annotations
from enum import Enum
from typing import List, Callable
from abc import ABC, abstractmethod

from engine.utils.logger import logger
from engine.models import Player
import engine.events as events
from engine.events import ACTION_EVENTS
import engine.roles as roles

class Actor(ABC):
    tags = ['any_random']
    def __init__(self, player: Player) -> None:
        self.alignment = None
        
        # Attributes
        self.player = player
        self.alias = player.alias
        self.number = player.number
        self.alive = player.alive
        
        # State
        self.allies: List[Actor] = []
        self.possible_targets: List[List[Actor]] = []
        self.visitors: List[Actor] = []
        self.bodyguards: List[roles.Bodyguard] = []
        self.night_immune: bool = False
        # Action
        self.visiting: Actor = None
    
    @property
    def role_name(self) -> str:
        return self.__class__.__name__
    
    def dump_state(self):
        # print(self)
        # Returns the base player used to construct the Actor, and some actor fields
        return {**self.player.model_dump(by_alias=True),**{
            'number': self.number,
            # 'house': self.house,
            'alive': self.alive,
            'possibleTargets': [ # self.possible_targets is a list of lists [[], []]. Need to loop through the internal lists and convert the actors to just their numbers
                [ actor.number for actor in pos_targets_list]
                for pos_targets_list in self.possible_targets],
            'targets': [],
            'allies': [{
                "alias": ally.alias,
                "number": ally.number,
                "role": ally.role_name,
                "alive": ally.alive
                } for ally in self.allies],
            'alias': self.alias,
            # 'events': self.events
        }}
          
    def __repr__(self) -> str:
        return f"|{self.role_name}| {self.alias}({self.number})"
    
    def find_allies(self, actors: List[Actor] = None) -> List[Actor] | None:
        self.allies = []
        return self.allies
    
    def find_possible_targets(self, actors: List[Actor] = None) -> List[Actor] | None:
        self.possible_targets = []
        return self.possible_targets
    
    def set_targets(self, targets: List[Actor]):
        self.targets = targets
        
    def clear_targets(self) -> None:
        self.targets = []
        
    def do_action(self):
        self.action()
        
    @abstractmethod
    def action(self):
        pass
    
    def visit(self, target: Actor) -> None:
        logger.info(f"{self} is visiting {target}'s house")
        self.home = False
        self.visiting = target
        target.visitors.append(self)
        return
    
    def kill(self, target: Actor, success: Callable[[None], None], fail: Callable[[None], None], true_death: bool = False) -> None:
        logger.info(f"{self} is attempting to kill {target}")
        
        self.visit(target)
        
        if target.bodyguards:
            bg = target.bodyguards.pop(0)
            bg.shootout(self)
        elif target.night_immune:
            logger.info(f"{self} failed to kill {target} because they are night-immune")
            fail()
            
            # Night Immunity event group
            survive_event_group = events.GameEventGroup(group_id=events.Common.NIGHT_IMMUNE)
            
            # Inform the target that they survived the attack
            survive_event_group.new_event(
                events.GameEvent(
                    event_id=events.Common.NIGHT_IMMUNE,
                    targets=[target.player.id],
                    message="You were attacked tonight but survived due to Night Immunity"
                )
            )
            
            ACTION_EVENTS.new_event_group(survive_event_group)
        
        else:
            success()
            target.die(reason=f"Killed by {self}", true_death=true_death)
            
    def die(self, reason: str=None, true_death: bool=False) -> None:
        # TODO: True Death
        self.alive = False
        # self.doctors = [doctor for doctor in self.doctors if doctor.alive] # Remove any dead doctors
        # if self.doctors:
        #     doctor = self.doctors.pop(0)
        #     doctor.revive_target(self)
        # else:
        self.cod = reason
        logger.info(f"{self} died. Cause of death: {reason}")
            
class Alignment(Enum):
    TOWN = "Town"
    MAFIA = "Mafia"
    
class Town(Actor):
    def __init__(self, player: Player) -> None:
        super().__init__(player)
        self.alignment = Alignment.TOWN
        
    def check_for_win(self):
        pass
    
class Mafia(Actor):
    def __init__(self, player: Player) -> None:
        super().__init__(player)
        self.alignment = Alignment.MAFIA
        
    def find_allies(self, actors: List[Actor] = []) -> List[Actor]:
        self.allies = [actor for actor in actors if actor.alignment == self.alignment]
        
    def check_for_win(self):
        pass