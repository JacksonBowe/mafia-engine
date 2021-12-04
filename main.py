'''
This file houses all of the user-facing commands such as create_game, build_game, resolve_state
'''



players = ["Amy", "Bob", "Cat", "Dog", "Frog", "Egg", "Groot"]
roles = ["Citizen", "Citizen", "Citizen", "Citizen", "Citizen", "Mafioso", "Mafioso"]



def main():
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