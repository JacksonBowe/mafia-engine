import logging


class Actor:

    def __init__(self, player):
        self.alias = player.get('alias', None)
        self.player = player
        self.number = player.get('number', None)
        self.house = [self]
        self.night_immune = False
        self.death_reason = player.get('deathReason', '')
        self.alive = player.get('alive', True)
        self.allies = []
        self.doctors = []
        self.possible_targets = []
        self.targets = player.get('targets', [])
        self.events = []
        
    def __repr__(self) -> str:
        return f"|{self.role_name}| {self.alias}({self.number})"
        
        
    @property
    def state(self):
        # Returns the base player used to construct the Actor, and some actor fields
        return {**self.player,**{
            'number': self.number,
            # 'house': self.house,
            'alive': self.alive,
            'possible_targets': self.possible_targets,
            'targets': self.targets,
            'allies': self.allies,
            'alias': self.alias
        }}
    
    def find_allies(self, actors):
        pass
    
    def find_possible_targets(self, actors):
        pass
        
    def set_number_and_house(self, number):
        self.set_number(number),
        self.set_house(number)

    def set_number(self, number):
        if number < 1 or number > 15:
            raise "Error"
        self.number = number


    def set_house(self, house):
        self.house = house
        
    def action(self, targets: list=[]):
        pass
    
    def visit(self, target):
        target.house.append(self)
    
    def kill(self, target, true_death=False):
        logging.info(f"{self} is attempting to kill {target}")
        self.visit(target)
        
        if target.night_immune:
            self.events.append(f"Failed to kill {target}: Target is Night Immune")
            target.events.append(f"You were attacked but managed to survive")
            logging.info(f"{self} failed to kill {target}: Target is Night Immune")
            return False, "Target is Night Immune"
        
        target.die()
        return True, ""

    def die(self):
        if self.doctors:
            doctor = self.doctors.pop(0)
            logging.info(f"{self} was killed, and then healed by {doctor}")
            self.events.append("You were killed, and then revived by a G.O.A.T'ed medic")
        else:
            logging.info(f"{self} was killed")
            self.alive = False
        
        # # returns -> success, reason
        # print(self.role_name, self.night_immune)
        # # TODO
        # # if self.bodyguards:
        # #     bodyguard = self.bodyguards.pop(0)
        # #     killer.die(bodyguard)
        # if self.night_immune:
        #     self.events.append("You were attacked but managed to survive")
        #     logging.info(f"|{self.role_name}| {self.alias}({self.number}): Attacked, but is Night Immune")
        #     result = False, 'Target is Night Immune'
        
        # # elif self.jailed: # etc
        
        # else:
        
        #     logging.info(f"|{self.role_name}| {self.alias}({self.number}): {killer.kill_message}")
        #     self.alive = False
            
        #     self.death_reason = killer.kill_message
        #     result = True, ""
            
        # # Check if doctor healed
        # # for doctor in self.doctors
        
        # return  result
            
        
            
        
    

    # def dump(self):
        # This is an ACTOR level method that is used by ROLE children. When the ROLE child 
        # calls self.dump() it will run the Actor.dump() method, which calls the Child.state 
        # propery, which in turn calls the Actor.state property
        # state = self.state
        # self.player['state'] = self.state
        # for key in state:
        #     self.player[key] = state[key]
        # self.player['targets'] = []
        # self.player['allies'] = self.allies
        # self.player['possible_targets'] = self.possible_targets
        # return self.state
    
    
        
    
    
        