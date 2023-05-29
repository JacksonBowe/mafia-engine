from typing import List

import engine.roles as roles
import engine.events as events
from engine.events import ACTION_EVENTS
from engine.utils.logger import logger

class Detective(roles.Town):
    def __init__(self, player: dict=dict(), settings: dict=dict()):
        super().__init__(player)
        self.role_name = "Doctor"
        
    def find_possible_targets(self, actors):
        num_targets = 1
        self.possible_targets = []
        for i in range(num_targets):
            self.possible_targets.insert(i, [
                actor for actor in actors
                if actor.alive
                and actor.number != self.number
            ])
            
    def action(self) -> None:
        target = self.targets[0]
        logger.info(f"{self} will track {target}")
        self.visit(target)
        
    def investigate(self):
        target = self.targets[0]
        if not target.visiting: return
        print('yoyoyo')
        ACTION_EVENTS.new_event(
            events.GameEvent(
                event_id=events.Common.VISITED_BY,
                targets=[self.player['id']],
                message=f"Your target visited {target.visiting.alias}"
            )
        )
            