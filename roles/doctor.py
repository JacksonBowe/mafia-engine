from roles.actor import Actor

class Doctor(Actor):
    def __init__(self, player, settings):
        super().__init__(player)
        
        self.role_name = "Doctor"
        self.alignment = "Town"
        self.night_immune = False
        pass

    # def find
    
    
    def action(self, actor_targets):
        if not actor_targets: return
        target = actor_targets[0]
        
        target.doctors.append(self) # Add self into the list of doctors protecting this target
    
    