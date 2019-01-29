from itertools import combinations

class Tournament:
    '''
    Class to create and hold matches in a given tournament. Takes dict with groups as keys and team lists as values
    to initialize.
    '''
    def __init__(self, groups, match_dates):
        assert isinstance(groups, dict), 'Groups must be dictionary'
        self.groups = groups
        self.match_dates = match_dates
        self.matches = self.gen_matches(self.groups)
        self.results = {}


    def gen_matches(self, groups):
        '''
        Generates matches with unique id
        '''
        res = {}
        for group, _ in self.groups.iteritems():
             teams = self.groups[group]
             matches = [(group + str(num), comb[0], comb[1]) for num, comb in enumerate(combinations(teams, 2))]
             res[group] = matches
        return res     
    
     
    def get_matches(self):
        '''
        Returns all matches of tournament as list of tuples
        '''
        return [match for pairs in self.matches.itervalues() for match in pairs]


    def add_playoffs(self, playoff_round, matches, playoff_dates):
        '''
        Updates tournament with playoffs
        '''
        assert isinstance(matches, list), 'matches must be list of tuples'
        assert isinstance(playoff_dates, dict), 'playoff_dates must be dict'
        self.matches[playoff_round] = matches
        self.match_dates.update(playoff_dates)
