import engine as Mafia
import json
import random

def create():
    players = [
        {
            "id":  "1",
            "name": "Player 1",
            "alias": "Jackson",
            "roleActions": {
                "remainingVests": 100
            }
        },
        {
            "id": "2",
            "name": "Player 2",
            "alias": "Brandon"
        },
        {
            "id": "3",
            "name": "Player 3",
            "alias": "Bronson"
        },
        {
            "id": "4",
            "name": "Player 4",
            "alias": "Wesley"
        },
        {
            "id": "5",
            "name": "Player 5",
            "alias": "Rory"
        },
        {
            "id": "6",
            "name": "Player 6",
            "alias": "Kody"
        },
        {
            "id": "7",
            "name": "Player 7",
            "alias": "Dinkle"
        },
        {
            "id": "8",
            "name": "Player 8",
            "alias": "Gorden"
        },
        {
            "id": "9",
            "name": "Player 9",
            "alias": "Scrooge"
        },
        {
            "id": "10",
            "name": "Player 10",
            "alias": "Bertha"
        },
        {
            "id": "11",
            "name": "Player 11",
            "alias": "Brett"
        },
        {
            "id": "12",
            "name": "Player 12",
            "alias": "Muck"
        },
        {
            "id": "13",
            "name": "Player 13",
            "alias": "Mick"
        },
        {
            "id": "14",
            "name": "Player 14",
            "alias": "Dog"
        },
        {
            "id": "15",
            "name": "Player 15",
            "alias": "Car"
        }
    ]
    config = {
        "tags": [
            "town_government", 
            "town_protective", 
            "town_protective", 
            "town_power", 
            "town_investigative", 
            "town_killing", 
            "town_investigative", 
            "town_random", 
            "mafia_killing",
            "mafia_deception",
            "mafia_support",
            "neutral_evil",
            "neutral_benign",
            "neutral_random",
            "any_random"
        ],
        "settings": {},
        "roles": {
            "Citizen": {
                "max": 1,
                "weight": 1,
                "settings": {
                    "maxVests": 2
                }
            },
            "Mayor": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Doctor": {
                "max": 1,
                "weight": 1,
                "settings": {

                }
            },
            "Detective": {
                "max": 1,
                "weight": 1,
                "settings": {}
            },
            "Bodyguard": {
                "max": 1,
                "weight": 1,
                "settings": {

                }
            },
            # "Escort": {
            #     "max": 0,
            #     "weight": 1,
            #     "settings": {

            #     }
            # },
            # "Sheriff": {
            #     "max": 0,
            #     "weight": 1,
            #     "settings": {

            #     }
            # },
            # "Investigator": {
            #     "max": 0,
            #     "weight": 1,
            #     "settings": {

            #     }
            # },
            "Mafioso": {
                "max": 1,
                "weight": 1,
                "settings": {

                }
            },
            # "Consort": {
            #     "max": 0,
            #     "weight": 1,
            #     "settings": {

            #     }
            # },
            # "Janitor": {
            #     "max": 0,
            #     "weight": 1,
            #     "settings": {

            #     }
            # },
            # "Survivor": {
            #     "max": 0,
            #     "weight": 1,
            #     "settings": {

            #     }
            # },
            # "SerialKiller": {
            #     "max": 0,
            #     "weight": 1,
            #     "settings": {

            #     }
            # },
            # "Enforcer": {
            #     "max": 0,
            #     "weight": 1,
            #     "settings": {

            #     }
            # }
        }
    }

    # Build the initial game state
    game = Mafia.new_game(players, config)
    
    # Message all players their roles
    for actor in game.actors:
        print(actor)
        # print(f"({actor.player['id']}) {actor.alias}, you have been assigned the role {actor.role_name}. {actor.state}")
        
    print(game.actors)
        
    print('The starting game state saved to dynamo is', game.state.json())
    
