from roles.actor import Actor

class Citizen(Actor):
    def __init__(self, name):
        self.role_name = "Citizen"
        self.alignment = "Town"
        self.tags = ['Government']
        super().__init__(name)

        pass