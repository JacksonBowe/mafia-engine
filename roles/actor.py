import logging
from events import (
    EVENTS,
    GameEvent,
    GameEventGroup,
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
        self.bodyguards = []
        self.events = []
        self.possible_targets = []
        self.targets = player.get('targets', [])
        # self.action_events = GameEventGroup()
        
        
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
        
    def action(self, targets: list=[]) -> GameEventGroup:
        if not self.alive: return
        # TODO check if has attribute _self._action . If not then return None
        self._action(targets)

    def action_success(self):
        # TODO check if has attribute self._action_success. If not then return
        self._action_success()
        
    def visit(self, target) -> None:
        target.house.append(self)
        # If target.is_allert: target.kill_intruder(self) -> self.die() lmao
        
    def survive_attack(self) -> None:
        # TODO
        # Function that runs when an actor survives an attack for whatever reason
        # Inform the player that they were attacked but survived.
        
        # Inform all doctors on target that they were not needed
        pass
    
    def kill(self, target, true_death: bool=False) -> None:
        logging.info(f"{self} is attempting to kill {target}")
        
        # event_group = EVENTS[-1]
        self.visit(target)
        
        if not self.alive: return
        
        if target.bodyguards:
            # TODO: Process Bodyguard stuff
            bodyguard = target.bodyguards.pop()
            print(bodyguard)
            bodyguard.shootout
            pass

        elif target.night_immune:
            logging.info(f"{self} failed to kill {target}: Target was Night Immune")
            target.survive_attack() # TODO

        else:            
            self._action_success()
            target.die(self.death_reason)
            return True
        

        return 

    def die(self, reason: str) -> None:
        if self.doctors:
            doctor = self.doctors.pop(0)
            doctor.revive_target()          

        else:
            logging.info(f"{self} was killed")
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

    
    
        
    
    
        