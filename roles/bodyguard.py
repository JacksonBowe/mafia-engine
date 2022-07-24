from roles.actor import Actor
import logging

class Bodyguard(Actor):
    def __init__(self, player, settings):
        super().__init__(player)
        self.role_name = "Bodyguard"
        self.alignment = "Town"
    
    @property
    def state(self):
        # Return 'self.state' merged with 'parent.state'
        return {**super().state,**{
        }}
        

        
        
        