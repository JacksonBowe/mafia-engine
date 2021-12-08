from roles.actor import Actor

class Mafioso(Actor):
    def __init__(self, name):
        self.role_name = "Mafioso"
        self.alignment = "Mafia"
        self.tags = ["Killing"]
        super().__init__(name)
        pass