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

if __name__ == '__main__':

    main()