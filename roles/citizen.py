from roles.actor import Actor

class Citizen(Actor):
    def __init__(self, player, settings):
        super().__init__(player)
        self.role_name = "Citizen"
        self.alignment = "Town"
        self.maxVests = settings.get('maxVests', 2)
        self.remainingVests = player.get('remainingVests', self.maxVests)
    
    @property
    def state(self):
        # Return 'self.state' merged with 'parent.state'
        return {**super().state,**{
            "remainingVests": self.remainingVests
        }}
        
    def find_allies(self, actors):
        self.allies = []
        
    def find_possible_targets(self, actors):
        self.possible_targets = [self.number]
    
      
    def action(self, targets: list=[]):
        self.remainingVests -= 1
        
        