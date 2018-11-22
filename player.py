class Player:
    '''
    Class to hold information about player.
    '''
    def __init__(self, player_name):
        assert isinstance(player_name, str), 'Player name must be character'
        self.player_name = player_name
        self.tip_history = {}

    def get_score(self):
         return sum(self.tip_history.values())