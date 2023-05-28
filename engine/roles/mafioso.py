
from typing import List

import engine.events as events
from engine.events import ACTION_EVENTS
import engine.roles as roles
from engine.utils.logger import logger


class Mafioso(roles.Mafia):
    def __init__(self, player: dict, settings: dict):
        super().__init__(player)
        self.role_name = 'Mafioso'
        self.alignment = roles.Alignment.MAFIA
        self.kill_message = "You were killed by a member of the Mafia" # TODO
        self.death_reason = "They were found riddled with bullets" # TODO
        
    def find_allies(self, actors: List[roles.Actor] = None) -> None:
        self.allies = [actor for actor in actors if actor.alignment == self.alignment]
        return
    
    def find_possible_targets(self, actors: List[roles.Actor] = None) -> None:
        # Number of targets
        num_targets = 1 
        self.possible_targets = []
        for i in range(num_targets):
            self.possible_targets.insert(i, [
                actor for actor in actors 
                if actor.alive
                and actor.alignment != self.alignment
                and actor.number != self.number # Seems a bit redundant, but can't hurt
            ])
            
    def action(self, targets: List[roles.Actor]=[]):
        target = targets[0]
        def success():
            print('Target was killed')
            success_event_group = events.GameEventGroup(group_id='mafioso_action_success', duration=events.Duration.MAFIA_KILL)
            
            # Inform all players that a Mafia kill has succeeded
            success_event_group.new_event(
                events.GameEvent(
                    event_id="mafia_kill_success",
                    targets=['*'],
                    message="There are sounds of shots in the streets"
                )
            )
            
            # Inform the target player that they have been killed
            success_event_group.new_event(
                events.GameEvent(
                    event_id=events.Common.KILLED_BY_MAFIA,
                    targets=[target.player['id']],
                    message='You were killed by a member of the Mafia'
                )
            )
            
            ACTION_EVENTS.new_event_group(success_event_group)
        
        def fail():
            print('Target survived')
            fail_event_group = events.GameEventGroup(group_id="mafioso_action_fail", duration=events.Duration.MAFIA_KILL)
            
            # Inform all players that a Mafia kill has failed
            fail_event_group.new_event(
                events.GameEvent(
                    event_id='mafia_kill_fail',
                    targets=['*'],
                    message=''
                )
            )
            
            ACTION_EVENTS.new_event_group(fail_event_group)
        
        
        self.kill(target, success, fail)
