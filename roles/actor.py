

class Actor:

    def __init__(self, player):
        self.alias = player['state']['alias']
        self.player = player
        self.number = ''
        self.house = ''
        self.alive = True
        self.target = player.get('targets', [])
        
        
    @property
    def state(self):
        return {
            'alias': self.alias,
            'number': self.number,
            'house': self.house,
            'alive': self.alive
        }

    def set_number_and_house(self, number):
        self.set_number(number),
        self.set_house(number)

    def set_number(self, number):
        if number < 1 or number > 15:
            raise "Error"
        self.number = number


    def set_house(self, house):
        self.house = house

    def dump(self):
        # This is an ACTOR level method that is used by ROLE children. When the ROLE child 
        # calls self.dump() it will run the Actor.dump() method, which calls the Child.state 
        # propery, which in turn calls the Actor.state propery
        self.player['state'] = self.state
        self.player['targets'] = []
        return self.player
    
    
        