from player import player
from gamestats import gamestats

class player_iterator():
    def __init__(self, players):
        self.players = players
    
    def getPoints(self):
        for play in self.players:
            yield play.stats.PPG
            
    
        