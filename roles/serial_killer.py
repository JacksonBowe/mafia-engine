from roles.actor import Actor

class SerialKiller(Actor):
    def __init__(self, name):
        self.role_name = "Serial Killer"
        self.alignment = "Neutral"
        self.tags = ["Killing", "Evil"]
        super().__init__(name)
        pass
