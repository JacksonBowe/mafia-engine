import random
from consts import ROLE_TAGS


class GameSave():
    def __init__(self, config: dict) -> None:
        self.config = config
        self.roles = self.select_roles()
        pass
    
    def select_roles(self):
        
        role_options = []
        for tag in self.config['tags']:
            role_options.append((tag, self.find_by_tag(tag)))

        # Sort the tag:[roles] tuples by increading len([roles]), 
        # this means that tags with only a single valid outcome have a higher chance of succeeding
        role_options = sorted(role_options, key=lambda option: len(option[1]))

        # Loop through and assign roles
        roles = []
        blacklist = []
        
        for option in role_options:
            # Update the blacklist
            for role in self.config['roles']:
                if roles.count(role) == self.config['roles'][role]['max'] and role not in blacklist:
                    print(f"Max reached for '{role}' -> adding to blacklist")
                    blacklist.append(role)
                    
            # sort again
            role_options = sorted(role_options, key=lambda option: len(option[1]))

            # remove roles that are in the blacklist
            available_roles = [role for role in role_options[0][1] if role[0] not in blacklist]
            
            # Pick a weighted random choice
            roles = [option[0] for option in available_roles]
            weights = [option[1] for option in available_roles]

            for i in range(100):
                if len(available_roles) == 0 or i == 99:
                    print("Unable to select free role, failing to 'citizen'")
                    choice = "citizen"
                    break
                choice = random.choices(roles, weights=weights, k=1)[0]
                if not choice in blacklist: break
                
            print(f"Picking {option[0]}: {choice}")
                
            del role_options[0]

        return 1
    
    def find_by_tag(self, tag):
        # get all the roles that have this tag along with their weight and max
        roles = []
        for role in ROLE_TAGS:
            if tag in ROLE_TAGS[role] or tag == role:
                weight = self.config['roles'][role]['weight']
                max = self.config['roles'][role]['max']
                roles.append((role, weight, max))
        return roles
    
    
    '''
    
    
    
    '''
    
    
    
    