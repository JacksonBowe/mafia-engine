from events import EVENTS, GameEvent, GameEventGroup
from roles.actor import Actor
from typing import List
import logging

class Bodyguard(Actor):
    def __init__(self, player: dict=dict(), settings: dict=dict()):
        super().__init__(player)
        self.role_name = "Bodyguard"
        self.alignment = "Town"
    
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
        logging.info(f"{self} will protect {self.target} tonight")
        self.target.bodyguards.append(self)
        
    def shootout(self, attacker: Actor):
        shootout_event_group = GameEventGroup()
        
        # Inform all players that a shootout has occured
        shootout_event_group.new_event(
            GameEvent(
                event_id='bodyguard_shootout',
                targets=['*'],
                message="You hear sounds of a shootout"
            )
        )
        
        # TODO: Inform other bodyguards?
        
        # Inform the player that they have been protected
        shootout_event_group.new_event(
            GameEvent(
                event_id='bodyguard_protect',
                targets=self.target.player['id'],
                message='You were attacked but your Bodyguard defended you while you escaped'
            )
        )
        
        # Inform the attacker that they have died in a shootout
        shootout_event_group.new_event(
            GameEvent(
                event_id='bodyguard_kill_attacker',
                targets=[attacker.player['id']],
                message='You were killed by the Bodyguard defending your target'
            )
        )
        
        # Inform self that you have died defending target
        shootout_event_group.new_event(
            GameEvent(
                event_id='bodyguard_die_protecting',
                targets=self.player['id'],
                message='You died defending your target'
            )
        )
                
        EVENTS.new_event_group(shootout_event_group)
        attacker.die('Killed in a shootout')
        self.die('Killed in a shootout')

    

    

        

        
        
        