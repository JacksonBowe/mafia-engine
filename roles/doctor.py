from roles.actor import Actor

class Doctor(Actor):
    def __init__(self, player, settings):
        self.role_name = "Doctor"
        self.alignment = "Town"
        super().__init__(player)

        pass
    
    