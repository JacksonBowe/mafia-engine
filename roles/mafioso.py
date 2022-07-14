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
        
    # def action(self, targets: list=[]):
    #     self.remainingVests -= 1