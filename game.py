import random


from game_save2 import GameSave
from game_state2 import GameState

from logger import logger



class Game():
    def __init__(self) -> None:
        self.save = None
        self.state = None
        pass
    
    def new(self, players: list, save: dict):
        logger.info("--- Creating Game ---")
        logger.info("Players: {}".format(len(players)))
        
        
        self.save = GameSave(save)
        
        # self.state = GameState().new()
        
        self.roles, self.failed_roles = self.save.generate_roles()
        
        # Assign roles and numbers to players
        random.shuffle(players)
        random.shuffle(self.save.roles)
        
        # Allocate roles
        logger.info("--- Allocating roles ---")
        for index, player in enumerate(players):
            player['role'] = self.save.roles[index]
            logger.info(f"\t|-> {player['alias']} ({player['name']}):\t\t{player['role']}")
        
        # Generate GameState
        logger.info("--- Generating initial GameState ---")
        self.state = GameState().from_lobby(players, self.save.roles_settings)
        
        
        '''
        Assign roles to players
        convert player-role pairs to Actors
        generate allies and possible targets
        
        '''
        
        return self