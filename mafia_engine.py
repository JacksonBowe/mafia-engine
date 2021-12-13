import importlib
import random


class MafiaEngine():
    def __init__(self):
        self.game_state = GameState()
        pass

    def create_game(self, players, roles):
        # TODO: Needs to take a a GameSave rather than simply a roles list
        # Needs to return a GameState in JSON format
        print("Creating Game")
        print("Roles:", roles)
        print("Players:", len(players), players)

        print("Constructing GameState")
        class_roles = []
        for role in roles:
            class_roles.append(self.class_for_name('roles', role))
        
        random.shuffle(players)
        random.shuffle(class_roles)
        players_roles = list(zip(players, class_roles))
        self.actors = []

        for i, player_role in enumerate(players_roles):
            
            actor = player_role[1](player_role[0])
            actor.set_number_and_house(i+1)
            # print(f'Creating actor: {actor.name} ({actor.role_name})')
            self.actors.append(actor)

        self.day = 1
        # self.init_game_state(self.actors)

        return self.dump_state()

    def init_game_state(self, actors):
        game_state = GameState("init", actors=self.actors)
        pass

    # This can go in a UTILS file maybe
    def class_for_name(self, module_name, class_name):
        m = importlib.import_module(module_name)
        c = getattr(m, class_name)
        return c

    def dump_state(self):
        result = {
            "day": self.day,
            "actors": [{
                "number": actor.number,
                "name": actor.name,
                "role": actor.role_name,
                "house": actor.house,
                "targets": [],
                "alive": actor.alive
            } for actor in self.actors],
            "graveyard": [{
                "name": actor.name
            } for actor in self.actors if not actor.alive]
        }
        return result
        pass



class GameState():

    def __init__(self, method=None, **kwargs):
        if method == "init":
            self.actors = kwargs.get('self.actors')
            return self.init_state(self.actors)

    def init_state(self, actors):
        print("initting")
        self.day = 0,
        self.self.actors = [None for i in range(len(self.actors))] # Initialise an empyt list for the size we want
        print(self.self.actors)
        for actor in self.actors:
            print(actor.number)
            pass

    def load_state(self):
        pass

    def dump_state(self):
        pass