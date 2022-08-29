import logging
from typing import List
from roles.actor import Actor
from events import EVENTS, GameEvent, GameEventGroup

class Mafioso(Actor):
    def __init__(self, player: dict=dict(), settings: dict=dict()):
        super().__init__(player)
        self.role_name = "Mafioso"
        self.alignment = "mafia"
        self.kill_message = "You were killed by a member of the Mafia" 
        self.death_reason = "They were found riddled with bullets."
        pass
    
    @property
    def state(self):
        # Return 'self.state' merged with 'parent.state'
        return {**{
            
        }, **super().state}
        
    def _find_allies(self, actors):
        self.allies = [actor for actor in actors if actor.alignment == self.alignment]
        
    def _find_possible_targets(self, actors):
        
        # Number of targets
        num_targets = 1
        self.possible_targets = []
        for i in range(num_targets):
            self.possible_targets.insert(i, [
                actor for actor in actors
                if actor.alive
                and actor.alignment != self.alignment
                and actor.number != self.number
            ])
            
    def _action(self, targets: List[Actor]=[], ):
        
        self.target = targets[0]
        # Inform self "You will attempt to kill {target.alias} tonight"
        self.kill(self.target)
        
        # if success:
        #     self._action_success(target)
        

    def _action_success(self):
        kill_event_group = GameEventGroup()
        # Inform all players that a mafia kill has succeeded
        kill_event_group.new_event(
            GameEvent(
                event_id='mafia_kill_success',
                targets=['*'],
                message="There are sounds of shots in the streets"
            )
        )
        # Inform the target player that they have been killed
        kill_event_group.new_event(
            GameEvent(
                event_id="killed_by_mafia",
                targets=[self.target.player['id']],
                message='You were killed by a member of the mafia'
            )
        )
        EVENTS.new_event_group(kill_event_group)

    def _action_fail(self):
        kill_fail_event_group = GameEventGroup()

        kill_fail_event_group.new_event(
            GameEvent(
                event_id='mafia_kill_fail',
                targets=['*'],
                message=''
            )
        )

        EVENTS.new_event_group(kill_fail_event_group)
    
    # def _action_fail(self, target):
    #     event_group = GameEventGroup()
    #     # Inform all players that a mafia kill has failed
    #     event_group.new_event(
    #         GameEvent(
    #             event_id='mafia_kill_fail',
    #             targets=['*'],
    #             message=None
    #         )
    #     )
        
    #     # Inform the target of the failed attack
    #     event_group.new_event(
    #         GameEvent(
    #             event_id="night_immune_hit_by_mafia",
    #             targets=[target.player['id']],
    #             message="You were attacked by the Mafia, but you managed to survive"
    #         )
    #     )
        
    #     # Inform the mafioso of the failed attack
    #     event_group.new_event(
    #         GameEvent(
    #             event_id="target_night_immune",
    #             targets=[self.player['id']],
    #             message=f"Failed to kill {target.alias}: Target is Night Immune"
    #         )
    #     )

        