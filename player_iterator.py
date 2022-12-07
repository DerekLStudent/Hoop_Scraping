#ITERATOR DESIGN PATTERN USED

from player import player
from gamestats import gamestats

#iterator used for going through a player list
class player_iterator():
    def __init__(self, players):
        self.players = players
    
    #iterates through a player list but only yields their ppg stat
    def getPoints(self):
        for play in self.players:
            yield play.stats.PPG
            
    
        