import tournament
import tipgame

# Init tournament
fifa2018 = {
    "GroupA": ["Egypt", "Russia", "Saudi-Arabia", "Uruguay"],
    "GroupB": ["Iran", "Marocco", "Portugal", "Spain"],
    "GroupC": ["Australia", "Denmark", "France", "Peru"],
    "GroupD": ["Argentina", "Croatia", "Iceland", "Nigeria"]
}
t = tournament.Tournament(fifa2018)

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
