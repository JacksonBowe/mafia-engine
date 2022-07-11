
ROLE_TAGS = {
    # TOWN
    "citizen"       : ["any_random", "town_random", "town_government"],
    "doctor"        : ["any_random", "town_random", "town_protective"],
    "bodyguard"     : ["any_random", "town_random", "town_protective", "town_killing"],
    "escort"        : ["any_random", "town_random", "town_protective", "town_power"],
    "sheriff"       : ["any_random", "town_random", "town_investigative"],
    "investigator"  : ["any_random", "town_random", "town_investigative"],
    # MAFIA
    "mafioso"       : ["any_random", "mafia_random", "mafia_killing"],
    "consort"       : ["any_random", "mafia_random", "mafia_support"],
    "janitor"       : ["any_random", "mafia_random", "mafia_deception"],
    # TRIAD
    "enforcer"      : ["any_random", "triad_random", "triad_killing"],
    # CULT
    # NEUTRAL
    "survivor"      : ["any_random", "neutral_random", "neutral_benign"],
    "serial_killer" : ["any_random", "neutral_random", "neutral_evil", "neutral_killing"],    
}