import logging
from roles.actor import Actor

class Mafioso(Actor):
    def __init__(self, player, settings):
        super().__init__(player)
        self.role_name = "Mafioso"
        self.alignment = "mafia"
        self.kill_message = "You were killed by a member of the mafia"
        pass
    
    @property
    def state(self):
        # Return 'self.state' merged with 'parent.state'
        return {**{
            
        }, **super().state}
        
    def find_allies(self, actors):
        self.allies = [{
            "alias": actor.alias,
            "number": actor.number,
            "role": actor.role_name,
            "alive": actor.alive
            } for actor in actors if actor.alignment == self.alignment]
        
    def find_possible_targets(self, actors):
        # Number of targets
        num_targets = 1
        self.possible_targets = []
        for i in range(num_targets):
            self.possible_targets.insert(i, [
                actor.number for actor in actors
                if actor.alive
                and actor.alignment != self.alignment
                and actor.number != self.number
            ])
            
    def action(self, actor_targets):
        target = actor_targets[0]

        # self.set_house(target.number)
        # # TODO: If target.bodyguards: self.die("You were killed by the bodyguard protecting your target", true_death=True), target.bodyguards.pop(0)
        # success, reason = target.die(self)
        # if not success:
        #     print("Kill failed: " + reason)
        #     self.events.append("Kill failed: " + reason)
        
        self.kill(target)
        