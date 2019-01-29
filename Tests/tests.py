import tournament
import tipgame
import datetime as datetime

# Init tournament
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

t = tournament.Tournament(fifa2018, fifa2018_match_dates)

     
# Init game
g = tipgame.TipGame(game_name='afc_game', tour=t)

# Init players
g.add_player('Jancsi')
g.add_player('Matyi')

# Make tips
g.make_tip('Jancsi', ('GroupD1', 'Argentina', 'Iceland'), (1,1))
g.make_tip('Matyi', ('GroupD1', 'Argentina', 'Iceland'), (4,0))
g.make_tip('Jancsi', ('GroupA1', 'Egypt', 'Saudi-Arabia'), (3,1))
g.make_tip('Matyi', ('GroupA1', 'Egypt', 'Saudi-Arabia'), (2,1))

# Update scores
g.update_scores(('GroupD1', 'Argentina', 'Iceland'), (2, 1))
g.update_scores(('GroupA1', 'Egypt', 'Saudi-Arabia'), (2, 1))

# Check scores
g.results
g.players['Jancsi'].tip_history
g.players['Matyi'].tip_history
g.players['Jancsi'].get_score()
g.players['Matyi'].get_score()
