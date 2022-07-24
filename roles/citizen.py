from roles.actor import Actor
import logging

class Citizen(Actor):
    def __init__(self, player, settings):
        super().__init__(player)
        self.role_name = "Citizen"
        self.alignment = "Town"
        self.maxVests = settings.get('maxVests', 2)
        self.remaining_vests = player.get('remainingVests', self.maxVests)
    
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
        if self.alias == "Bronson": print(f"{self} generating targets. Vests {self.remaining_vests}")
        if self.remaining_vests > 0:
            self.possible_targets = [[self.number]]
        if self.alias == "Bronson": print("Targets generated", self.possible_targets)
    
      
    def action(self, actor_targets):
        if not self.remaining_vests > 0:
            logging.critical(f"{self} tried to use vest but has 0 remaining")
            print(f"{self} tried to use vest but has 0 remaining")
            print(f"{self.targets}, {self.possible_targets}")
            return
        print(actor_targets)
        target = actor_targets[0]
        if target != self: 
            logging.warning(f"{self.alias}({self.number}) invalid target ({actor_targets[0].number}). {self.role_name} can only target self)")
            return
        self.remaining_vests -= 1
        self.night_immune = True
        logging.info(f"|{self.role_name}| {self.alias}({self.number}) used vest. {self.remaining_vests} remaining")
        print(f"|{self.role_name}| {self.alias}({self.number}) used vest. {self.remaining_vests} remaining")
        self.events.append(f"default:You don your bullet proof vest. You have {self.remaining_vests} remaining")
        
        
        
        