import player
import datetime
from Utils.data_manipulation import score_match


class PlayerNotExists(Exception):
     '''
     Custom exception to handle non-existing player error
     '''
     pass


class PlayerAlreadyExists(Exception):
     '''
     Custom exception to handle adding existing player error
     '''
     pass


class MatchNotInTournament(Exception):
     '''
     Custom exception to handle match not part of tournament error
     '''
     pass


class PlayerAlreadyMadeTip(Exception):
     '''
     Custom exception to handle player already made tip error
     '''
     pass


class PlayerMadeNoTip(Exception):
     '''
     Custom exception to handle player already made tip error
     '''
     pass


class NoTipsForMatch(Exception):
     '''
     Custom exception to handle no tips for match error
     '''
     pass


class MatchAlreadyScored(Exception):
     '''
     Custom exception to handle match already scored error
     '''
     pass


class MatchAlreadyPlayed(Exception):
     '''
     Custom exception to handle match already played error
     '''
     pass


class TipAlreadyMade(Exception):
     '''
     Custom exception to handle error when attempting to alter tip with same tip 
     '''
     pass




class TipGame:
    '''
    Class to manage and score tips
    '''
    def __init__(self, game_name, tour):
        self.game_name = game_name
        self.players = {}
        self.tour = tour
        self.tips = {}
        #self.results = {}

     
    def add_player(self, player_name):
         if player_name in self.players:
              raise PlayerAlreadyExists(player_name)
         else:
              self.players[player_name] = player.Player(player_name)
         
     
    def make_tip(self, player_name, match, tip, alter = False):
         '''
         Make original tip for given match or alter already existing tip of player
         '''
         try:
              # Check if player exists
              player = self.players[player_name]
         except KeyError:
              raise PlayerNotExists(player_name)
              
         # Check if match is part of tournament
         if match not in self.tour.get_matches():
              raise MatchNotInTournament(match)     
         
         # Check if match has been played
         if self.tour.match_dates[match[0]] < datetime.datetime.now():
              raise MatchAlreadyPlayed(match)    
         
         if not alter:
              # Make original tip
              if match not in self.tips:
                   self.tips[match] = {player.player_name: tip}
                   self.players[player_name].tip_history[match] = [(tip, datetime.datetime.now())]
              # Check if player already made tip for match
              elif player_name in self.tips[match].keys():
                   raise PlayerAlreadyMadeTip(player_name, match)
              else:
                   self.tips[match].update({player.player_name: tip})
                   self.players[player_name].tip_history[match] = [(tip, datetime.datetime.now())]
         else:
              # Alter tip 
              if match not in self.tips:
                   raise NoTipsForMatch(match)
              # Check if player already made tip for match     
              elif not player_name in self.tips[match].keys():
                   raise PlayerMadeNoTip(match)
              # Check if original tip is different from new tip     
              elif self.tips[match][player_name] == tip:
                   raise TipAlreadyMade(match)
              else:
                   self.tips[match].update({player.player_name: tip})
                   self.players[player_name].tip_history[match].append((tip, datetime.datetime.now()))
    
    
    def update_scores(self, match, result):
         '''
         Update player score and history based on match result
         '''
         # Check if match is part of tournament
         if match not in self.tour.get_matches():
              raise MatchNotInTournament(match)
         
         try:
              tips_made = self.tips[match]
         except KeyError:
              raise NoTipsForMatch(match)
              
         if match in self.tour.results:
              raise MatchAlreadyScored(match)
         
         self.tour.results[match] = result 
          
         for player_name in tips_made.keys():
              tip = tips_made[player_name]
              score = score_match(tip, result)
              
              self.players[player_name].score_history[match] = score
         
     
    def get_leaderboard(self, player_name = 'all'):
        if player_name == 'all':
             return sorted([(key, value.get_score()) for key, value in self.players.iteritems()], key = lambda x: x[1], reverse = True)
        else:
             try:
                  return (self.players[player_name].player_name, self.players[player_name].get_score())
             except KeyError:
                  raise PlayerNotExists(player_name)
         
         
