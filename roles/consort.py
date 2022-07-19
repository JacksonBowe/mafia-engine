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