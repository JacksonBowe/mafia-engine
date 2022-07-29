from dataclasses import dataclass, field

EVENTS = []

@dataclass
class GameEvent:
    ''' What event was it, and who should it be broadcast to'''
    event_id: str
    targets: list
    message: str   

@dataclass
class ActorEvent:
    night: str
    visited: list
    visited_by: list
    