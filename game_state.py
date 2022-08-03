from game_save import GameSave
from consts import TURN_ORDER
from events import EVENTS, GameEventGroup, ACTION_EVENTS
import importlib
import logging
import json


class GameState():

    def __init__(self):
        self.day = 1
        self.actors = []
        self.save = None
        pass
            
    def class_for_name(self, module_name, class_name):
        # Imports a class based on a provided string 
        # i.e ->
        #       :module_name = roles
        #       :class_name = citizen
        # Result: from roles.citizen import Citizen
        m = importlib.import_module(module_name)
        c = getattr(m, class_name)
        return c
    
    def generate_allies_and_possible_targets(self):
        for actor in self.actors:
            if not actor.alive: continue
            actor.find_allies(self.actors)
            actor.find_possible_targets(self.actors)
    
    def new(self, players, game_save):
        self.day = 1
        self.save = game_save
        # self.actors = []
        print("Initing Gamestate with default value, applying new numbers to players")
        logging.info("Importing required roles and instantiating actors")
        for index, player in enumerate(players):
            role = self.class_for_name('roles', player['role'])
            # Instantiate a Role class with :player and :role_settings <- Pulled from GameSave
            actor = role(player, game_save.role_settings(player['role']))
            actor.set_number_and_house(index+1)
            self.actors.append(actor)
    
    def load(self, players, game_save: GameSave, prev_state: dict()):
        # print(json.dumps(prev_state, indent=4))
        self.day = prev_state['day']
        self.save = game_save
        logging.info(f"Day: {self.day}") # TODO add number of alive players?
        # self.actors = []
        print("Loading game state")
        for player in players:
            role = self.class_for_name('roles', player['role'])
            # Instantiate a Role class with :player and :role_settings <- Pulled from GameSave
            actor = role(player, game_save.role_settings(player['role']))
            self.actors.append(actor)
        
        
         
    def resolve(self):
        self.day += 1
        # Generate possible targets. This shouldn't be nessessary
        self.generate_allies_and_possible_targets()

        # sort the actors based on TURN_ORDER
        self.actors.sort(key=lambda actor: TURN_ORDER.index(actor.role_name))
        
        for actor in self.actors:
            if not actor.targets: continue
            print(f"|{actor.role_name}| {actor.alias}({actor.number}) is targetting {actor.targets}")
            targets = []
            for t in actor.targets:
                # Convert the targetted numbers into actor; eg. [[4]] -> [[actor where actor.number == 4]]
                for a in self.actors:
                    if a.number == t:
                        targets.append(a)
            
            # Create a new GameEventGroup, this will get populated by all events generated from this actors action
            
            actor_events = actor.action(targets)
            # print(actor_events)
            if actor_events:
                ACTION_EVENTS.new_event_group(actor_events)

        # Regenerate possible targets
        self.generate_allies_and_possible_targets()    
        
    
    def check_for_win(self):
        town_members = [actor for actor in self.actors if actor.alive and actor.alignment == "Town"]
        print("Town members", town_members)
        if not town_members: return "mafia_win"

    def dump(self):
        result = {
            "day": self.day,
            "players": [{
                "number": actor.number,
                "name": actor.alias,
                "alive": actor.alive
            } for actor in self.actors],
            # "events": [event.dump() for event in EVENTS],
            'events': EVENTS.dump(),
            # "events": EVENTS,
            "graveyard": [{
                "number": actor.number,
                "name": actor.alias,
                "deathReason": actor.death_reason
            } for actor in self.actors if not actor.alive]
        }

        return result