from roles.actor import Actor

class SerialKiller(Actor):
    def __init__(self, player, settings):
        self.role_name = "Serial Killer"
        self.alignment = "Neutral"
        super().__init__(player)
        pass
