import logging
from events import EVENTS, GameEvent, GameEventGroup
from roles.actor import Actor

class Doctor(Actor):
    def __init__(self, player: dict=dict(), settings: dict=dict()):
        super().__init__(player)
        
        self.role_name = "Doctor"
        self.alignment = "Town"
        self.night_immune = False
        
        pass

    def find_possible_targets(self, actors):
        num_targets = 1
        self.possible_targets = []
        for i in range(num_targets):
            self.possible_targets.insert(i, [
                actor for actor in actors
                if actor.alive
                and actor.number != self.number
            ])
    
    
    def action(self, actor_targets):
        if not actor_targets: return
        target = actor_targets[0]
        logging.info(f"{self} is attemping to heal {target}")
        target.doctors.append(self) # Add self into the list of doctors protecting this target
    
    def revive_target(self, target):
        logging.info(f"{target} was killed, and then healed by {self}")
        target.events.append("You were killed, and then revived by a G.O.A.T'ed medic")
        # Notify self and doctor of revival
        revive_event_group = GameEventGroup()
        
        # Inform the doctor that his revive was successfull
        revive_event_group.new_event(
            GameEvent(
                event_id="doctor_revive_target_success",
                targets=[self.player['id']],
                message='Your target was attacked last night, but you successfully revive them'
            )
        )
        # Inform all the other doctors that they were not needed
        revive_event_group.new_event(
            GameEvent(
                event_id="doctor_revive_unneeded",
                targets=[doctor.player['id'] for doctor in target.doctors],
                message="Your target was attacked last night, but your services were not needed... That's pretty suss bro"
            )
        )
        
        # Inform the player that they were revived
        revive_event_group.new_event(
            GameEvent(
                event_id="doctor_revive",
                targets=[target.player['id']],
                message="As your vision fades to black, you hear the rustling of footsteps and then BOOM - REVIVED BY AN ABSOLUTELY G.O.A.T'ed DOCTOR"
            )
        )
        EVENTS.new_event_group(revive_event_group)