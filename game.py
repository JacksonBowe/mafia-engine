import random
import json

from game_save2 import GameSave
from game_state2 import GameState
from consts import TURN_ORDER
from events import GameEventGroup, EVENTS, ACTION_EVENTS
from copy import deepcopy

from logger import logger



class Game():
    def __init__(self) -> None:
        self._save: GameSave = None
        self._state: GameState = None
        self._events: GameEventGroup = GameEventGroup()
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
        self._state = GameState().from_lobby(players, self._save.roles_settings)
        
        
        '''
        Assign roles to players
        convert player-role pairs to Actors
        generate allies and possible targets
        
        '''
        
        return self
    
    def load(self, prev_game_state: dict, players: list, save: list):
        logger.info("--- Loading Game ---")
        self._save = GameSave(save)
        
        self._state = GameState().from_previous(prev_game_state, players, self._save.roles_settings)

        return self
        
        '''
        load the previous state to get the day
        load the players as actors
        process the player actions
        '''
        
    def resolve_actions(self):
        logger.info("--- Resolving player actions ---")
        self._state.day += 1
        self._state.generate_allies_and_possible_targets()

        # sort the actors based on TURN_ORDER
        self._state.actors.sort(key=lambda actor: TURN_ORDER.index(actor.role_name))
        
        for actor in self._state.actors:
            if not actor.targets: continue
            logger.info(f"|{actor.role_name}| {actor.alias}({actor.number}) is targetting {actor.targets}")
            
            # The targets are just numbers, need to find associated Actors
            targets = [self._state.get_actor_by_number(target) for target in actor.targets]
            
            ACTION_EVENTS = GameEventGroup()
            actor.action(targets)
            
            print("action_events", ACTION_EVENTS)
            if ACTION_EVENTS.events:
                print('hereeee')
                # copy = 
                self._events.new_event_group(deepcopy(ACTION_EVENTS))
                
        # Regenerate possible targets
        self._state.generate_allies_and_possible_targets()
        
        print('Events', json.dumps(self._events.dump(), indent=4))
                
    
    @property
    def actors(self):
        self._state.generate_allies_and_possible_targets()
        return [actor.state for actor in self._state.actors]
        
    @property
    def state(self):
        return self._state.dump()