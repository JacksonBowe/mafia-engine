from roles.actor import Actor

class Citizen(Actor):
    def __init__(self, player, settings):
        self.role_name = "Citizen"
        self.alignment = "Town"
        self.maxVests = settings.get('maxVests', 2)
        super().__init__(player)

        pass