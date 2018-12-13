def score_match(player_tip, match_result):
     '''
     Compare two tuples and derive scores
     '''
     player_tip_diff = player_tip[0] - player_tip[1]
     match_result_diff = match_result[0] - match_result[1]
     
     # Exact tip
     if player_tip == match_result:
          score = 3
     # Not exact tip      
     else:
          # Got draw right
          if player_tip_diff == 0 and match_result_diff == 0:    
               score = 1
          # Wrong with one draw (need to catch this to avoid ZeroDivisionError)
          elif not all([player_tip_diff, match_result_diff]):
               score = 0
          # Got winner right   
          elif player_tip_diff*1/abs(player_tip_diff) == match_result_diff*1/abs(match_result_diff):
               score = 1
          # Wrong
          else:    
               score = 0
     
     return score

