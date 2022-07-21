from roles.actor import Actor

class Mafioso(Actor):
    def __init__(self, player, settings):
        self.role_name = "Mafioso"
        self.alignment = "mafia"
        super().__init__(player)
        pass
    
    @property
    def state(self):
        # Return 'self.state' merged with 'parent.state'
        return {**{
            
        }, **super().state}
        
    def find_allies(self, actors):
        self.allies = [{
            actor.number: {
            "alias": actor.alias,
            "role": actor.role_name,
            "alive": actor.alive
            }} for actor in actors if actor.alignment == self.alignment]
        
    def find_possible_targets(self, actors):
        # Number of targets
        num_targets = 1
        
        for i in range(num_targets):
            self.possible_targets.append([
                actor.number for actor in actors
                if actor.alive
                and actor.alignment != self.alignment
                and actor.number != self.number
            ])
            
    def action(self, actor_targets):
        
        print(actor_targets)