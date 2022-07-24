'''
This file houses all of the user-facing commands such as create_game, build_game, resolve_state
It is essentially the API
'''
import json
import logging
import random
from controller import MafiaController



def main2():
    logging.basicConfig(filename="log.txt",
        level=logging.DEBUG, 
        format="[%(funcName)s][%(levelname)s] \t%(message)s",
        filemode="w")

    with open('test-actors.json', 'r') as l:
        players = json.load(l)

    with open('test-game-save.json', 'r') as s:
        save = json.load(s)

    with open('test-game-state.json', 'r') as st:
        state = json.load(st)

    # apply state
    game = MafiaController().load_game(players, save, state)
    
    with open('test-actors-output.json', 'w') as f:
        f.write(json.dumps([actor.state for actor in game.actors], indent=4))   
        
        # log("Saving GameState to file 'output-game-state.json'...")
    with open('test-game-state-output.json', 'w') as f:
        f.write(json.dumps(game.dump(), indent=4))
        
        
    game.resolve()
    
    with open('resolve-test-actors-output.json', 'w') as f:
        f.write(json.dumps([actor.state for actor in game.actors], indent=4))   
        
        # log("Saving GameState to file 'output-game-state.json'...")
    with open('resolve-test-game-state-output.json', 'w') as f:
        f.write(json.dumps(game.dump(), indent=4))
    
    # print(json.dumps(game.dump(), indent=4))
    
    pass

def main():
    logging.basicConfig(filename="log.txt",
        level=logging.DEBUG, 
        format="[%(funcName)s][%(levelname)s] \t%(message)s",
        filemode="w")

    with open('test-actors.json', 'r') as l:
        players = json.load(l)

    with open('test-game-save.json', 'r') as s:
        save = json.load(s)

    with open('test-game-state.json', 'r') as st:
        state = json.load(st)

    while True:
        print()
        for player in players:
            player['targets'] = []
            if not player['possible_targets']: continue
            
            if player['role'] == "Citizen":
                # continue
                if not player['possible_targets'][0]: continue

                # 50/50 if the citizen will target itself
                if random.choice(([False] * 5) + ([True]*state['day'])): 
                    target = [random.choice(player['possible_targets'][0])]
                    player['targets'] = target

            else:
                # Pick a random target and target them
                targets = list()
                for i, possible_targets in enumerate(player["possible_targets"]):
                    if not possible_targets: continue
                    target = random.choice(possible_targets)
                    targets.insert(i, target)
                player['targets'] = targets

        game = MafiaController().load_game(players, save, state)
        game.resolve()
        

        players = [actor.state for actor in game.actors]
        # print(json.dumps(players, indent=4))
        state = game.dump()

        if game.check_for_win():
            print("GAME FINISHED")
            break


        print()
        # input("Enter for next turn")






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