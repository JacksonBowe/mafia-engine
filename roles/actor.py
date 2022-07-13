

class Actor:

    def __init__(self, player):
        self.name = player['alias']
        self.number = player['number']
        self.house = player['house']
        self.alive = True
        
    @property
    def actor_state(self):
        return {
            'name': self.name,
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

    
    
        