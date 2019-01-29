import tournament
import tipgame
import datetime

fifa2018 = {
    "GroupA": ["Egypt", "Russia", "Saudi-Arabia", "Uruguay"],
    "GroupB": ["Iran", "Marocco", "Portugal", "Spain"],
    "GroupC": ["Australia", "Denmark", "France", "Peru"],
    "GroupD": ["Argentina", "Croatia", "Iceland", "Nigeria"]
}

fifa2018_match_dates = {
 'GroupA0': datetime.datetime(2018, 6, 30, 16, 0),
 'GroupA1': datetime.datetime(2018, 7, 1, 16, 0),
 'GroupA2': datetime.datetime(2018, 7, 2, 16, 0),
 'GroupA3': datetime.datetime(2018, 7, 3, 16, 0),
 'GroupA4': datetime.datetime(2018, 7, 4, 16, 0),
 'GroupA5': datetime.datetime(2018, 7, 5, 16, 0),
 'GroupB0': datetime.datetime(2018, 7, 12, 16, 0),
 'GroupB1': datetime.datetime(2018, 7, 13, 16, 0),
 'GroupB2': datetime.datetime(2018, 7, 14, 16, 0),
 'GroupB3': datetime.datetime(2018, 7, 15, 16, 0),
 'GroupB4': datetime.datetime(2018, 7, 16, 16, 0),
 'GroupB5': datetime.datetime(2018, 7, 17, 16, 0),
 'GroupC0': datetime.datetime(2018, 7, 6, 16, 0),
 'GroupC1': datetime.datetime(2018, 7, 7, 16, 0),
 'GroupC2': datetime.datetime(2018, 7, 8, 16, 0),
 'GroupC3': datetime.datetime(2018, 7, 9, 16, 0),
 'GroupC4': datetime.datetime(2018, 7, 10, 16, 0),
 'GroupC5': datetime.datetime(2018, 7, 11, 16, 0),
 'GroupD0': datetime.datetime(2018, 6, 24, 16, 0),
 'GroupD1': datetime.datetime(2018, 6, 25, 16, 0),
 'GroupD2': datetime.datetime(2018, 6, 26, 16, 0),
 'GroupD3': datetime.datetime(2018, 6, 27, 16, 0),
 'GroupD4': datetime.datetime(2018, 6, 28, 16, 0),
 'GroupD5': datetime.datetime(2018, 6, 29, 16, 0)
}


# Init tournament
t = tournament.Tournament(fifa2018, fifa2018_match_dates)


# Init game
game = tipgame.TipGame(game_name='my_game', tour=t)

# Init players
game.add_player('Player1')
game.add_player('Player2')


class Editor():
     '''
     Class to build user facing CLI interface
     '''
     def __init__(self):
          self.menu_map = {
                    "tip": self.tip,
                    "score": self.score,
                    "quit": self.quit
                    }
     
     def tip(self):
          '''
          Register and store tips from user input
          '''
          done = False
          while not done:
               # Ask for user input
               player_name = raw_input("Player: ")
               match = tuple(raw_input("Match (group and teams separated by comma): ").strip().split(","))
               tip = tuple([int(i) for i in raw_input("Tip (result separeted by comma): ").strip().split(",")])
               
               try:
                    game.make_tip(player_name, match, tip)
                    done = True
               except tipgame.PlayerNotExists:
                    print "This player does not participate in game!"
                    return
               except tipgame.MatchNotInTournament:
                    print "This match is not part of tournament!"
                    return
               except tipgame.PlayerAlreadyMadeTip:
                    print "This player already made tip for this match!"
                    return
               else:
                    print "Tip successful: {} has tipped {} for {}".format(player_name, tip, match)
     
     
     def score(self):
          '''
          Score match from user input and update results
          '''
          done = False
          while not done:
               # Ask for user input
               match = tuple(raw_input("Match (group and teams separated by comma): ").strip().split(","))
               result = tuple([int(i) for i in raw_input("Tip (result separeted by comma): ").strip().split(",")])
               
               try:
                    game.update_scores(match, result)
                    done = True
               except tipgame.MatchNotInTournament:
                    print "This match is not part of tournament!"
                    return
               except tipgame.NoTipsForMatch:
                    print "There are no tips for this match!"
                    return
               except tipgame.MatchAlreadyScored:
                    print "This match has already been scored!"
                    return
               else:
                    print "Game updated successfully: {} resulted in {}".format(match, result) 
     
     
     def quit(self):
          '''
          Exit user facing CLI interface
          '''
          raise SystemExit()
     
     
     def menu(self):
          '''
          Build user menu
          '''
          try:
               answer = ""
               while True:
                    # Define user interface
                    print(
                    '''
Please enter a command:   
\ttip\tTo make a tip
\tscore\tTo score a match
\tquit\tTo quit game
                    ''')
                    
                    answer = raw_input("Enter your choice: ").lower() 
                    try:
                         func = self.menu_map[answer]
                    except KeyError:
                         print "{} is not a valid command".format(answer)
                    else:
                         func()
                         
          finally:
               print "Thank you for using Tip-Game"
                    
Editor().menu()