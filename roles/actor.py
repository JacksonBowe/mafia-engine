

class Actor:

    def __init__(self, player):
        self.alias = player.get('alias', None)
        self.player = player
        self.number = player.get('number', None)
        self.house = player.get('number', None)
        self.death_reason = player.get('deathReason', '')
        self.alive = player.get('alive', True)
        self.allies = []
        self.possible_targets = []
        self.targets = player.get('targets', [])
        self.events = []
        
        
    @property
    def state(self):
        # Returns the base player used to construct the Actor, and some actor fields
        return {**self.player,**{
            'number': self.number,
            'house': self.house,
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
    
    
        
    
    
        