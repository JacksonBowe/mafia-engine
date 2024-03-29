from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Callable

from engine.utils.logger import logger
import engine.roles as roles
import engine.events as events
from engine.events import ACTION_EVENTS

class Actor(ABC):
    def __init__(self, player: dict):
        self.alias: str = player.get('alias', None)
        self.player: dict = player
        self.number: int = player.get('number', None)
        self.alignment: str = roles.Alignment.TOWN
        self.role_name: str = 'Actor'
        self.house: int = None
        self.home: bool = True
        self.alive: bool = player.get('alive', True)
        self.action_done: bool = False
        self.night_immune: bool = False
        self.visiting: Actor = None
        self.visitors: List[Actor] = []
        self.doctors: List[roles.Doctor] = []
        self.bodyguards: List[roles.Bodyguard] = []
        self.possible_targets: List[List[Actor]] = []
        self.targets: List[Actor] = None
        self.allies: List[Actor] = []
        self.death_reason: str = None
        self.death_day: int = None
        # self.targets: List = player.get('targets', [])
        self.will: str = player.get('will', None)
        # TODO: self.witched, self.roleblocked
        
    def __repr__(self) -> str:
        return f"|{self.role_name}| {self.alias}({self.number})"
    
    @property
    def state(self):
        # print(self)
        # Returns the base player used to construct the Actor, and some actor fields
        return {**self.player,**{
            'number': self.number,
            # 'house': self.house,
            'alive': self.alive,
            'possible_targets': [ # self.possible_targets is a list of lists [[], []]. Need to loop through the internal lists and convert the actors to just their numbers
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
    
    def set_number_and_house(self, number: int) -> None:
        self.number = number
    
    def find_allies(self, actors: List[Actor]=None) -> None:
        self.allies = []
        return self.allies
    
    def find_possible_targets(self, actors: List[Actor]=None) -> None:
        self.possible_targets = []
        return self.possible_targets
    
    def set_targets(self, targets: List[roles.Actor]=[]):
        self.targets = targets

    def lynched(self):
        reason = "They were lynched"
        self.die(reason)
    
    def do_action(self):
        self.action_done = True
        self.action()
    
    @abstractmethod
    def action(self):
        pass
    
    def investigate(self):
        pass
    
    def visit(self, target: roles.Actor) -> None:
        logger.info(f"{self} is visiting {target}'s house")
        self.home = False
        self.visiting = target
        target.visitors.append(self)
        return
    
    def kill(self, target: roles.Actor, success: Callable[[None],None], fail: Callable[[None],None], true_death: bool=False) -> None:
        # Triggers success/fail callback
        logger.info(f"{self} is attempting to kill {target}")
        
        self.visit(target)
        
        if not self.alive: return # TODO: Not entirely sure this should be here
        
        if target.bodyguards:
            bodyguard = target.bodyguards.pop(0)
            bodyguard.shootout(self)
        elif target.night_immune:
            logger.info(f"{self} failed to kill {target} because they are night-immune")
            fail()
            
            # Night Immunity event group
            survive_event_group = events.GameEventGroup(group_id=events.Common.NIGHT_IMMUNE)
            
            # Inform the target that they survived the attack
            survive_event_group.new_event(
                events.GameEvent(
                    event_id=events.Common.NIGHT_IMMUNE,
                    targets=[target.player['id']],
                    message="You were attacked tonight but survived due to Night Immunity"
                )
            )
            
            ACTION_EVENTS.new_event_group(survive_event_group)
        
        else:
            success()
            target.die(reason=self.death_reason, true_death=true_death)
            
    def die(self, reason: str=None, true_death: bool=False) -> None:
        # TODO: True Death
        self.alive = False
        self.doctors = [doctor for doctor in self.doctors if doctor.alive] # Remove any dead doctors
        if self.doctors:
            doctor = self.doctors.pop(0)
            doctor.revive_target(self)
        else:
            self.death_reason = reason
            logger.info(f"{self} died. Cause of death: {reason}")
     
    @abstractmethod       
    def check_for_win(self, actors: List[Actor]) -> bool:
        pass
            
class Town(Actor):
    def __init__(self, player: dict):
        super().__init__(player)
        self.alignment = "Town"
        
    def check_for_win(self, actors: List[Actor]) -> bool:
        enemies = []
        enemies.extend([actor for actor in actors if actor.alignment in [roles.Alignment.MAFIA]])
        if enemies: return False
        else: return True
        
class Mafia(Actor):
    def __init__(self, player: dict): # TODO: Add settings here?
        super().__init__(player)
        self.alignment = roles.Alignment.MAFIA
        self.kill_message = "You were killed by a member of the Mafia" # TODO
        self.death_reason = "They were found riddled with bullets" # TODO
        
    def find_allies(self, actors: List[roles.Actor] = None) -> None:
        self.allies = [actor for actor in actors if actor.alignment == self.alignment]
        return
    
    def check_for_win(self, actors: List[Actor]) -> bool:
        enemies = [actor for actor in actors if actor not in self.allies]
        wins_with = [''] # TODO: Not sure if this should be tags or explicily stating roles. Probably roles
        
        if enemies: return False
        else: return True
        
        
        
        
        
        
        
    
    
        
    