import player

class TipGame:
    '''
    Class to manage and score tips
    '''
    def __init__(self, game_name, tour):
        self.game_name = game_name
        self.players = {}
        self.tour = tour
        self.tips = {}

     
    def add_player(self, player_name):
         self.players[player_name] = player.Player(player_name)
         
     
    def make_tip(self, player_name, match, tip):
         '''
         Make tip for player for given match
         '''
         try:
              # Catch if player does not exist
              player = self.players[player_name]
              
              # Catch if match is not part of tournament
              if match not in self.tour.get_matches():
                   raise NameError
                   
              if match not in self.tips:
                   self.tips[match] = {player.player_name: tip}
              # Catch if player already made tip for match
              elif player_name in self.tips[match].keys():
                   raise ValueError
              elif player_name not in self.tips[match].keys():
                   self.tips[match].update({player.player_name: tip})

         except KeyError:
              print 'Player not in game!'
              
         except NameError:
               print 'Match not in tournament!'
               
         except ValueError:
               print 'Player already made tip for this match!'
              
              
    def update_scores(self, match, result):
         '''
         Update player score and history based on match result
         '''
         try:
              tips_made = self.tips[match]
             
         except KeyError:
              print 'No tips exist for match!'
             
         for player_name in tips_made.keys():
              player_tip = tips_made[player_name]
             
              # Player tipped exact result 
              if player_tip == result:
                   score = 3
              # Player did not tip exact result      
              else:
                   tip_diff = player_tip[0] - player_tip[1]
                   result_diff = result[0] - result[1]
                  
                   # Player tipped draw right  
                   if tip_diff == 0 and result_diff == 0:    
                        score = 1 
                   # Player tipped winner right     
                   elif tip_diff*1/abs(tip_diff) == result_diff*1/abs(result_diff):
                        score = 1
                   # Player tipped wrong
                   else:     
                        score = 0
               
             
             
    
     
    def get_results(self):
        pass
