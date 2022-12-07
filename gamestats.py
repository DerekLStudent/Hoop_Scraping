#class to organize a players per game stats
class gamestats:
    def __init__(self, PPG, RPG, APG, SPG, BPG, FTPercent, TwosPercent, ThreesPercent, MPG):
        self.PPG = PPG  #points per game
        self.RPG = RPG  #rebounds per game
        self.APG = APG  #assists per game
        self.SPG = SPG  #steals per game
        self.BPG = BPG  #blocks per game
        self.FTPercent = FTPercent              #free throw percentage
        self.TwosPercent = TwosPercent          #two point percentage
        self.ThreesPercent = ThreesPercent      #three point percentage
        self.MPG = MPG  #minutes per game
        
    #print to console test function
    def displayStats(self):
        print("PPG:", self.PPG)
        print("RPG:", self.RPG)
        print("APG:", self.APG)
        print("SPG:", self.SPG)
        print("BPG:", self.BPG)
        print("2P%:", self.TwosPercent)
        print("3P%:", self.ThreesPercent)
        print("FT%:", self.FTPercent)
        print("MPG:", self.MPG)
        