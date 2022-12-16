import logging
from events import (
    EVENTS,
    ACTION_EVENTS,
    GameEvent,
    GameEventGroup,
)

class Actor:

    def __init__(self, player: dict=dict()):
        self.alias = player.get('alias', None)
        self.player = player
        self.number = player.get('number', None)
        self.house = [self] # TODO: A list of all Actors at this house?
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
        # print(self)
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
        # TODO: This makes no sense
        self.house = house
        
    def action(self, targets: list=[]) -> GameEventGroup:
        if not self.alive: return
        if not targets: return
        if not (hasattr(self, '_action') and callable(self._action)): return
        
        action_events = self._action(targets)
        print('sup', action_events)
        
        
    def visit(self, target) -> None:
        self.house.remove(self)
        target.house.append(self)
        # If target.is_allert: target.kill_intruder(self) -> self.die() lmao
    
    def kill(self, target, true_death: bool=False) -> None:
        # Returns True/False for Success/Fail
        logging.info(f"{self} is attempting to kill {target}")
        
        self.visit(target)
        
        if not self.alive: return
        
        if target.bodyguards:
            # TODO: Process Bodyguard stuff
            bodyguard = target.bodyguards.pop()
            bodyguard.shootout(self)

        elif target.night_immune:
            logging.info(f"{self} failed to kill {target}: Target was Night Immune")
            

            # Night Immunity event group
            survive_event_group = GameEventGroup()

            # Inform the attacker that their target is night immune
            survive_event_group.new_event(
                GameEvent(
                    event_id="target_night_immune",
                    targets=[self.player['id']],
                    message="Target is Night Immune"
                )
            )

            # Inform the target that they survived the attack
            survive_event_group.new_event(
                GameEvent(
                    event_id="self_night_immune",
                    targets=[target.player['id']],
                    message="You were attacked tonight but surived due to Night Immunity"
                )
            )
            ACTION_EVENTS.new_event_group(survive_event_group)
            
            return False
        else:            
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


    
    
        
    
    
        