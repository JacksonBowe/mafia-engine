import engine as Mafia
import json

def create():
    players = [
        {
            "id":  "1",
            "name": "Player 1",
            "alias": "Jackson"
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
            "Enforcer": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            }
        }
    }

    # Build the initial game state
    game = Mafia.new_game(players, config)
    
    # Message all players their roles
    for actor in game.actors:
        print(actor)
        # print(f"({actor.player['id']}) {actor.alias}, you have been assigned the role {actor.role_name}. {actor.state}")
        
    print(game.actors)
    
    with open('t2.json', 'w') as f:
        json.dump(game.dump(), f)
        
    print('The starting game state saved to dynamo is', game.state.json())
    
def load():
    players = [
    {
        "id": "5",
        "name": "Player 5",
        "alias": "Rory",
        "role": "Citizen",
        "number": 1,
        "alive": True,
        "possible_targets": [
            [
                1
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
        "id": "8",
        "name": "Player 8",
        "alias": "Gorden",
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
        "id": "15",
        "name": "Player 15",
        "alias": "Car",
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
        "id": "7",
        "name": "Player 7",
        "alias": "Dinkle",
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
        "id": "14",
        "name": "Player 14",
        "alias": "Dog",
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
        "id": "13",
        "name": "Player 13",
        "alias": "Mick",
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
        "id": "11",
        "name": "Player 11",
        "alias": "Brett",
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
        "id": "4",
        "name": "Player 4",
        "alias": "Wesley",
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
        "id": "3",
        "name": "Player 3",
        "alias": "Bronson",
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
        "id": "1",
        "name": "Player 1",
        "alias": "Jackson",
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
        "id": "2",
        "name": "Player 2",
        "alias": "Brandon",
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
        "id": "10",
        "name": "Player 10",
        "alias": "Bertha",
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
        "id": "6",
        "name": "Player 6",
        "alias": "Kody",
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
        "id": "12",
        "name": "Player 12",
        "alias": "Muck",
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
            "Enforcer": {
                "max": 0,
                "weight": 1,
                "settings": {

                }
            }
        }
    }

    game = Mafia.load_game(players, config)
    

if __name__=='__main__':
    create()