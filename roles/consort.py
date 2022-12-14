from roles.actor import Actor

class Consort(Actor):
    def __init__(self, player, settings):
        self.role_name = "Consort"
        self.alignment = "mafia"
        super().__init__(player)
        pass
    
    @property
    def state(self):
        # Return 'self.state' merged with 'parent.state'
        return {**{
            
        }, **super().state}
        
    def find_allies(self, actors):
        self.allies = self.allies = [actor for actor in actors if actor.alignment == self.alignment]
        
    def find_possible_targets(self, actors):
        # Number of targets
        num_targets = 1
        self.possible_targets = []
        for i in range(num_targets):
            self.possible_targets.append([
                actor for actor in actors
                if actor.alive
                and actor.alignment != self.alignment
                and actor.number != self.number
            ])

    