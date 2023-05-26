from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import (
    List,
    Union
)
from engine.utils.logger import logger


@dataclass
class Duration:
    ZERO: int = 0
    # Mafia actions
    MAFIA_KILL: int = 3
    # Town Actions
    
    # Neutral Actions
    

@dataclass
class GameEvent:
    ''' What event was it, and who should it be broadcast to'''
    event_id: str
    targets: list
    message: str

    def dump(self):
        return asdict(self)

@dataclass
class GameEventGroup:
    ''' A Grouping of game events, eg. Broadcast event A to all players, and event B to select players'''
    group_id: str = None
    duration: Duration = Duration.ZERO
    events: List[Union[GameEvent, GameEventGroup]] = field(default_factory=list)

    def new_event(self, event: GameEvent):
        self.events.append(event)
        return
    
    def new_event_group(self, event_group: GameEventGroup):
        logger.debug(f"New event group '{event_group.group_id}'")
        self.duration += event_group.duration
        self.events.append(event_group)
        return
    
    # @property
    # def total_duration(self):
    #     # Calculate the duration for this event group + all contained event groups
    #     total = self.duration

    #     for event in self.events:
    #         if isinstance(event, GameEventGroup):
    #             total += event.duration

        
    #     return total
    
    def reset(self, new_id: str=None):
        self.events.clear()
        return self

    def dump(self):
        # return [event.dump() for event in self.events]
        # self.duration = self.total_duration
        # print('total duration', self.total_duration)
        return asdict(self)['events']



# Create a root event group. Bit silly but I want to use the methods
EVENTS = GameEventGroup(group_id='root')
ACTION_EVENTS = GameEventGroup(group_id='action')


# ------- Shared Events ------- #
@dataclass
class Common:
    INVALID_TARGET = "invalid_target"
    KILLED_BY_MAFIA = "killed_by_mafia"
    