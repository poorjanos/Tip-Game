import player
from Utils.data_manipulation import score_tuples

class TipGame:
    '''
    Class to manage and score tips
    '''
    def __init__(self, game_name, tour):
        self.game_name = game_name
        self.players = {}
        self.tour = tour
        self.tips = {}
        self.results = {}

     
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
              if match in self.results:
                   raise ValueError
              
              self.results[match] = result 
               
              for player_name in tips_made.keys():
                   player_tip = tips_made[player_name]
                   score = score_tuples(player_tip, result)
                   
                   self.players[player_name].tip_history[match] = score
         
         except KeyError:
              print 'No tips exist for match!'
         
         except ValueError:
              print 'Match already scored!'

           
         
             
              
               
             
             
    
     
    def get_results(self):
        pass
