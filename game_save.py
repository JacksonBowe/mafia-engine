

class GameSave():
    def __init__(self, config: dict) -> None:
        self.config = config
        self.roles = self.select_roles()
        pass
    
    def select_roles(self):
        factions = [faction for faction in self.config['factions'] if self.config['factions'][faction]['config']['max'] > 0]
        
        print(factions)
        
        return 1
    
    