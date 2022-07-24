from roles.actor import Actor
import logging

class Escort(Actor):
    def __init__(self, player, settings):
        super().__init__(player)
        self.role_name = "Escort"
        self.alignment = "Town"
    
    @property
    def state(self):
        # Return 'self.state' merged with 'parent.state'
        return {**super().state,**{
        }}