def load():
    players = [
        {
            "id": "8",
            "name": "Player 8",
            "alias": "Gorden",
            "role": "Citizen",
            "number": 2,
            "alive": True,
            "possible_targets": [
                [
                    2
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "14",
            "name": "Player 14",
            "alias": "Dog",
            "role": "Citizen",
            "number": 3,
            "alive": True,
            "possible_targets": [
                [
                    3
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "1",
            "name": "Player 1",
            "alias": "Jackson",
            "role": "Citizen",
            "number": 4,
            "alive": True,
            "possible_targets": [
                [
                    4
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "9",
            "name": "Player 9",
            "alias": "Scrooge",
            "role": "Citizen",
            "number": 5,
            "alive": True,
            "possible_targets": [
                [
                    5
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "5",
            "name": "Player 5",
            "alias": "Rory",
            "role": "Citizen",
            "number": 6,
            "alive": True,
            "possible_targets": [
                [
                    6
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "12",
            "name": "Player 12",
            "alias": "Muck",
            "role": "Citizen",
            "number": 7,
            "alive": True,
            "possible_targets": [
                [
                    7
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "7",
            "name": "Player 7",
            "alias": "Dinkle",
            "role": "Citizen",
            "number": 8,
            "alive": True,
            "possible_targets": [
                [
                    8
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "10",
            "name": "Player 10",
            "alias": "Bertha",
            "role": "Citizen",
            "number": 9,
            "alive": True,
            "possible_targets": [
                [
                    9
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "6",
            "name": "Player 6",
            "alias": "Kody",
            "role": "Citizen",
            "number": 10,
            "alive": True,
            "possible_targets": [
                [
                    10
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "15",
            "name": "Player 15",
            "alias": "Car",
            "role": "Citizen",
            "number": 11,
            "alive": True,
            "possible_targets": [
                [
                    11
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "13",
            "name": "Player 13",
            "alias": "Mick",
            "role": "Citizen",
            "number": 12,
            "alive": True,
            "possible_targets": [
                [
                    12
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "3",
            "name": "Player 3",
            "alias": "Bronson",
            "role": "Citizen",
            "number": 13,
            "alive": True,
            "possible_targets": [
                [
                    13
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "4",
            "name": "Player 4",
            "alias": "Wesley",
            "role": "Citizen",
            "number": 14,
            "alive": True,
            "possible_targets": [
                [
                    14
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "11",
            "name": "Player 11",
            "alias": "Brett",
            "role": "Citizen",
            "number": 15,
            "alive": True,
            "possible_targets": [
                [
                    15
                ]
            ],
            "targets": [],
            "allies": []
        }
    ]
    state = {
        "day": 1,
        "players": [
            {
                "number": 1,
                "alias": "Brandon",
                "alive": False
            },
            {
                "number": 2,
                "alias": "Gorden",
                "alive": True
            },
            {
                "number": 3,
                "alias": "Dog",
                "alive": True
            },
            {
                "number": 4,
                "alias": "Jackson",
                "alive": True
            },
            {
                "number": 5,
                "alias": "Scrooge",
                "alive": True
            },
            {
                "number": 6,
                "alias": "Rory",
                "alive": True
            },
            {
                "number": 7,
                "alias": "Muck",
                "alive": True
            },
            {
                "number": 8,
                "alias": "Dinkle",
                "alive": True
            },
            {
                "number": 9,
                "alias": "Bertha",
                "alive": True
            },
            {
                "number": 10,
                "alias": "Kody",
                "alive": True
            },
            {
                "number": 11,
                "alias": "Car",
                "alive": True
            },
            {
                "number": 12,
                "alias": "Mick",
                "alive": True
            },
            {
                "number": 13,
                "alias": "Bronson",
                "alive": True
            },
            {
                "number": 14,
                "alias": "Wesley",
                "alive": True
            },
            {
                "number": 15,
                "alias": "Brett",
                "alive": True
            }
        ],
        "graveyard": [
            {
                "number": 1,
                "alias": "Brandon",
                "deathReason": 'Terminal Fiths'
            },
        ]
    }
    config = {
        "tags": [
            "town_government", 
            "town_protective", 
            "town_protective", 
            "town_power", 
            "town_investigative", 
            "town_killing", 
            "town_investigative", 
            "town_random", 
            "mafia_killing",
            "mafia_deception",
            "mafia_support",
            "neutral_evil",
            "neutral_benign",
            "neutral_random",
            "any_random"
        ],
        "settings": {},
        "roles": {
            "Citizen": {
                "max": 1,
                "weight": 1,
                "settings": {
                    "maxVests": 2
                }
            },
            "Mayor": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Doctor": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Bodyguard": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Escort": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Sheriff": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Investigator": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Mafioso": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Consort": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Janitor": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Survivor": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "SerialKiller": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
        }
    }
    
    game = Mafia.load_game(players, state, config)
    
    print(game.dump_state())

def load_lynch():
    players = [
        {
            "id": "8",
            "name": "Player 8",
            "alias": "Gorden",
            "role": "Citizen",
            "number": 2,
            "alive": True,
            "possible_targets": [
                [
                    2
                ]
            ],
            "targets": [],
            "allies": []
        }
    ]

    state = {
        "day": 1,
        "players": [
            {
                "number": 2,
                "alias": "Gordon",
                "alive": True
            },
        ],
        "graveyard": [
            {
                "number": 1,
                "alias": "Brandon",
                "deathReason": 'Terminal Fiths'
            },
        ]
    }

    config = {
        "tags": [
            "town_government", 
        ],
        "settings": {},
        "roles": {
            "Citizen": {
                "max": 1,
                "weight": 1,
                "settings": {
                    "maxVests": 2
                }
            }
        }
    }

    game = Mafia.load_game(players, state, config)

    game.lynch(2)

    print(game.dump_state())
    
def create_unbalanced():
    players = [
        {
            "id":  "1",
            "name": "Player 1",
            "alias": "Jackson",
            "roleActions": {
                "remainingVests": 100
            }
        },
        {
            "id": "2",
            "name": "Player 2",
            "alias": "Brandon"
        }
    ]
    config = {
        "tags": [
            "town_government", 
            "town_protective", 
            "town_protective", 
            "town_power", 
            "town_investigative", 
            "town_killing", 
            "town_investigative", 
            "town_random", 
            "godfather",
            "mafia_killing",
            "mafia_killing",
            "neutral_evil",
            "neutral_benign",
            "neutral_random",
            "any_random"
        ],
        "settings": {
            # TODO: Add durations here
        },
        "roles": {
            "Citizen": {
                "max": 0,
                "weight": 0.01,
                "settings": {
                    "maxVests": 2
                }
            },
            "Mayor": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Doctor": {
                "max": 2,
                "weight": 1,
                "settings": {

                }
            },
            "Bodyguard": {
                "max": 2,
                "weight": 1,
                "settings": {

                }
            },
            "Escort": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Sheriff": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Investigator": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Mafioso": {
                "max": 2,
                "weight": 1,
                "settings": {
                    "promotes": False
                }
            },
            "Godfather": {
                "max": 1,
                "weight": 1,
                "settings": {
                    "nightImmune": True
                }
            },
            "Consort": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Survivor": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "SerialKiller": {
                "max": 0,
                "weight": 1,
                "settings": {
                    "nightImmune": True
                }
            }
        }
    }

    # Build the initial game state
    try:
        game = Mafia.new_game(players, config)
    except Mafia.AssConfigException as e:
        print('[ERROR] AssConfigException: Unable to generate a viable game')

def resolve():
    players = [
        {
            "id": "1",
            "name": "Player 1",
            "alias": "BDogs",
            "role": "Godfather",
            "number": 1,
            "alive": True,
            "possible_targets": [
                [
                    3
                ]
            ],
            "targets": [3],
            "allies": []
        },
        {
            "id": "2",
            "name": "Player 2",
            "alias": "Gorden",
            "role": "Citizen",
            "number": 2,
            "alive": False,
            "possible_targets": [
                [
                    2
                ]
            ],
            "targets": [2],
            "allies": []
        },
        {
            "id": "3",
            "name": "Player 3",
            "alias": "Dog",
            "role": "Citizen",
            "number": 3,
            "alive": True,
            "possible_targets": [
                [
                    3
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "4",
            "name": "Player 4",
            "alias": "Jyackson",
            "role": "Doctor",
            "number": 4,
            "alive": True,
            "possible_targets": [
                [
                    4
                ]
            ],
            "targets": [
                8
            ],
            "allies": []
        },
        {
            "id": "5",
            "name": "Player 5",
            "alias": "Scrooge",
            "role": "Citizen",
            "number": 5,
            "alive": True,
            "possible_targets": [
                [
                    5
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "6",
            "name": "Player 6",
            "alias": "Guff",
            "role": "Mafioso",
            "number": 6,
            "alive": True,
            "possible_targets": [
                [
                    6
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "7",
            "name": "Player 7",
            "alias": "Muck",
            "role": "Detective",
            "number": 7,
            "alive": True,
            "possible_targets": [
                [
                    1
                ]
            ],
            "targets": [6],
            "allies": []
        },
        {
            "id": "8",
            "name": "Player 8",
            "alias": "Dinkle",
            "role": "Bodyguard",
            "number": 8,
            "alive": True,
            "possible_targets": [
                [
                    8
                ]
            ],
            "targets": [3],
            "allies": []
        },
        {
            "id": "9",
            "name": "Player 9",
            "alias": "Bertha",
            "role": "Citizen",
            "number": 9,
            "alive": True,
            "possible_targets": [
                [
                    9
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "10",
            "name": "Player 10",
            "alias": "Kod",
            "role": "Citizen",
            "number": 10,
            "alive": True,
            "possible_targets": [
                [
                    10
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "11",
            "name": "Player 11",
            "alias": "Car",
            "role": "Citizen",
            "number": 11,
            "alive": True,
            "possible_targets": [
                [
                    11
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "12",
            "name": "Player 12",
            "alias": "Mick",
            "role": "Citizen",
            "number": 12,
            "alive": True,
            "possible_targets": [
                [
                    12
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "13",
            "name": "Player 13",
            "alias": "Girthy",
            "role": "Citizen",
            "number": 13,
            "alive": True,
            "possible_targets": [
                [
                    13
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "14",
            "name": "Player 14",
            "alias": "Imp",
            "role": "Citizen",
            "number": 14,
            "alive": True,
            "possible_targets": [
                [
                    14
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "15",
            "name": "Player 15",
            "alias": "Brett",
            "role": "Citizen",
            "number": 15,
            "alive": True,
            "possible_targets": [
                [
                    15
                ]
            ],
            "targets": [],
            "allies": []
        }
    ]
    state = {
        "day": 1,
        "players": [
            {
                "number": 1,
                "alias": "BDogs",
                "alive": False
            },
            {
                "number": 2,
                "alias": "Gorden",
                "alive": True
            },
            {
                "number": 3,
                "alias": "Dog",
                "alive": True
            },
            {
                "number": 4,
                "alias": "Jyackson",
                "alive": True
            },
            {
                "number": 5,
                "alias": "Scrooge",
                "alive": True
            },
            {
                "number": 6,
                "alias": "Guff",
                "alive": True
            },
            {
                "number": 7,
                "alias": "Muck",
                "alive": True
            },
            {
                "number": 8,
                "alias": "Dinkle",
                "alive": True
            },
            {
                "number": 9,
                "alias": "Bertha",
                "alive": True
            },
            {
                "number": 10,
                "alias": "Kod",
                "alive": True
            },
            {
                "number": 11,
                "alias": "Car",
                "alive": True
            },
            {
                "number": 12,
                "alias": "Mick",
                "alive": True
            },
            {
                "number": 13,
                "alias": "Girthy",
                "alive": True
            },
            {
                "number": 14,
                "alias": "Imp",
                "alive": True
            },
            {
                "number": 15,
                "alias": "Brett",
                "alive": True
            }
        ],
        "graveyard": [
            {
                "number": 1,
                "alias": "Brandon",
                "deathReason": 'Terminal Fiths',
                "role": "Citizen",
                "will": "And I oop"
            },
        ]
    }
    config = {
        "tags": [
            "town_government", 
            "town_protective", 
            "town_protective", 
            "town_power", 
            "town_investigative", 
            "town_killing", 
            "town_investigative", 
            "town_random", 
            "mafia_killing",
            "mafia_deception",
            "mafia_support",
            "neutral_evil",
            "neutral_benign",
            "neutral_random",
            "any_random"
        ],
        "settings": {},
        "roles": {
            "Citizen": {
                "max": 1,
                "weight": 1,
                "settings": {
                    "maxVests": 2
                }
            },
            "Mayor": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Doctor": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Bodyguard": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Escort": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Sheriff": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Detective": {
                "max": 1,
                "weight": 1,
                "settings": {

                }
            },
            "Godfather": {
                "max": 1,
                "weight": 1,
                "settings": {

                }
            },
            "Mafioso": {
                "max": 3,
                "weight": 1,
                "settings": {

                }
            },
            "Consort": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Janitor": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Survivor": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "SerialKiller": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Enforcer": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            }
        }
    }
    
    game = Mafia.load_game(players, state, config)

    game.resolve()
    
    print(json.dumps(game.events.dump(), indent=4))
    print('Total events duration:', game.events.duration)
    
    
    state = game.dump_state()

    print(len(state['players']))
    # print(game.dump_state())
def simulate():
    players = [
        {
            "id": "1",
            "name": "Player 1",
            "alias": "Brandon",
            "role": "Godfather",
            "number": 1,
            "alive": True,
            "possible_targets": [
                [
                    3
                ]
            ],
            "targets": [3],
            "allies": []
        },
        {
            "id": "2",
            "name": "Player 2",
            "alias": "Gorden",
            "role": "Citizen",
            "number": 2,
            "alive": True,
            "possible_targets": [
                [
                    2
                ]
            ],
            "targets": [2],
            "allies": []
        },
        {
            "id": "3",
            "name": "Player 3",
            "alias": "Dog",
            "role": "Citizen",
            "number": 3,
            "alive": True,
            "possible_targets": [
                [
                    3
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "4",
            "name": "Player 4",
            "alias": "Jackson",
            "role": "Doctor",
            "number": 4,
            "alive": True,
            "possible_targets": [
                [
                    4
                ]
            ],
            "targets": [
                3
            ],
            "allies": []
        },
        {
            "id": "5",
            "name": "Player 5",
            "alias": "Scrooge",
            "role": "Doctor",
            "number": 5,
            "alive": True,
            "possible_targets": [
                [
                    5
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "6",
            "name": "Player 6",
            "alias": "Rory",
            "role": "Mafioso",
            "number": 6,
            "alive": True,
            "possible_targets": [
                [
                    6
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "7",
            "name": "Player 7",
            "alias": "Muck",
            "role": "Doctor",
            "number": 7,
            "alive": True,
            "possible_targets": [
                [
                    7
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "8",
            "name": "Player 8",
            "alias": "Dinkle",
            "role": "Citizen",
            "number": 8,
            "alive": True,
            "possible_targets": [
                [
                    8
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "9",
            "name": "Player 9",
            "alias": "Bertha",
            "role": "Citizen",
            "number": 9,
            "alive": True,
            "possible_targets": [
                [
                    9
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "10",
            "name": "Player 10",
            "alias": "Kody",
            "role": "Citizen",
            "number": 10,
            "alive": True,
            "possible_targets": [
                [
                    10
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "11",
            "name": "Player 11",
            "alias": "Car",
            "role": "Citizen",
            "number": 11,
            "alive": True,
            "possible_targets": [
                [
                    11
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "12",
            "name": "Player 12",
            "alias": "Mick",
            "role": "Citizen",
            "number": 12,
            "alive": True,
            "possible_targets": [
                [
                    12
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "13",
            "name": "Player 13",
            "alias": "Bronson",
            "role": "Citizen",
            "number": 13,
            "alive": True,
            "possible_targets": [
                [
                    13
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "14",
            "name": "Player 14",
            "alias": "Wesley",
            "role": "Citizen",
            "number": 14,
            "alive": True,
            "possible_targets": [
                [
                    14
                ]
            ],
            "targets": [],
            "allies": []
        },
        {
            "id": "15",
            "name": "Player 15",
            "alias": "Brett",
            "role": "Citizen",
            "number": 15,
            "alive": True,
            "possible_targets": [
                [
                    15
                ]
            ],
            "targets": [],
            "allies": []
        }
    ]
    state = {
        "day": 1,
        "players": [
            {
                "number": 1,
                "alias": "Brandon",
                "alive": True
            },
            {
                "number": 2,
                "alias": "Gorden",
                "alive": True
            },
            {
                "number": 3,
                "alias": "Dog",
                "alive": True
            },
            {
                "number": 4,
                "alias": "Jackson",
                "alive": True
            },
            {
                "number": 5,
                "alias": "Scrooge",
                "alive": True
            },
            {
                "number": 6,
                "alias": "Rory",
                "alive": True
            },
            {
                "number": 7,
                "alias": "Muck",
                "alive": True
            },
            {
                "number": 8,
                "alias": "Dinkle",
                "alive": True
            },
            {
                "number": 9,
                "alias": "Bertha",
                "alive": True
            },
            {
                "number": 10,
                "alias": "Kody",
                "alive": True
            },
            {
                "number": 11,
                "alias": "Car",
                "alive": True
            },
            {
                "number": 12,
                "alias": "Mick",
                "alive": True
            },
            {
                "number": 13,
                "alias": "Bronson",
                "alive": True
            },
            {
                "number": 14,
                "alias": "Wesley",
                "alive": True
            },
            {
                "number": 15,
                "alias": "Brett",
                "alive": True
            }
        ],
        "graveyard": []
    }
    config = {
        "tags": [
            "town_government", 
            "town_protective", 
            "town_protective", 
            "town_power", 
            "town_investigative", 
            "town_killing", 
            "town_investigative", 
            "town_random", 
            "mafia_killing",
            "mafia_deception",
            "mafia_support",
            "neutral_evil",
            "neutral_benign",
            "neutral_random",
            "any_random"
        ],
        "settings": {},
        "roles": {
            "Citizen": {
                "max": 1,
                "weight": 1,
                "settings": {
                    "maxVests": 2
                }
            },
            "Mayor": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Doctor": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Bodyguard": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Escort": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Sheriff": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Investigator": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Godfather": {
                "max": 1,
                "weight": 1,
                "settings": {

                }
            },
            "Mafioso": {
                "max": 3,
                "weight": 1,
                "settings": {

                }
            },
            "Consort": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Janitor": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Survivor": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "SerialKiller": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Enforcer": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            }
        }
    }
    
    # game = Mafia.load_game(players, state, config)

    # while not game.check_for_win():
    for j in range(150):
        game = Mafia.load_game(players, state, config)
        # game.state.generate_allies_and_possible_targets()
        for actor in game.state.actors:
            
            targets = []
            for i, p_targets in enumerate(actor.possible_targets):
                targets.insert(i, random.choice(p_targets))
            actor.set_targets(targets)
        game.resolve()
        
        print('Graveyard', len(game.state.graveyard))
        
        players = game.actors
        state = game.state.json()
        if game.check_for_win(): 
            print("Game over on turn", j)
            break

    # print(json.dumps(players, indent=4))
    # print(json.dumps(state, indent=4))
    
    
    
    # print(json.dumps(game.events.dump(), indent=4))
    print('Winners', game.check_for_win())
    # print('Total events duration:', game.events.duration)
    # print('Graveyard', len(game.state.graveyard))
    # print("Alive", game.state.alive_actors)
    print('State', json.dumps(game.dump_state(), indent=4))


def test():
    players = [{'id': '297e2488-a011-70d3-37fe-7726fc204909', 'createdAt': 1689715773448, 'name': 'UncleGenghi', 'alive': True, 'gameId': '9cf2712e-40c1-4a41-8893-af732ad484d1', 'alias': 'UncleGenghi', 'role': 'Godfather', 'possible_targets': [[1]], 'number': 1, 'targets': [], 'allies': [], 'type': 'GAME_ACTOR'}, {'id': '79ae6438-a0f1-702d-dcb3-e86eff713c10', 'createdAt': 1689715773448, 'name': 'User 2', 'alive': True, 'gameId': '9cf2712e-40c1-4a41-8893-af732ad484d1', 'alias': 'User 2', 'role': 'Citizen', 'possible_targets': [[1]], 'number': 2, 'targets': [], 'allies': [], 'type': 'GAME_ACTOR'}]
    state = {'day': 1, 'players': [{'number': 1, 'alias': 'UncleGenghi', 'alive': True}, {'number': 2, 'alias': 'User 2', 'alive': True}], 'graveyard': []}
    config = {
        "tags": [
            "town_government", 
            "town_protective", 
            "town_protective", 
            "town_power", 
            "town_investigative", 
            "town_killing", 
            "town_investigative", 
            "town_random", 
            "mafia_killing",
            "mafia_deception",
            "mafia_support",
            "neutral_evil",
            "neutral_benign",
            "neutral_random",
            "any_random"
        ],
        "settings": {},
        "roles": {
            "Citizen": {
                "max": 1,
                "weight": 1,
                "settings": {
                    "maxVests": 2
                }
            },
            "Doctor": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Bodyguard": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Escort": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Sheriff": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Investigator": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            },
            "Godfather": {
                "max": 1,
                "weight": 1,
                "settings": {

                }
            },
            "Mafioso": {
                "max": 3,
                "weight": 1,
                "settings": {

                }
            },
        }
    }
    
    game = Mafia.load_game(players, state, config)
    
    winners = game.check_for_win()

    print(winners)

if __name__=='__main__':
    create_unbalanced()