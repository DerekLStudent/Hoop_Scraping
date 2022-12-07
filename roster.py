from player import player
from player_iterator import player_iterator
import pandas as pd

#holds a list of players the user wants to keep in their roster
class roster:
    #initialize with player list and player iterator
    def __init__(self):
        self.fullRoster = []
        self.playIter = player_iterator(self.fullRoster)    #player iterator used
        
    #get the average ppg of the roster using the player iterator object
    def getAvgPoints(self):
        totalSum = 0
        for ppg in self.playIter.getPoints():
            totalSum += float(ppg)
            
        return totalSum / len(self.fullRoster)
    
        
    #returns true if a given player is already in the roster by checking name and year
    def playerInRoster(self, player):
        for man in self.fullRoster:
            if man.name == player.name and man.year == player.year:
                return True
        
        return False
    
    #adds a player to the roster as long as the roster doesn't have more than 15 players
    def addToRoster(self, player):
        if not self.playerInRoster(player):
            if(len(self.fullRoster) < 15):
                self.fullRoster.append(player)
                print("Added", player.name, "to roster.")
            else:
                print("You can only have 15 players on a roster. Who do you want to remove?")
                self.displayFullRoster()
                
        
    #removes last player added to roster
    def clearLastPlayer(self):
        self.fullRoster.pop()
            
    #clears entire roster
    def clearRoster(self):
        self.fullRoster.clear()
        
            
    #returns a pd dataframe of the roster
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
            