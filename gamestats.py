class gamestats:
    def __init__(self, PPG, RPG, APG, SPG, BPG, FTPercent, TwosPercent, ThreesPercent, MPG):
        self.PPG = PPG
        self.RPG = RPG
        self.APG = APG
        self.SPG = SPG
        self.BPG = BPG
        self.FTPercent = FTPercent
        self.TwosPercent = TwosPercent
        self.ThreesPercent = ThreesPercent
        self.MPG = MPG
        
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
        