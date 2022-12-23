import random
import json
from dataclasses import dataclass

from game_save2 import GameSave
from game_state2 import GameState
from consts import TURN_ORDER
from events import GameEventGroup, EVENTS

from logger import logger



class Game():
    def __init__(self) -> None:
        self._save: GameSave = None
        self.state: GameState = None
        EVENTS.reset()
        pass
    
    def new(self, players: list, save: dict):
        logger.info("--- Creating Game ---")
        logger.info("Players: {}".format(len(players)))
        
        
        self._save = GameSave(save)
        
        self.roles, self.failed_roles = self._save.generate_roles()
        
        # Assign roles and numbers to players
        random.shuffle(players)
        random.shuffle(self._save.roles)
        
        # Allocate roles
        logger.info("--- Allocating roles ---")
        for index, player in enumerate(players):
            player['role'] = self._save.roles[index]
            logger.info(f"\t|-> {player['alias']} ({player['name']}):\t\t{player['role']}")
        
        # Generate GameState
        logger.info("--- Generating initial GameState ---")
        self.state = GameState().from_lobby(players, self._save.roles_settings)
        
        
        '''
        Assign roles to players
        convert player-role pairs to Actors
        generate allies and possible targets
        
        '''
        
        return self
    
    def load(self, prev_game_state: dict, players: list, save: list):
        logger.info("--- Loading Game ---")
        self._save = GameSave(save)
        
        self.state = GameState().from_previous(prev_game_state, players, self._save.roles_settings)

        return self
        
    def resolve_actions(self):
        logger.info("--- Resolving player actions ---")
        self.state.day += 1
        self.state.generate_allies_and_possible_targets()

        # sort the actors based on TURN_ORDER
        self.state.actors.sort(key=lambda actor: TURN_ORDER.index(actor.role_name))
        
        for actor in self.state.actors:
            if not actor.targets: continue
            logger.info(f"|{actor.role_name}| {actor.alias}({actor.number}) is targetting {actor.targets}")
            
            # The targets are just numbers, need to find associated Actors
            targets = [self.state.get_actor_by_number(target) for target in actor.targets]

            actor.action(targets)
            
            # if self.events.events:
            #     print(self.events)
                
        # Regenerate possible targets
        self.state.generate_allies_and_possible_targets()
        
        # print('State', json.dumps(self.dump_state(), indent=4))
        # print('Actors', json.dumps(self.dump_actors(), indent=4))
        # print('Events', json.dumps(self.dump_events(), indent=4))
        # print('Duration', EVENTS.total_duration)
                
    
    def dump_actors(self):
        self.state.generate_allies_and_possible_targets()
        return [actor.state for actor in self.state.actors]
    
    def dump_state(self):
        return self.state.dump()
    
    def dump_events(self):
        return EVENTS.dump()
    
    @property
    def events(self):
        return EVENTS.events
    
    
@dataclass
class Actors:
    actors