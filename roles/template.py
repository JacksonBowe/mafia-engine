import logging
from typing import List
from events import EVENTS, GameEvent, GameEventGroup
from roles.actor import Actor

class Doctor(Actor):
    def __init__(self, player: dict=dict(), settings: dict=dict()):
        super().__init__(player)
        self.role_name = ""
        self.alignment = ""
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
        target = targets[0]
        logging.info(f"{self} is attemping to ...")

    def _action_success(self, target):
        # onSuccess handler
        template_event_group = GameEventGroup()
        # Inform all players that a mafia kill has succeeded
        template_event_group.new_event(
            GameEvent(
                event_id='action_success',
                targets=['*'],
                message="An action has occurred"
            )
        )
        # Inform the target player that they have been killed
        template_event_group.new_event(
            GameEvent(
                event_id="action target",
                targets=[target.player['id']],
                message='You were the target of the action'
            )
        )
        EVENTS.new_event_group(template_event_group)