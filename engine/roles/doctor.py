from typing import List

import engine.roles as roles
import engine.events as events
from engine.events import ACTION_EVENTS
from engine.utils.logger import logger

class Doctor(roles.Town):
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
        logger.info(f"{self} will attempt to heal {target}")
        self.visit(target)
        target.doctors.append(self) # Add self into the list of doctors protecting this target
    
    def revive_target(self, target: roles.Actor) -> None:
        logger.info(f"{self} revives {target}")
        
        # Event group for the revival
        revive_event_group = events.GameEventGroup(group_id='doctor_revive')
        
        # Inform the doctor that the target was revived
        revive_event_group.new_event(
            events.GameEvent(
                event_id='doctor_revive_success',
                targets=self.player['id'],
                message='Your target was attacked last night, but you successfully revived them'
            )
        )
        
        # TODO: Possibly inform all other doctos that the target was revived
        
        # Inform the player that they were revivied
        revive_event_group.new_event(
            events.GameEvent(
                event_id='revive_by_doctor',
                targets=[target.player['id']],
                message='You were revived by a doctor. Rock on'
            )
        )
        
        ACTION_EVENTS.new_event_group(revive_event_group)
        print('Target revived')