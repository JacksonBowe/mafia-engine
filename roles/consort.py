from roles.actor import Actor

class Mafioso(Actor):
    def __init__(self, name):
        self.role_name = "Consort"
        self.alignment = "mafia"
        super().__init__(name)
        pass