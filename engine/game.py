from __future__ import annotations
from typing import List
import random
import json
import copy

from engine.utils.logger import logger

from engine.game_save import GameSave
from engine.game_state import GameState
from engine.events import ACTION_EVENTS, GameEventGroup

import engine.roles as roles


class Game:
    def __init__(self) -> None:
        self.save: GameSave = None
        self.state = None
        self.roles: list = None
        self.failed_roles: list = None
        self.events = GameEventGroup(group_id='root')
        
    @property
    def actors(self) -> dict:
        return [actor.state for actor in self.state.actors]
          
    def new(self, players: List[dict], config: dict) -> Game:
        logger.info('--- Creating a new Game ---')
        logger.info("Players: {}".format(players))
        
        self.save = GameSave(config=config)
        self.roles, self.failed_roles = self.save.generate_roles()
        
        # Assign roles and numbers to players
        random.shuffle(players)
        random.shuffle(self.save.roles)
        
        # Allocate roles
        logger.info("--- Allocating roles ---")
        for index, player in enumerate(players):
            player['role'] = self.save.roles[index]
            logger.info(f"  |-> {player['alias']} ({player['name']}):".ljust(40) + f" {player['role']}")
        
        # Generate GameState
        logger.info("--- Generating initial GameState ---")
        self.state = GameState().new(players, self.save.roles_settings)
        
        return self
    
    def load(self, players, state, config) -> Game:
        logger.info('--- Loading Game ---')
        logger.info("Players: {}".format(players))
        logger.info("GameState: {}".format(state))
        
        self.save = GameSave(config=config)
        
        # Generate GameState
        self.state = GameState().load(players, state, self.save.roles_settings)
        
        return self
    
    def resolve(self):
        ''' Resolve all player actions'''
        logger.info("--- Resolving all player actions ---")
        self.state.day += 1
        
        self.state.generate_allies_and_possible_targets()
        
        # sort the actors based on TURN_ORDER
        self.state.actors.sort(key=lambda actor: roles.TURN_ORDER.index(actor.role_name))
        
        # Prelim check to ensure that players are only targetting valid options
        # This needs to happen BEFORE resolution as Witch can then fuck with the targetting as intended
        for actor in self.state.actors:
            if not actor.targets or not actor.possible_targets: continue
            for i, target in enumerate(actor.targets):
                p_targets = [p_target.number for p_target in actor.possible_targets[i]]
                if target in p_targets: continue
                actor.targets = None
                break
        
        # Resolve all actions for the day
        for actor in self.state.actors:
            if not actor.targets: continue
            
            # The targets are just numbers, need to find associated Actors
            targets = [self.state.get_actor_by_number(target) for target in actor.targets]
            logger.info(f"{actor} is targetting {targets}")
            
            # Initialise the events group for this action
            ACTION_EVENTS.reset(new_id=f"{'_'.join(actor.role_name.lower().split(' '))}_action")
            actor.action(targets)
            if ACTION_EVENTS.events:
                self.events.new_event_group(copy.deepcopy(ACTION_EVENTS))
            
            
    def check_for_win(self): # TODO
        return [actor for actor in self.state.actors if actor.check_for_win(self.state.alive_actors)]
        
    
    def dump_state(self) -> dict:
        return self.state.json()
        