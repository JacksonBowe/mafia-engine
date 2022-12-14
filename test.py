import __init__ as Mafia
import json

from logger import logger



def main():
    print('Testing game creation')
    
    
    with open('sample_lobby.json', 'r') as l:
        players = json.load(l)['players']
        
    with open('test-game-save.json', 'r') as s:
        save = json.load(s)
        
    game = Mafia.create_game(players, save)
    
    print('Game', game)
    
    print('GameState', json.dumps(game.state, indent=4))
    print('ActorsState', json.dumps(game.actors, indent=4))
    
def resolve():
    print("Testing game resolve")
    
    with open('sample_game_state.json', 'r') as pgs:
        prev_game_state = json.load(pgs)
        
    with open('sample_game_actors.json', 'r') as ga:
        players = json.load(ga)
        
    with open('test-game-save.json', 'r') as s:
        save = json.load(s)
        
    # Do I need to supply the game save? Unsure. Lets see
    game = Mafia.load_game(prev_game_state, players, save)
    
    game.resolve_actions()
    

if __name__ == '__main__':

    resolve()