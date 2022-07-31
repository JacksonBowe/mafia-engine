from dataclasses import dataclass, field, asdict
import logging

EVENTS = []

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
    game_events: list[GameEvent] = field(default_factory=list)

    def new_event(self, event: GameEvent):
        self.game_events.append(event)
        return

    def dump(self):
        return [game_event.dump() for game_event in self.game_events]

@dataclass
class ActorEvent:
    night: str
    visited: list
    visited_by: list
    