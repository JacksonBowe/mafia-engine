import random
from typing import List
from engine.roles import import_role, Actor
from engine.models import Player, GameConfig, GameState

from engine.utils.logger import logger
class Game:
    def __init__(self, day: int, players: List[Player], config: GameConfig):
        self.day = day
        self.config = config
        self.actors: List[Actor] = []
        self._graveyard = []
        
        logger.info("Importing required roles and instantiating actors")
        for index, player in enumerate(players):
            Role = import_role(player.role)
            # Instantiate a Role class with a :player and :roles_settings[role]
            actor = Role(player, config.roles[player.role].settings)
            self.actors.append(actor)
            
        self.generate_allies_and_possible_targets()
    
    @classmethod
    def new(cls, players: List[Player], config: GameConfig):
        logger.info('--- Creating a new Game ---')
        logger.info("Players: {}".format(players))
        
        roles, failures = config.generate_roles()
        
        # Assign rules and numbers to players
        random.shuffle(players)
        random.shuffle(roles)
        
        # Ensure that there are equal roles to players, pad roles with 'Citizen'
        if len(players) > len(roles):
            roles.extend(['Citizen'] * (len(players) - len(roles)))

        # Allocate roles
        logger.info("--- Allocating roles ---")
        for index, player in enumerate(players):
            player.number = index + 1
            player.role = roles[index]
            logger.info(f"  |-> {player.alias} ({player.name}):".ljust(40) + f" {player.role}")    
    
        return cls(1, players, config)
    
    @classmethod
    def load(cls, players: List[Player], config: GameConfig, state: GameState):
        logger.info('--- Loading Game ---')
        logger.info("Players: {}".format(players))
        for player in players:
            logger.info(f"  |-> {player.alias} ({player.name}):".ljust(40) + f" {player.role} {'(DEAD)' if not player.alive else ''}") 
        
        g = cls(state.day, players, config)
        g._graveyard = state.graveyard
        
        for actor in g.actors:
            actor.set_targets([g.get_actor_by_number(target) for target in actor.player.targets])
    
        return g
    
    def generate_allies_and_possible_targets(self):
        for actor in self.alive_actors:
            actor.find_allies(self.actors)
            actor.find_possible_targets(self.actors)
    
    def resolve(self):
        pass
    
    def check_for_win(self):
        pass
    
    def get_actor_by_number(self, number: int) -> Actor:
        return next((actor for actor in self.actors if actor.number == number), None)
    
    @property
    def alive_actors(self) -> List[Actor]:
        return [actor for actor in self.actors if actor.alive]
    
    @property
    def dead_actors(self) -> List[Actor]:
        return [actor for actor in self.actors if not actor.alive]
    
    @property
    def graveyard(self) -> dict:
        return self._graveyard + [{
            'number': actor.number,
            'alias': actor.alias,
            'cod': 'actor.cod',
            'dod': 1,
            'role': 'actor.role_name',
            'will': 'actor.will'
        } for actor in self.dead_actors]
    
    def dump_state(self):
        return GameState(**{
            'day': self.day,
            'players': [{
                'number': actor.number,
                'alias': actor.alias,
                'alive': actor.alive,
            } for actor in self.actors],
            'graveyard': self.graveyard
        }).model_dump()
        
    def dump_actors(self):
        return [actor.dump_state() for actor in self.actors]