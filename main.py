import src.interface as Mafia

def main():
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
    save = {
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
    
    game = Mafia.create_game(players, save)
    
    print('Game', game)
    
    print('GameState', game.state)
    print('GameActors', game.state.actors)


if __name__=='__main__':
    main()