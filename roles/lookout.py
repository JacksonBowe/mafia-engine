from events import EVENTS, GameEvent, GameEventGroup
from roles.actor import Actor
import logging

class Lookout(Actor):
    def __init__(self, player: dict=dict(), settings: dict=dict()):
        super().__init__(player)
        self.role_name = "Lookout"
        self.alignment = "Town"
    
    @property
    def state(self):
        # Return 'self.state' merged with 'parent.state'
        return {**super().state,**{
        }}
        
    def _find_possible_targets(self, actors):
        num_targets = 1
        self.possible_targets = []
        for i in range(num_targets):
            self.possible_targets.insert(i, [
                actor for actor in actors
                if actor.alive
            ])
    
      
    def action(self, targets):
        if not targets: return
        self.target = targets[0]
        logging.info(f"{self} is observing the house of { self.target}")
        witnessed_visitors_event_group = GameEventGroup()
        visitors = [actor.alias for actor in self.target.house if actor.number is not self.target.number]
        # if (self.target.house)
        witnessed_visitors_event_group.new_event(
            GameEvent(
                event_id="lookout_witnessed_visitors",
                targets=[self.player['id']],
                message=f"Your target was visited by: {visitors}"
            )
        )
        
        EVENTS.new_event_group(witnessed_visitors_event_group)
        
        
        
        
        
        