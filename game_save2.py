from dataclasses import dataclass
import random

from logger import logger
from consts import ROLE_TAGS


@dataclass
class GameSave():
    def __init__(self, config: dict):
        self.config = config
        self.settings = config['settings']
        self.roles_settings = config['roles']
        self.tags = config['tags']
        
    def generate_roles(self):
        logger.info("--- Generating roles ---")
        logger.info("Tags: {}".format(self.tags))
        failed_roles = 0
        
        # Construct a list of all possible options for each specified tag
        role_options = []
        for tag in self.tags:
            possible_roles = []
            for role in self.roles_settings:
                if (role in ROLE_TAGS and tag in ROLE_TAGS[role]) or tag == role:
                    weight = self.roles_settings[role]['weight']
                    max = self.roles_settings[role]['max']
                    possible_roles.append((role, weight, max))
            role_options.append((tag, possible_roles))
            
        # Sort the (tag, [roles]) tuples by increasing len([roles]),
        # this means that tags with only a single valid valid outcome have a higher chance of succeeding
        role_options = sorted(role_options, key=lambda option: len(option[1]))
        
        # Loop through and select roles
        selected_roles = []
        blacklist = []
        
        for option in role_options:
            # 'option' = ('town_random', [('citizen', 5, 1), ('doctor', 1, 4)])
            #          = (tag, [(role, weight, max), etc...])
            
            # Update the blacklist
            for role in self.roles_settings:
                if selected_roles.count(role) == self.roles_settings[role]['max'] and role not in blacklist:
                    logger.info(f"\tMax reached for '{role}' -> adding to blacklist")
                    blacklist.append(role)
                    # Remove the role from all remaining options
                    for option_index, role_option in enumerate(role_options):
                        for role_index, remaining_role in enumerate(role_option[1]):
                            if remaining_role[0] == role:
                                logger.info("\t\tDeleting role '{}' from '{}'".format(role_options[option_index][1][role_index][0], role_options[option_index][0]))
                                del role_options[option_index][1][role_index]
                    
            # sort again
            role_options = sorted(role_options, key=lambda option: len(option[1]))

            # remove roles that are in the blacklist
            available_roles = [role for role in role_options[0][1] if role[0] not in blacklist]
            
            # Pick a weighted random choice
            roles = [option[0] for option in available_roles]
            weights = [option[1] for option in available_roles]

            # for i in range(100):
            if len(available_roles) == 0:
                # logger.info("\tUnable to select free role, failing to 'citizen'")
                choice = "Citizen"
                logger.warning(f"Picking {role_options[0][0]}: {choice} \t<--- FAILED!!!")
                failed_roles+=1
            else:
                choice = random.choices(roles, weights=weights, k=1)[0]
                logger.info(f"Picking {role_options[0][0]}: {choice}")
                
            selected_roles.append(choice)
            
            del role_options[0] # Remove the tag from the list
        
        
        self.roles = selected_roles
        self.failed_roles = failed_roles
        if failed_roles > 0: logger.warning(f"Number of failures: {failed_roles}")
        logger.info(f'Roles: {selected_roles}')
        return selected_roles, failed_roles
    