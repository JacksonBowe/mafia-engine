# Mafia Engine

This project contains the game logic for my serverless multiplayer game Mafia (the party game). To follow this project, check out the discord at https://discord.gg/EcGx9h2fwy

## About
For context, my game consists of (currently) two seperate repos. 

The primary codebase(private) contains everything nessesary to run and deploy game. It handles all the communication between players, the hosting, the user authentication... all the boring "non-game" stuff.

The secondary codebase(this one) is responsible for all the game logic. My intention is to make the this repo into a general purpose Mafia package.

## How it works
There are 3 primary functions that can be executed:
* new_game()
* load_game()
* resolve_game()

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

Using the config file a game is created and the role lineup chosen. Each player then gets assigned a role. If the engine cannot determine a valid role the default is Citizen.

The result looks like this:
```
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

## Loading games
Not as interesting as creating a new Game. 