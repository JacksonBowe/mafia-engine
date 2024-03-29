
from typing import List
from dataclasses import dataclass
import random

import engine.events as events
from engine.events import ACTION_EVENTS
import engine.roles as roles
from engine.utils.logger import logger


@dataclass
class GodfatherSettings:
    night_immune: bool = True
    
    def __init__(self, settings: dict=dict()) -> None:
        self.night_immune = settings.get('nightImmune', self.night_immune)

class Godfather(roles.Mafia):
    def __init__(self, player: dict, settings: dict=dict()):
        super().__init__(player)
        self.role_name = 'Godfather'
        self.settings = GodfatherSettings(settings)
        self.night_immune = self.settings.night_immune
    
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
            
    def action(self):
        target = self.targets[0]
        def success():
            success_event_group = events.GameEventGroup(group_id='godfather_action_success', duration=events.Duration.MAFIA_KILL)
            
            # Inform all players that a Mafia kill has succeeded
            success_event_group.new_event(
                events.GameEvent(
                    event_id="godfather_kill_success",
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
            fail_event_group = events.GameEventGroup(group_id="godfather_action_fail", duration=events.Duration.MAFIA_KILL)
            
            # Inform all players that a Mafia kill has failed
            fail_event_group.new_event(
                events.GameEvent(
                    event_id='godfather_kill_fail',
                    targets=['*'],
                    message=''
                )
            )
            
            ACTION_EVENTS.new_event_group(fail_event_group)
        
        # Check if there are idle Mafioso that you can send, else go yourself
        proxies = [ally for ally in self.allies if ally.role_name == 'Mafioso']
        if not proxies:
            self.kill(target, success, fail)
        else:
            proxy = random.choice(proxies)
            # TODO: If not target.witched
            proxy.targets = self.targets
            
            proxy_event_group = events.GameEventGroup(group_id='godfather_proxy')
            proxy_event_group.new_event(
                events.GameEvent(
                    event_id='godfather_proxy_choice',
                    targets=[ally.player['id'] for ally in self.allies],
                    message=f'The Godfather has chosed {proxy.alias} to carry out the hit'
                )
            )
            
            logger.info(f"{self} has chosen {proxy} to act as a proxy")
            ACTION_EVENTS.new_event_group(proxy_event_group)
