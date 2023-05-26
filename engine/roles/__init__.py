from enum import Enum

from engine.roles.actor import Actor
from engine.roles.citizen import Citizen
from engine.roles.mafioso import Mafioso
from engine.roles.doctor import Doctor

class Alignment(Enum):
    TOWN = "Town"
    MAFIA = "Mafia"
    
ROLE_TAGS = {
    # TOWN
    "Citizen"       : ["any_random", "town_random", "town_government"],
    # "Mayor"         : ["any_random", "town_random", "town_government"],
    "Doctor"        : ["any_random", "town_random", "town_protective"],
    # "Bodyguard"     : ["any_random", "town_random", "town_protective", "town_killing"],
    # "Escort"        : ["any_random", "town_random", "town_protective", "town_power"],
    # "Lookout"       : ["any_random", "town_random", "town_investigative"],
    # "Sheriff"       : ["any_random", "town_random", "town_investigative"],
    # "Investigator"  : ["any_random", "town_random", "town_investigative"],
    # MAFIA
    "Mafioso"       : ["any_random", "mafia_random", "mafia_killing"],
    # "Consort"       : ["any_random", "mafia_random", "mafia_support"],
    # "Janitor"       : ["any_random", "mafia_random", "mafia_deception"],
    # TRIAD
    # "Enforcer"      : ["any_random", "triad_random", "triad_killing"],
    # CULT
    # NEUTRAL
    # "Survivor"      : ["any_random", "neutral_random", "neutral_benign"],
    # "SerialKiller" : ["any_random", "neutral_random", "neutral_evil", "neutral_killing"],    
}

TURN_ORDER = [
    # Roleblocking
    "Consort",
    "Escort",
    # Self Protecting
    "Citizen",
    # Target Protecting
    "Doctor",
    "Bodyguard",
    # Killing
    "Mafioso",
    # Investigative
    "Lookout"
]