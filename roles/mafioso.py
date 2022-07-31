import logging
from roles.actor import Actor
from events import GameEvent, GameEventGroup

class Mafioso(Actor):
    def __init__(self, player: dict=dict(), settings: dict=dict()):
        super().__init__(player)
        self.role_name = "Mafioso"
        self.alignment = "mafia"
        self.kill_message = "You were killed by a member of the mafia"
        self.event_message = "You hear sounds of shots in the streets"
        self.kill_success_game_event = GameEvent(event_id="mafia_kill_success", targets=['*'], message=self.event_message)
        self.kill_fail_game_event = GameEvent(event_id="mafia_kill_fail", targets=['*'], message=None)
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
            
    def _action(self, targets: list()=[]):
        target = targets[0]

        # self.set_house(target.number)
        # # TODO: If target.bodyguards: self.die("You were killed by the bodyguard protecting your target", true_death=True), target.bodyguards.pop(0)
        # success, reason = target.die(self)
        # if not success:
        #     print("Kill failed: " + reason)
        #     self.events.append("Kill failed: " + reason)
        
        self.kill(target)

    def kill_success(self, target):
        event_group = GameEventGroup()
        # Inform all players that a mafia kill has succeeded
        event_group.new_event(
            GameEvent(
                event_id='mafia_kill_success',
                targets=['*'],
                message="You hear sounds of shots in the streets"
            )
        )
        # Inform the target player that they have been killed
        event_group.new_event(
            GameEvent(
                event_id="killed_by_mafia",
                targets=[target.player['id']],
                message='You were killed by a member of the mafia'
            )
        )
        return event_group

        