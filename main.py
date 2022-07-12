import json

'''
This file houses all of the user-facing commands such as create_game, build_game, resolve_state
It is essentially the API
'''

# from mafia_engine import MafiaEngine
from controller import MafiaController

with open('players.json', 'r') as p:
    players = json.load(p)

with open('sample_game_save.json', 'r') as s:
    save = json.load(s)



def main():
    Mafia = MafiaController()
    game = Mafia.create_game(players, save)
    # Mafia = MafiaEngine()
    # game = Mafia.create_game(players=players, roles=roles)
    # print("\nPrinting GameState")
    # print(json.dumps(game, indent=4))
    pass




if __name__ == "__main__":
    main()






'''
Game Builder:
    This should take in a GameSave and a PlayerList, the output should be a GameState

GameState:
    This object should represent the complete state of a game
    {
        day: int,
        actors: [
            {
                number: int,
                userid: str,
                nickname: str,
                role: str (to be converted to object on Game.ResolveState)
                target: [] (can be a list in event of two-target night actions),
                house: int (what house is the actor at on this night),
            
            }
        ], ...
    }
'''