from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import (
    List,
    Union
)
import logging
from logger import logger




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
    events: List[Union[GameEvent, GameEventGroup]] = field(default_factory=list)
    duration: int = 0

    def new_event(self, event: GameEvent):
        self.events.append(event)
        return
    
    def new_event_group(self, event_group: GameEventGroup):
        logger.debug(f"New event group '{event_group.group_id}'")
        self.events.append(event_group)
        return
    
    @property
    def total_duration(self):
        # Calculate the duration for this event group + all contained event groups
        total = self.duration
        for event in self.events:
            if isinstance(event, GameEventGroup):
                total += event.total_duration
        return total

    def dump(self):
        # return [event.dump() for event in self.events]
        return asdict(self)['events']
    
@dataclass
class Duration:
    value: int = 0
    
    def add(self, v : int) -> None:
        logger
        self.value =+ v

    
ACTION_EVENTS = GameEventGroup()
EVENTS = GameEventGroup(group_id='root')
DURATION = Duration()

@dataclass
class ActorEvent: # Feels like I may been this for coroner???
    night: str
    visited: list
    visited_by: list
    