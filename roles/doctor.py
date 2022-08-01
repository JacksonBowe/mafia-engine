import logging
from events import GameEvent, GameEventGroup
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
    
    @property
    def action_success_game_event(self, target) -> GameEventGroup:
        revive_event_group = GameEventGroup()

        # Notify self of successful revive
        notify_self_event = GameEvent(
            event_id="doctor_revive_success",
            targets=[self.player['id']],
            message='Your target was attacked last night, but you successfully revive them'
        )
        revive_event_group.new_event(notify_self_event)
        
        # Notify target of successful revive