from roles.actor import Actor
import logging

class Citizen(Actor):
    def __init__(self, player: dict=dict(), settings: dict=dict()):
        super().__init__(player)
        self.role_name = "Citizen"
        self.alignment = "Town"
        self.max_vests = settings.get('maxVests', 2)
        self.remaining_vests = player.get('remainingVests', self.max_vests)
    
    @property
    def state(self):
        # Return 'self.state' merged with 'parent.state'
        return {**super().state,**{
            "remainingVests": self.remaining_vests
        }}
        
    def find_allies(self, actors):
        self.allies = []
        
    def find_possible_targets(self, actors):
        self.possible_targets = []
        if self.remaining_vests > 0:
            self.possible_targets = [[self]]
    
      
    def action(self, targets):
        if not self.remaining_vests > 0:
            logging.critical(f"{self} tried to use vest but has 0 remaining")
            return
        target = targets[0]
        if target != self: 
            logging.warning(f"{self.alias}({self.number}) invalid target ({targets[0].number}). {self.role_name} can only target self)")
            return
        self.remaining_vests -= 1
        self.night_immune = True
        logging.info(f"|{self.role_name}| {self.alias}({self.number}) used vest. {self.remaining_vests} remaining")
        # print(f"|{self.role_name}| {self.alias}({self.number}) used vest. {self.remaining_vests} remaining")
        self.events.append(f"default:You don your bullet proof vest. You have {self.remaining_vests} remaining")
        
        
        
        