from typing import Set

from engine.roles.actor import Actor
from engine.roles.citizen import Citizen
from engine.roles.bodyguard import Bodyguard
from engine.roles.mafioso import Mafioso

# This is also turn order
ROLE_LIST: Set[Actor] = {
    # ---   Role Blocking       --- #
    
    # ---   Self Protecting     --- #
    Citizen,
    
    # ---   Target Protecting   --- #
    Bodyguard,
    # ---   Killing             --- #
    Mafioso
    # ---   Investigative       --- #
}

ROLE_TAGS_MAP = { role.__name__: role.tags for role in ROLE_LIST }