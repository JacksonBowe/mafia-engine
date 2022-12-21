from logger import logger
from typing import List
from events import EVENTS, GameEvent, GameEventGroup
from roles.actor import Actor

class Doctor(Actor):
    def __init__(self, player: dict=dict(), settings: dict=dict()):
        super().__init__(player)
        self.role_name = "Doctor"
        self.alignment = "Town"
        self.night_immune = False
        
        pass

    def _find_possible_targets(self, actors):
        num_targets = 1
        self.possible_targets = []
        for i in range(num_targets):
            self.possible_targets.insert(i, [
                actor for actor in actors
                if actor.alive
                and actor.number != self.number
            ])
    
    def _action(self, targets: List[Actor]=[]):
        if not targets: return
        self.target = targets[0]
        logger.info(f"{self} is attemping to heal { self.target}")
        self.visit(self.target)
        self.target.doctors.append(self) # Add self into the list of doctors protecting this target

    def _action_success(self):
        self.revive_target()
    
    def revive_target(self):
        logger.info(f"{self.target} was killed, and then healed by {self}")
        self.target.events.append("You were killed, and then revived by a G.O.A.T'ed medic")
        # Notify self and doctor of revival
        revive_event_group = GameEventGroup(group_id='revive_event_group')
        
        # Inform the doctor that his revive was successfull
        revive_event_group.new_event(
            GameEvent(
                event_id="doctor_revive_target_success",
                targets=[self.player['id']],
                message='Your target was attacked last night, but you successfully revive them'
            )
        )
        
        # Inform the player that they were revived
        revive_event_group.new_event(
            GameEvent(
                event_id="doctor_revive",
                targets=[self.target.player['id']],
                message="Sike. A Doctor has revived you. Rock on"
            )
        )

        EVENTS.new_event_group(revive_event_group)