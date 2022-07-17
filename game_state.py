from game_save import GameSave
import importlib
class GameState():

    def __init__(self, players, game_save: GameSave):
        self.day = 1
        self.actors = []
        for index, player in enumerate(players):
            role = self.class_for_name('roles', player['role'])
            # Instantiate a Role class with :player and :role_settings <- Pulled from GameSave
            actor = role(player, game_save.role_settings(player['role']))
            actor.set_number_and_house(index+1)
            self.actors.append(actor)
            print(actor.state)
            
    def class_for_name(self, module_name, class_name):
        # Imports a class based on a provided string 
        # i.e ->
        #       :module_name = roles
        #       :class_name = citizen
        # Result: from roles.citizen import Citizen
        m = importlib.import_module(module_name)
        c = getattr(m, class_name)
        return c
    
    def dump(self):
        # result = {}
        # for actor in self.actors:
            
        result = {
            "day": self.day,
            "players": [{
                "number": actor.number,
                "name": actor.alias
            } for actor in self.actors],
            "events": [],
            "graveyard": [{
                "number": actor.number,
                "name": actor.alias,
                "death_reason": actor.death_reason
            } for actor in self.actors if not actor.alive]
        }
        # result = [actor.dump() for actor in self.actors]
        return result