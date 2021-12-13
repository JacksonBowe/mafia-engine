

class Actor:

    def __init__(self, name):
        self.name = name
        self.alive = True

    def set_number_and_house(self, number):
        self.set_number(number),
        self.set_house(number)

    def set_number(self, number):
        if number < 1 or number > 15:
            raise "Error"
        self.number = number


    def set_house(self, house):
        self.house = house

    
    
        