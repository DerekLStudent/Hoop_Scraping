from player import player
from player_iterator import player_iterator
import pandas as pd

class roster:
    def __init__(self):
        self.fullRoster = []
        self.playIter = player_iterator(self.fullRoster)
        
    
    def getAvgPoints(self):
        totalSum = 0
        for ppg in self.playIter.getPoints():
            totalSum += float(ppg)
            
        return totalSum / len(self.fullRoster)
    
        
    def playerInRoster(self, player):
        for man in self.fullRoster:
            if man.name == player.name and man.year == player.year:
                return True
        
        return False
        
    def addToRoster(self, player):
        if not self.playerInRoster(player):
            if(len(self.fullRoster) < 15):
                self.fullRoster.append(player)
                print("Added", player.name, "to roster.")
            else:
                print("You can only have 15 players on a roster. Who do you want to remove?")
                self.displayFullRoster()
                
        
    def clearLastPlayer(self):
        self.fullRoster.pop()
            
    def clearRoster(self):
        self.fullRoster.clear()
        
            
    def rosterDF(self):
        perGameHeaders = ['Name','Year','Pos','Ht','PPG','RPG','APG','SPG','BPG','2P%','3P%','FT%','MPG']
        rosterDf = pd.DataFrame(columns = perGameHeaders)
        
        for man in self.fullRoster:
            
            rosterDf = rosterDf.append({
            'Name': man.name,
            'Year': man.year,
            'Pos': man.position,
            'Ht': man.height,
            'PPG': man.stats.PPG,
            'RPG': man.stats.RPG,
            'APG': man.stats.APG,
            'SPG': man.stats.SPG,
            'BPG': man.stats.BPG,
            '2P%': man.stats.TwosPercent,
            '3P%': man.stats.ThreesPercent,
            'FT%': man.stats.FTPercent,
            'MPG': man.stats.MPG
            }, ignore_index=True)
            
        return rosterDf
            