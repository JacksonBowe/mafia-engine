from dataclasses import dataclass, field, asdict
from typing import (
    List,
    Union
)
import logging




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
    events: List[Union[GameEvent, 'GameEventGroup']] = field(default_factory=list)

    def new_event(self, event: GameEvent):
        self.events.append(event)
        return
    
    def new_event_group(self, event_group: 'GameEventGroup'):
        self.events.append(event_group)
        return
    
    def reset(self):
        self.events = []

    def dump(self):
        return [event.dump() for event in self.events]

    
ACTION_EVENTS = GameEventGroup()
EVENTS = GameEventGroup()

@dataclass
class ActorEvent:
    night: str
    visited: list
    visited_by: list
    