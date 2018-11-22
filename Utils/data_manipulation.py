def score_tuples(tuple_a, tuple_b):
     '''
     Compare two tuples and derive scores
     '''
     tuple_a_diff = tuple_a[0] - tuple_a[1]
     tuple_b_diff = tuple_b[0] - tuple_b[1]
     
     # Exact match
     if tuple_a == tuple_b:
          score = 3
     # Not exact match      
     else:
          # Got draw right
          if tuple_a_diff == 0 and tuple_b_diff == 0:    
               score = 1
          # Wrong with one draw (need to catch here to avoid ZeroDivisionError)
          elif not all([tuple_a_diff, tuple_b_diff]):
               score = 0
          # Got winner right   
          elif tuple_a_diff*1/abs(tuple_a_diff) == tuple_b_diff*1/abs(tuple_b_diff):
               score = 1
          # Wrong
          else:    
               score = 0
     
     return score

