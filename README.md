# Mafia Engine

This project contains the game logic for my serverless multiplayer game Mafia (the party game). To follow this project, check out the discord at <https://discord.gg/EcGx9h2fwy>

## About

For context, my game consists of (currently) two seperate repos.

The primary codebase(private) contains everything nessesary to run and deploy game. It handles all the communication between players, the hosting, the user authentication... all the boring "non-game" stuff.

The secondary codebase(this one) is responsible for all the game logic. My intention is to make the this repo into a general purpose Mafia package.

## Supported Roles

| Faction | Roles                                 |
| ------- | ------------------------------------- |
| Town    | Citizen, Doctor, Bodyguard, Detective |
| Mafia   | Godfather, Mafioso                    |
| Neutral | None                                  |

## How it works

> **Warning: Nerd shit ahead**

There are 3 primary functions that can be executed:

- new_game()
- load_game()
- resolve_game()

### New games

A Game is created with a list of players and a config file.

```python
players = [
    {
        "id": "{user_id}",
        "name": "Jackson",
        "alias": "Genghi"
    },
    ...
]

config = { # Typically an external file
    "tags": [
        "town_goverment",
        ...
    ],
    "roles": {
        "Citizen": {
            "max": 1,
            "weight": 1, # How likely is this role to be selected
            "settings": {
                "maxVests": 2 # Configerable role specific settings
        },
        ...
    }
}

import engine as Mafia

game = Mafia.new_game(players, config)
```

Using the config file a game is created and the role lineup chosen. Each player then gets assigned a role. Once a role has been assigned up to its maximum limit it is removed from the pool.  
If the engine cannot determine a valid role the default is Citizen.

The result looks like this:

```
# log.txt
--- Creating a new Game ---
Players: [{'id': '1', 'name': 'Player 1', 'alias': 'Jackson'}, ...
--- Generating roles ---
Tags: ['town_government', 'town_protective', 'town_protective', ...
Picking town_investigative: Detective
- Max reached for 'Detective'            -> adding to blacklist
-- Deleting role 'Detective' from 'town_investigative'
-- Deleting role 'Detective' from 'town_random'
-- Deleting role 'Detective' from 'any_random'
Picking town_investigative: Citizen      <--- FAILED!!!
Picking town_killing: Bodyguard
...

--- Allocating roles ---
  |-> Car (Player 15):                   Citizen
  |-> Gorden (Player 8):                 Citizen
  |-> Brandon (Player 2):                Doctor
  ...
```

Player and game state can then be extracted as JSON.

```python
players = game.actors
state = game.state.json
```

### Loading games

Not as interesting as creating a new Game. Takes in a new list of players (with whatever actions they've taken) and the _previous game state_.

### Resolving actions

Requires a game to be loaded with player actions. Resolves all the actions and returns a list of event groups, which contain events.

```py
@dataclass
class GameEvent:
    ''' What event was it, and who should it be broadcast to'''
    event_id: str
    targets: list
    message: str

    def dump(self):
        return asdict(self)

@dataclass
class GameEventGroup:
    ''' A Grouping of game events, eg. Broadcast event A to all players, and event B to select players'''
    group_id: str = None
    duration: Duration = Duration.ZERO
    events: List[Union[GameEvent, GameEventGroup]] = field(default_factory=list)
```

An example of the following scenario:

- Godfather choses to kill Citizen, sends a Mafioso
- Bodyguard choses to protect Citizen
- Doctor choses to heal Bodyguard
- Mafioso dies, Bodyguard is revived

```shell
# log.txt
--- Resolving all player actions ---
|Doctor| Jyackson(4) is targetting [|Bodyguard| Dinkle(8)]
|Doctor| Jyackson(4) will attempt to heal |Bodyguard| Dinkle(8)
|Doctor| Jyackson(4) is visiting |Bodyguard| Dinkle(8)'s house
|Bodyguard| Dinkle(8) is targetting [|Citizen| Dog(3)]
|Bodyguard| Dinkle(8) will protect |Citizen| Dog(3)
|Bodyguard| Dinkle(8) is visiting |Citizen| Dog(3)'s house
|Godfather| BDogs(1) is targetting [|Citizen| Dog(3)]
|Godfather| BDogs(1) has chosen |Mafioso| Guff(6) to act as a proxy
|Mafioso| Guff(6) is targetting [|Citizen| Dog(3)]
|Mafioso| Guff(6) is attempting to kill |Citizen| Dog(3)
|Mafioso| Guff(6) is visiting |Citizen| Dog(3)'s house
|Bodyguard| Dinkle(8) defends their target from |Mafioso| Guff(6)
|Doctor| Jyackson(4) revives |Bodyguard| Dinkle(8)
|Mafioso| Guff(6) died. Cause of death: Died in a shootout
```

```python
# Events
[
    {
        "group_id": "godfather_action",
        "duration": 0,
        "events": [
            {
                "group_id": "godfather_proxy",
                "duration": 0,
                "events": [
                    {
                        "event_id": "godfather_proxy_choice",
                        "targets": [
                            "1",
                            "6"
                        ],
                        "message": "The Godfather has chosed Guff to carry out the hit"
                    }
                ]
            }
        ]
    },
    {
        "group_id": "mafioso_action",
        "duration": 3, # Group duration is the sum of it's children
        "events": [
            {
                "group_id": "shootout",
                "duration": 3, # This action will take 3 seconds, play a sound file for that long...
                "events": [
                    {
                        "event_id": "bodyguard_shootout",
                        "targets": [
                            "*" # Inform all players
                        ],
                        "message": "You hear sounds of a shootout"
                    },
                    {
                        "event_id": "bodyguard_protected",
                        "targets": [
                            "3" # Inform player with id=3
                        ],
                        "message": "You were protected by a bodyguard"
                    },
                    {
                        "event_id": "bodyguard_protected",
                        "targets": [
                            "6" # Inform player with id=6
                        ],
                        "message": "You were killed by the Bodyguard defending your target"
                    },
                    {
                        "event_id": "bodyguard_protected",
                        "targets": [
                            "8" # Inform player with id=8
                        ],
                        "message": "You died defending your target"
                    }
                ]
            },
            {
                "group_id": "doctor_revive",
                "duration": 0,
                "events": [
                    {
                        "event_id": "doctor_revive_success",
                        "targets": "4",
                        "message": "Your target was attacked last night, but you successfully revived them"
                    },
                    {
                        "event_id": "revive_by_doctor",
                        "targets": [
                            "8"
                        ],
                        "message": "You were revived by a doctor. Rock on"
                    }
                ]
            }
        ]
    }
]
```
