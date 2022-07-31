import logging
from events import (
    EVENTS,
)

class Actor:

    def __init__(self, player: dict=dict()):
        self.alias = player.get('alias', None)
        self.player = player
        self.number = player.get('number', None)
        self.house = [self]
        self.night_immune = False
        self.death_reason = player.get('deathReason', None)
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
        print(self)
        # Returns the base player used to construct the Actor, and some actor fields
        return {**self.player,**{
            'number': self.number,
            # 'house': self.house,
            'alive': self.alive,
            'possible_targets': [ # self.possible_targets is a list of lists [[], []]. Need to loop through the internal lists and convert the actors to just their numbers
                [ actor.number for actor in pos_targets_list]
                for pos_targets_list in self.possible_targets],
            'targets': self.targets,
            'allies': [{
                "alias": ally.alias,
                "number": ally.number,
                "role": ally.role_name,
                "alive": ally.alive
                } for ally in self.allies],
            'alias': self.alias,
            'events': self.events
        }}
    
    def find_allies(self, actors) -> None:
        try:
            self._find_allies(actors)
        except AttributeError:
            self.allies = []
    
    def find_possible_targets(self, actors) -> None:
        try:
            self._find_possible_targets(actors)
        except AttributeError:
            self.possible_targets = []
        
    def set_number_and_house(self, number):
        self.set_number(number),
        self.set_house(number)

    def set_number(self, number) -> None:
        if number < 1 or number > 15:
            raise "Error"
        self.number = number


    def set_house(self, house) -> None:
        self.house = house
        
    def action(self, targets: list=[]) -> None:
        try:
            self._action(targets)
        except AttributeError:
            pass
    
    def visit(self, target) -> None:
        target.house.append(self)
    
    def kill(self, target, true_death=False) -> None:
        logging.info(f"{self} is attempting to kill {target}")
        self.visit(target)
        
        if target.night_immune:
            self.events.append(f"Failed to kill {target}: Target is Night Immune")
            target.events.append(f"You were attacked but managed to survive")
            logging.info(f"{self} failed to kill {target}: Target is Night Immune")
            EVENTS.append(self.kill_fail(target))
            return False, "Target is Night Immune"
        # elif target.bodyguards:
            # Process Bodyguard stuff
        else:
            EVENTS.append(self.kill_success(target))
            target.die(self.death_reason)
        

        return

    def die(self, reason) -> None:
        if self.doctors:
            doctor = self.doctors.pop(0)
            logging.info(f"{self} was killed, and then healed by {doctor}")
            self.events.append("You were killed, and then revived by a G.O.A.T'ed medic")
        else:
            logging.info(f"{self} was killed")
            self.events.append("You were killed")
            self.death_reason = reason
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

    
    
        
    
    
        