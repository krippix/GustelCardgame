from game.player import Player

class game():
    # pre-game
    id:       int  # id of the game (used for the api)
    password: str
    decklist: list
    players:  list   
    
    # ingame
    phase:    int  # Current turn phase 1-4
    

    def __init__(self, player: Player, id: int):
        
        
        self.players = [player]



    def add_player(self, player: Player):
        self.players.append(player)