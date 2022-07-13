from roles.actor import Actor

class Mafioso(Actor):
    def __init__(self, player, settings):
        self.role_name = "Mafioso"
        self.alignment = "mafia"
        super().__init__(player)
        pass