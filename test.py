import json
import random
import __init__ as Mafia

from logger import logger

def main():
    print('Testing multi action game')
    
    with open('sample-lobby.json', 'r') as l:
        players = json.load(l)['players']
        
    with open('test-game-save.json', 'r') as s:
        save = json.load(s)
        
    print('Creating game')
    game = Mafia.create_game(players, save)
    
    # print('GameState', json.dumps(game.dump_state(), indent=4))
    # print('ActorsState', json.dumps(game.dump_actors(), indent=4))
    
    game_state = game.dump_state()
    actors_state = game.dump_actors()
    
    print(json.dumps(game_state, indent=4))
    print(json.dumps(actors_state, indent=4))
    
    while True:
        print("\nLooping\n")
        game = Mafia.load_game(game_state, actors_state, save)
        game.state.generate_allies_and_possible_targets()
        for actor in game.state.actors:
            
            if not actor.alive: continue
            # print(actor, actor.possible_targets)
            for possible_targets in actor.possible_targets:
                target = random.choice(possible_targets).number
                actor.targets.append(target)
                print(f'Actor {actor} targetting {target}')

            
        game.resolve_actions()
        game_state = game.dump_state()
        actors_state = game.dump_actors()
        
        print("\nAlive")
        for actor in game.state.alive_actors:
            print(actor)
        
        print("\nDead")
        for actor in game.state.dead_actors:
            print(actor)
            
        print()
        
        if game.state.check_for_win():
            break
        
        input()
    
    
if __name__ == "__main__":
    main()
    