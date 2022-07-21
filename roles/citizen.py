from roles.actor import Actor
import logging

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
        if self.remainingVests > 0:
            self.possible_targets = [self.number]
    
      
    def action(self, actor_targets):
        if not self.targets or self.targets[0] != self.number: 
            logging.warning(f"{self.alias}({self.number}) invalid target ({self.targets}). {self.role_name} can only target self)")
            return
        self.remainingVests -= 1
        logging.info(f"|{self.role_name}| {self.alias}({self.number}) used vest. {self.remainingVests} remaining")
        
        
        